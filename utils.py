import tkinter as tk
import re
from constant import *


def validate_email_address(email_address):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # pass the regular expression
    # and the string into the fullmatch() method
    if re.fullmatch(regex, email_address):
        return True
    else:
        return False


def show_password_event_action(entry, button):
    if entry.cget('show') == '':
        entry.config(show='*')
        button.config(text=SHOW_PASSWORD_LABEL)
    else:
        entry.config(show='')
        button.config(text='Hide Password')


def set_grid_row_column_configure(frame, num_rows, num_columns):
    '''
    for row_idx in range(num_rows):
        tk.Grid.rowconfigure(frame, index=row_idx, weight=1)

    for col_idx in range(num_columns):
        tk.Grid.columnconfigure(frame, index=col_idx, weight=1)
    '''


# method to get the table name from email address
def get_table_name_from_email(email, type_string):
    table_name = email
    table_name = table_name[:table_name.index("@")] + type_string
    return table_name


def get_patient_row_as_str(rows):
    # list of patient details which already exists with same name.
    patient_details_str = ""

    row_idx = 0
    for row in rows:
        print("row --", row)
        patient_details_str += (PATIENT_ID + str(row[PATIENT_INFO_ID_INDEX]))
        patient_details_str += ' , '

        if 0 != len(row[PATIENT_INFO_NAME_INDEX]):
            patient_details_str += (PATIENT_NAME + row[PATIENT_INFO_NAME_INDEX])
            patient_details_str += ' , '
        if 0 != len(row[PATIENT_INFO_GENDER_INDEX]):
            patient_details_str += (PATIENT_GENDER + row[PATIENT_INFO_GENDER_INDEX])
            patient_details_str += ' , '
        if 0 != row[PATIENT_INFO_AGE_INDEX]:
            patient_details_str += (PATIENT_AGE + str(row[PATIENT_INFO_AGE_INDEX]))
            patient_details_str += ' , '
        # if 0 != len(row[PATIENT_INFO_DOB_INDEX]):
        #    patient_details_str += (PATIENT_DOB + row[PATIENT_INFO_DOB_INDEX])
        # patient_details_str += ','
        if 0 != len(row[PATIENT_INFO_OCCUPATION_INDEX]):
            patient_details_str += (PATIENT_OCCUPATION + row[PATIENT_INFO_OCCUPATION_INDEX])
            patient_details_str += ' , '
        if 0 != len(row[PATIENT_INFO_MARTIAL_STATUS_INDEX]):
            patient_details_str += (PATIENT_MARTIAL_S + row[PATIENT_INFO_MARTIAL_STATUS_INDEX])
            patient_details_str += ' , '
        if 0 != len(row[PATIENT_INFO_CONTACT_NO_INDEX]):
            patient_details_str += (PATIENT_CONTACT_NO + row[PATIENT_INFO_CONTACT_NO_INDEX])
            patient_details_str += ' , '
        # if 0 != len(row[PATIENT_INFO_ADDRESS_INDEX]):
        #    patient_details_str += (PATIENT_ADDRESS + row[PATIENT_INFO_ADDRESS_INDEX])
        #    patient_details_str += ' , '
        if 0 != len(row[PATIENT_INFO_CITY_INDEX]):
            patient_details_str += (PATIENT_CITY + row[PATIENT_INFO_CITY_INDEX])

        row_idx += 1
        if row_idx != len(rows):
            patient_details_str += "\n"

    return patient_details_str


def get_medical_record_as_str(row):
    medical_record_str = ""

    #   medical_record_str += (PATIENT_ID + str(row[MEDICAL_RECORD_TABLE_ID_INDEX]))
    #   medical_record_str += ' , '

    if 0 != len(str(row[MEDICAL_RECORD_TABLE_RECORD_DATE_INDEX])):
        medical_record_str += (MEDICAL_RECORD_DATE + str(row[MEDICAL_RECORD_TABLE_RECORD_DATE_INDEX]))
        medical_record_str += ' , '
    if 0 != row[MEDICAL_RECORD_TABLE_MEDICINE_INDEX]:
        medical_record_str += (MEDICAL_RECORD_MEDICINES + ' ( ' + row[MEDICAL_RECORD_TABLE_MEDICINE_INDEX])
        medical_record_str += ' ), '
    if 0 != row[MEDICAL_RECORD_TABLE_SYMPTOMS_INDEX]:
        medical_record_str += (MEDICAL_RECORD_SYMPTOMS +
                               row[MEDICAL_RECORD_TABLE_SYMPTOMS_INDEX].replace('\n', ' '))

    return medical_record_str


def encode_single_value(multi_values, deliminator=','):
    encoded_str = ""
    idx = 0
    for value in multi_values:
        encoded_str += value
        if idx + 1 != len(multi_values):
            encoded_str += deliminator
        idx += 1
    return encoded_str


def decode_single_value(medicine_info_string, deliminator=','):
    curr_info_str = ""
    info_list = []
    for ch in medicine_info_string:
        if ch != deliminator:
            curr_info_str += ch
        else:
            # We put the string in the list irrespective of the its length or if its ""
            # so there would be as many entries in the list as number of deliminator + 1
            info_list.append(curr_info_str)
            curr_info_str = ""

    # Place the last string in.
    info_list.append(curr_info_str)
    curr_info_str = ""

    return info_list
