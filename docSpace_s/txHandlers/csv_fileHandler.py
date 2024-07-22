import csv
import time
import os
from constant import *
from threading import Thread, Event
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

'''
Below class handles the CSV file handling.
We have one CSV file which holds the Doctor info.
For a doctor we would have two CSV files corresponding to two tables in the database:.
patient_info.csv
medical_record.csv
CSV file can be of maximum MAX_BACK_UP_CSV_FILE_SIZE(25 MB) size as of now
We create a table in database to keep hold of number of files created as of now.
Entries in the table:
FileName creation Date is_back_up_ed back_up_date_time file_size

'''


# This class has two purpose, one is to implement and run a thread which is responsible for transmitting
# CSV files using gmail.
# Second to perform handling of CSV file.
# This is class which has static elements and exposes different interface function to perform relevant
# tasks.
class CsvHandler(Thread):
    # These are class global static variables.
    patient_info_csv_file_handler = None
    medical_record_csv_file_handler = None
    doctor_info_csv_file_handler = None

    patient_info_csv_file = None
    medical_record_csv_file = None
    doctor_info_csv_file = None

    pending_patient_info_csv_file = None
    pending_medical_record_csv_file = None
    pending_doctor_info_csv_file = None

    patient_info_event = None
    medical_record_event = None
    doctor_info_event = None

    smtp_session = None

    @staticmethod
    def is_new_csv_file_needed(file_name, identifier):

        try:
            # We would update the file only if no existing csv file tx is pending
            if identifier == MEDICAL_RECORD_TYPE_STRING:
                if CsvHandler.medical_record_event is None or \
                   CsvHandler.medical_record_event.is_set():
                    return False
            elif identifier == PATIENT_INFO_TYPE_STRING:
                if CsvHandler.patient_info_event is None or \
                   CsvHandler.patient_info_event.is_set():
                    return False
            else:
                # Doctor info
                if CsvHandler.doctor_info_event is None or \
                   CsvHandler.doctor_info_event.is_set():
                    return False

            # check the file size to decide if new csv file is needed or not
            size = os.path.getsize("./"+file_name)
            if size >= MAX_CSV_FILE_SIZE_BYTES:
                return True
        except Exception as e:
            print("CsvHandler::get_file_size cannot get file size for " + file_name, " exception ", e)

        return False

    @staticmethod
    def create_gmail_transmission_session():
        try:
            # Create SMTP session for sending the mail
            sender_address = 'ravreet.tech.ino@gmail.com'
            sender_pass = 'huigomgnfejammsi'
            CsvHandler.smtp_session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
            CsvHandler.smtp_session.starttls()  # enable security
            CsvHandler.smtp_session.login(sender_address, sender_pass)  # login with mail_id and password
            return True
        except Exception as e:
            CsvHandler.smtp_session = None
            print("CsvHandlers::create_smtp_session:: Unable to create smtp session exception ", e)
            return False

    @staticmethod
    def transmit_csv_file_by_gmail(file_name):
        try:
            mail_content = "DocSpace Back up file" + file_name
            # The mail addresses and password
            sender_address = 'ravreet.tech.ino@gmail.com'
            receiver_address = 'ravreet.tech.ino@gmail.com'

            # Setup the MIME
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'DocSpace Back up:: ' + file_name

            # The subject line
            # The body and the attachments for the mail
            message.attach(MIMEText(mail_content, 'plain'))

            attach_file = open(file_name, 'rb')  # Open the file as binary mode
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload(attach_file.read())
            encoders.encode_base64(payload)  # encode the attachment
            # add payload header with filename
            payload.add_header('Content-Decomposition', 'attachment', filename=file_name)
            message.attach(payload)

            text = message.as_string()
            CsvHandler.smtp_session.sendmail(sender_address, receiver_address, text)

            print('csvhandler::transmit_csv_file CSV file tx ' + file_name)
        except Exception as e:
            print("CsvHandlers::create_smtp_session:: Unable to tx csv file " + file_name + " exception ", e)

    @staticmethod
    def check_transmit_csv_file(event, file_name):
        # If the event is set than perform the below action.
        if file_name is not None and event is not None and event.is_set():
            # transmit the file using gmail attachment
            event.clear()
            CsvHandler.transmit_csv_file_by_gmail(file_name)

    @staticmethod
    def check_transmit_all_csv_file():

        if CsvHandler.smtp_session is None:
            if not CsvHandler.create_gmail_transmission_session():
                return False

        CsvHandler.check_transmit_csv_file(CsvHandler.patient_info_event,
                                           CsvHandler.patient_info_csv_file)
        CsvHandler.check_transmit_csv_file(CsvHandler.medical_record_event,
                                           CsvHandler.medical_record_csv_file)
        CsvHandler.check_transmit_csv_file(CsvHandler.doctor_info_event,
                                           CsvHandler.doctor_info_csv_file)
        return True

    # Override the run method which will be called when thread is started
    # Main task of this thread is to keep on polling and check if a csv file
    # (patient/medical/doctor) is updated or not. update is indicated using event
    # by the main thread.
    # If update is interpreted then transmit the file using gmail attachment.
    def run(self):
        while True:

            # Check and update the csv file to tx before performing the transmission
            if CsvHandler.pending_doctor_info_csv_file is not None:
                CsvHandler.doctor_info_csv_file = CsvHandler.pending_doctor_info_csv_file
            elif CsvHandler.pending_patient_info_csv_file is not None:
                CsvHandler.patient_info_csv_file = CsvHandler.pending_patient_info_csv_file
            elif CsvHandler.pending_medical_record_csv_file is not None:
                CsvHandler.medical_record_csv_file = CsvHandler.pending_medical_record_csv_file

            if not CsvHandler.check_transmit_all_csv_file():
                # If we are unable to transmit CSV files sleep for 60
                # seconds and try again.
                time.sleep(60)

            time.sleep(60)

    @staticmethod
    # Saves the record into the input csv file.
    def save_record_to_csv_file(file_name, identifier, record, is_file_update_pending):

        try:
            # In case corresponding handler is not set first open and set the file handler.
            if identifier == MEDICAL_RECORD_TYPE_STRING:
                if CsvHandler.medical_record_csv_file_handler is None:
                    CsvHandler.medical_record_csv_file_handler = open(file_name, "a", newline="")
                    CsvHandler.medical_record_csv_file = file_name
                    CsvHandler.medical_record_event = Event()

                if is_file_update_pending:
                    # close the previous file handler
                    CsvHandler.medical_record_csv_file_handler.close()
                    CsvHandler.medical_record_csv_file_handler = open(file_name, "a", newline="")
                    CsvHandler.pending_medical_record_csv_file = file_name

                writer = csv.writer(CsvHandler.medical_record_csv_file_handler)
                writer.writerow(record)
                CsvHandler.medical_record_csv_file_handler.flush()

                # set the event so that the handler thread can pick the csv for transmission via gmail
                CsvHandler.medical_record_event.set()
            elif identifier == PATIENT_INFO_TYPE_STRING:
                if CsvHandler.patient_info_csv_file_handler is None:
                    CsvHandler.patient_info_csv_file_handler = open(file_name, "a", newline="")
                    CsvHandler.patient_info_csv_file = file_name
                    CsvHandler.patient_info_event = Event()

                if is_file_update_pending:
                    # close the previous file handler
                    CsvHandler.patient_info_csv_file_handler.close()
                    CsvHandler.patient_info_csv_file_handler = open(file_name, "a", newline="")
                    CsvHandler.pending_patient_info_csv_file = file_name

                writer = csv.writer(CsvHandler.patient_info_csv_file_handler)
                writer.writerow(record)
                CsvHandler.patient_info_csv_file_handler.flush()

                # set the event so that the handler thread can pick the csv for transmission via gmail
                CsvHandler.patient_info_event.set()
            else:
                if CsvHandler.doctor_info_csv_file_handler is None:
                    # This is the case of DOCTOR INFO.
                    CsvHandler.doctor_info_csv_file_handler = open(file_name, "a", newline="")
                    CsvHandler.doctor_info_csv_file = file_name
                    CsvHandler.doctor_info_event = Event()

                if is_file_update_pending:
                    # close the previous file handler
                    CsvHandler.doctor_info_csv_file_handler.close()
                    CsvHandler.doctor_info_csv_file_handler = open(file_name, "a", newline="")
                    CsvHandler.pending_doctor_info_csv_file = file_name

                writer = csv.writer(CsvHandler.doctor_info_csv_file_handler)
                writer.writerow(record)
                CsvHandler.doctor_info_csv_file_handler.flush()

                # set the event so that the handler thread can pick the csv for transmission via gmail
                CsvHandler.doctor_info_event.set()
        except Exception as e:
            print("CsvHandler::save_record_to_csv_file: Error writing to file ", file_name, " record ", record,
                  " Exception ", e)
            # As of now continue the App even in case we get an Exception.

    @staticmethod
    def close_csv_file_handlers():
        print("Closing CSV file ")
        try:
            # Check and send the file explicitly and clear the Event in process of doing so.
            CsvHandler.check_transmit_all_csv_file()

            # Close all the handlers and set them to None.
            if CsvHandler.patient_info_csv_file_handler is not None:
                CsvHandler.patient_info_csv_file_handler.close()

            if CsvHandler.doctor_info_csv_file_handler is not None:
                CsvHandler.doctor_info_csv_file_handler.close()

            if CsvHandler.medical_record_csv_file_handler is not None:
                CsvHandler.medical_record_csv_file_handler.close()

            CsvHandler.patient_info_csv_file_handler = None
            CsvHandler.medical_record_csv_file_handler = None
            CsvHandler.doctor_info_csv_file_handler = None

            CsvHandler.medical_record_csv_file = None
            CsvHandler.patient_info_csv_file = None
            CsvHandler.doctor_info_csv_file = None

            CsvHandler.medical_record_event = None
            CsvHandler.patient_info_event = None
            CsvHandler.doctor_info_event = None

        except Exception as e:
            print("CsvHandler::close_csv_file Error Closing CSV file ", e)
