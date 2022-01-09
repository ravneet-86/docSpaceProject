import mysql.connector
import os
import pipes
from constant import *
from utils import *
from patient_details import PatientDetails
import pandas as pd
from global_app_data import *

ENABLE_DB_DEBUG = True


# Class to perform DataBase connection and perform database operations.
class DbController:

    # Below are the core SQL Implementation functions use to query the Database using
    # mySql queries. These are not meant to be called outside of the DB Controller.

    def _db_delete_table(self, table):
        # Run insert for given table.
        try:
            sql = "drop table " + DB_NAME + "." + table

            if ENABLE_DB_DEBUG:
                print("dbController:db_delete_table Deleting table with query ", sql)
            self.db_cursor.execute(sql)
            self.db_connector.commit()
            return True
        except Exception as e:
            print("DbController:_db_create_table: Failed to run create table query DB: ", DB_NAME)
            print("Sql statement ", sql, "exception: ", e)
            return False

    def _db_create_table(self, table):
        # Run insert for given table.
        try:
            sql = "create table " + DB_NAME + "." + table

            if ENABLE_DB_DEBUG:
                print("dbController:db_create_table Creating table with query ", sql)
            self.db_cursor.execute(sql)
            self.db_connector.commit()
            return True
        except Exception as e:
            print("DbController:_db_create_table: Failed to run create table query DB: ", DB_NAME)
            print("Sql statement ", sql, "exception: ", e)
            return False

    def _db_insert(self, table, column_string, values):
        # Run insert for given table.
        try:
            sql = "Insert into " + DB_NAME + "." + table + " " + column_string + " values "

            for i in range(len(values)):
                if 0 == i:
                    sql += "(%s"
                else:
                    sql += ", %s"

                if i + 1 == len(values):
                    sql += ")"

            if ENABLE_DB_DEBUG:
                print("dbController:_db_insert Running insert query ", sql, " values ", values)
            self.db_cursor.execute(sql, values)
            self.db_connector.commit()
            return True
        except Exception as e:
            print("DbController:db_insert: Failed to insert query table", DB_NAME + "." + table,
                  " values ", values, " Size ",
                  len(values))
            print("Sql statement ", sql, "exception: ", e)
            return False

    def _db_update(self, table, column_name_list, values, where_params):
        # Example update anand_patient_info set name = "sarv" where patient_id = 1 and date = 1990-12-2;
        value_idx = 0
        sql = "update " + DB_NAME + "." + table + " set "
        try:
            for col_name in column_name_list:

                sql += col_name + " = '" + values[value_idx] + "'"

                if value_idx + 1 != len(values):
                    sql += ' , '
                else:
                    idx = 0
                    sql += ' where '
                    for where_name, where_value in where_params:
                        sql += where_name + " = '" + where_value + "'"
                        if (idx + 1) != len(where_params):
                            sql += ' and '
                        else:
                            sql += ';'
                        idx += 1

                value_idx += 1

            if ENABLE_DB_DEBUG:
                print("dbController:_db_update Running update query ", sql, " values ", values)
            self.db_cursor.execute(sql)
            self.db_connector.commit()
            return True
        except Exception as e:
            print("DbController:db_update: Failed to update query table", DB_NAME + "." + table,
                  " values ", values, " Size ",
                  len(values))
            print("Sql statement ", sql, "exception: ", e)
            return False

    # Function to get the last inserted row in the given table
    # Note this will work only for table which has single auto increment primary key.
    def _db_get_last_inserted_row(self, table, key_id):
        try:
            sql = "select * from " + DB_NAME + "." + table + " where " + key_id + " = ( select last_insert_id() );"

            if ENABLE_DB_DEBUG:
                print("_db_get_last_inserted_row:_db_get_rows Running select query ", sql)
            self.db_cursor.execute(sql)
            rows = self.db_cursor.fetchall()
            return True, rows

        except Exception as e:
            print("DbController:_db_get_last_inserted_row: Failed to get rows for table ", DB_NAME + "." + table)
            print("Sql statement ", sql, "exception: ", e)
            return False, None

    # Function to get the rows of a given table
    def _db_get_rows(self, table):
        try:
            sql = "select * from " + DB_NAME + "." + table

            if ENABLE_DB_DEBUG:
                print("dbController:_db_get_rows Running select query ", sql)
            self.db_cursor.execute(sql)
            rows = self.db_cursor.fetchall()
            return True, rows
        except Exception as e:
            print("DbController:db_insert: Failed to get rows for table ", DB_NAME + "." + table)
            print("Sql statement ", sql, "exception: ", e)
            return False, None

    # Function to get the rows of a given table under the select where query using where_params
    def _db_get_rows(self, table, where_params):
        index = 0
        for param in where_params:
            # Form the select where query if its the first parameter
            if 0 == index:
                sql = "select * from " + DB_NAME + "." + table + " where " + \
                      param[0] + "='" + param[1] + "'"
            else:
                sql += " and " + param[0] + "='" + param[1] + "'"

            index += 1
            if index == len(where_params):
                sql += ";"

        try:
            if ENABLE_DB_DEBUG:
                print("db_controller:_db_get_rows where clause executing sql ", sql, " where params ", where_params)

            self.db_cursor.execute(sql)
            rows = self.db_cursor.fetchall()
            return True, rows
        except Exception as e:
            print("DbController:db_get_rows where: Failed to get rows for table ", DB_NAME + "." + table)
            print("Sql statement ", sql, " where params ", where_params, "exception: ", e)
            return False, None

    # Creates and run db query to select rows basesd upon like parameters to encorporate regular expression
    # ex below:
    # select * from anand_patient_info where name like ('s%') or address like ('da%') or occupation like ('u%');
    def _db_get_rows_like(self, table, like_params, contains_or_start_with):
        index = 0

        sql = ""
        for param in like_params:
            # Form the select where query if its the first parameter
            if 0 == index:
                # True indicates we should get the rows which contains the parameter string.
                if contains_or_start_with:
                    sql = "select * from " + DB_NAME + "." + table + " where " + \
                          param[0] + " like ('%" + param[1] + "%')"
                else:  # False indicates we should get the rows which start with the parameter string
                    sql = "select * from " + DB_NAME + "." + table + " where " + \
                          param[0] + " like ('" + param[1] + "%')"
            else:
                # True indicates we should get the rows which contains the parameter string.
                if contains_or_start_with:
                    sql += " or " + param[0] + " like ('%" + param[1] + "%')"
                else:  # False indicates we should get the rows which start with the parameter string
                    sql += " or " + param[0] + " like ('" + param[1] + "%')"

            index += 1
            if index == len(like_params):
                sql += ";"

        try:
            if ENABLE_DB_DEBUG:
                print("db_controller:_db_get_rows_like where clause executing sql ", sql, " where params ",
                      like_params)

            df = pd.read_sql(sql, self.db_connector)

            if ENABLE_DB_DEBUG:
                print("returned df ", df)

            return True, df
            # self.db_cursor.execute(sql)
            # rows = self.db_cursor.fetchall()
            # return True, rows
        except Exception as e:
            print("DbController:db_get_rows_like where: Failed to get rows for table ", DB_NAME + "." + table)
            print("Sql statement ", sql, " where params ", like_params, "exception: ", e)
            return False, None

    # Below are the interface functions which are accessed by the Application frames
    # to Query or Get Data already Queried from DB.
    # Function to check if DB is connected successfully or not after object creation.
    def is_db_connected(self):
        if 0 != len(self.error):
            # Currently we can have only one error message. use index 0, If needed we should
            # append all the error messages
            error_msg = self.error[0]
            return error_msg
        else:
            return ""

    # Function to check the doctor info w.r.t to input email and password, if succesful info is found this also
    # sets the internal parameters for doctor info which would be used during login
    def db_check_doctor_info(self, email, password):
        # Form the where parameters for the query
        where_params = [(DOCTOR_INFO_EMAIL_COL_NAME, email)]
        status, rows = self._db_get_rows(DOCTOR_INFO_TABLE, where_params)

        error_msg = ""
        if not status:
            error_msg = ERROR_CHECKING_EMAIL_ADDRESS
        elif 0 == len(rows):
            error_msg = ERROR_EMAIL_USER_NOT_EXIST
        else:
            # This is just a debug check and is not possible to happen as email is a primary key.
            if len(rows) > 1:
                print("db_check_doctor_info: More than one rows for primary email address ", rows)

            for row in rows:
                # Return the first matched email, password entry.
                if row[DOCTOR_INFO_PASSWORD_INDEX] == password:
                    # Save the doctor info for further usage
                    self.doctor_info = row
                    self.patient_info_table = get_table_name_from_email(email,
                                                                        PATIENT_INFO_TYPE_STRING)
                    self.medical_record_table = get_table_name_from_email(email,
                                                                          MEDICAL_RECORD_TYPE_STRING)

                    return error_msg
            # Email is present as non zero rows are returned, but password didn't match.
            error_msg = ERROR_PASSWORD_NOT_MATCHING

        return error_msg

    # Function to check if email address already exists in database or not.
    def check_email_exists(self, email):
        # Form the where parameters for the query
        where_params = [(DOCTOR_INFO_EMAIL_COL_NAME, email)]
        status, rows = self._db_get_rows(DOCTOR_INFO_TABLE, where_params)

        error_msg = ""
        if not status:
            error_msg = ERROR_CHECKING_EMAIL_ADDRESS
        elif 0 != len(rows):
            error_msg = EMAIL_ADDRESS_ALREADY_EXIST

        return error_msg

    # Function to insert values in the doctor info table for doctor's registration.
    def db_register_doctor_info(self, name_entry, email_entry,
                                password_entry, contact_number_entry,
                                mobile_number_entry, clinic_name_entry,
                                clinic_address_entry):

        # Before inserting create a table for the doctor to store patient information.
        patient_info_table = get_table_name_from_email(email_entry, PATIENT_INFO_TYPE_STRING)

        # Step 1: Create Patient info table
        table_sql = patient_info_table + CREATE_TABLE_PATIENT_INFO_STRING

        status = self._db_create_table(table_sql)

        error_msg = ""
        if not status:
            error_msg = ERROR_CREATING_TABLE + "\n" + patient_info_table
            return error_msg

        # Step 2: Create Medical Record table for the patients, in case this fails delete the
        # table created in step 1
        medical_record_table = get_table_name_from_email(email_entry,
                                                         MEDICAL_RECORD_TYPE_STRING)

        table_sql = medical_record_table + CREATE_TABLE_MEDICAL_RECORD_STRING
        status = self._db_create_table(table_sql)

        if not status:
            error_msg = ERROR_CREATING_TABLE + "\n" + medical_record_table
            # delete the table created in step 1.
            self._db_delete_table(patient_info_table)
            return error_msg

        # Table creation is successful, Form the query and run insert for given table.
        values = [name_entry, email_entry, password_entry, contact_number_entry,
                  mobile_number_entry, clinic_name_entry, clinic_address_entry]

        # Step 3: insert the data received in the Data base.
        status = self._db_insert(DOCTOR_INFO_TABLE, DOCTOR_INFO_COL, values)

        if not status:
            error_msg = ERROR_INSERTING_TABLE
            # In case of any Error, delete the table created in step 1 and step 2.
            self._db_delete_table(patient_info_table)
            self._db_delete_table(medical_record_table)

        return error_msg

    # Method to get all the patient details starting from input string.
    def db_get_all_patient(self, like_str):
        like_params = [(PATIENT_INFO_TABLE_NAME_COL_NAME, like_str),
                       (PATIENT_INFO_TABLE_CITY_COL_NAME, like_str),
                       (PATIENT_INFO_TABLE_OCCU_COL_NAME, like_str)]
        # Parameter containsOrStartWith set to True to indicates contains.
        return self._db_get_rows_like(self.patient_info_table, like_params, True)

    # Checks if patient exists in db with given name or not, returns the list of patient details
    # objects if patient exist
    def db_check_patient_exist_by_name(self, patient_name):
        like_params = [(PATIENT_INFO_TABLE_NAME_COL_NAME, patient_name)]
        # Parameter containsOrStartWith set to False to indicate start with.
        status, df = self._db_get_rows_like(self.patient_info_table, like_params, False)

        if not status:
            return False, None
        # list of patient details which already exists with same name.
        patient_details_str = ""

        # In case there is no patient exists then return True and none for the patient results
        # if len(rows) == 0 or rows is None:
        if df.empty:
            return True, patient_details_str

        return True, get_patient_row_as_str(df.values.tolist())

    def get_all_medical_records(self, patient_id):
        where_params = [(MEDICAL_RECORD_TABLE_ID_COL_NAME, patient_id)]

        status, rows = self._db_get_rows(self.medical_record_table, where_params)
        error_msg = ""
        if not status:
            error_msg = ERROR_GETTING_MEDICAL_RECORDS

        print ("get_all_medical_records records ", rows)
        return error_msg, rows

    def db_save_patient_medical_record(self, values):
        # First check if given medical record already exists or not
        where_params = [(MEDICAL_RECORD_TABLE_ID_COL_NAME, values[MEDICAL_RECORD_TABLE_ID_INDEX]),
                        (MEDICAL_RECORD_TABLE_RECORD_DATE_COL_NAME, values[MEDICAL_RECORD_TABLE_RECORD_DATE_INDEX])]

        status, rows = self._db_get_rows(self.medical_record_table, where_params)

        # If the patient record for given date already exist we will update this record otherwise insert
        # a new one.
        error_msg = ""
        if status and 0 != len(rows):
            status = self._db_update(self.medical_record_table, MEDICAL_COL_NAME_LIST, values, where_params)

            if not status:
                error_msg = ERROR_UPDATING_MEDICAL_RECORD_TABLE
        else:
            # Insert the data received in the Data base.
            status = self._db_insert(self.medical_record_table, MEDICAL_RECORD_INFO_COL,
                                     values)

            if not status:
                error_msg = ERROR_INSERTING_MEDICAL_RECORD_TABLE

        return error_msg

    # Function to insert values in the doctor info table for doctor's registration.
    def db_register_patient_info(self, name_entry, gender_entry,
                                 age_entry, contact_no_entry,
                                 address_entry, city_entry,
                                 martial_s_entry, occupation_entry,
                                 dob_entry):

        error_msg = ""
        # TODO: Convert date into appropriate format, it should be in the format YYYY-MM-DD
        # dob_entry = "STR_TO_DATE('" + dob_entry + "', '%d-%m-%y')"
        # Form the query and run insert for given table.
        if 0 == len(dob_entry):
            dob_entry = '0000-0-0'

        if 0 == len(age_entry):
            age_entry = 0

        values = [name_entry, gender_entry, age_entry, contact_no_entry,
                  address_entry, city_entry, martial_s_entry, occupation_entry,
                  dob_entry]

        # Insert the data received in the Data base.
        status = self._db_insert(self.patient_info_table, PATIENT_INFO_COL,
                                 values)

        if not status:
            error_msg = ERROR_INSERTING_PATIENT_TABLE
        else:
            status, rows = self._db_get_last_inserted_row(self.patient_info_table, PATIENT_INFO_TABLE_ID_COL_NAME)

            if status and 0 != len(rows):
                print("registered row ",  rows[0])
                GlobalAppData.set_curr_selected_patient(rows[0])
            else:
                where_params = [(PATIENT_INFO_TABLE_NAME_COL_NAME, name_entry),
                                (PATIENT_INFO_TABLE_GENDER_COL_NAME, gender_entry),
                                (PATIENT_INFO_TABLE_AGE_COL_NAME, age_entry),
                                (PATIENT_INFO_TABLE_CONTACT_NO_COL_NAME, contact_no_entry),
                                (PATIENT_INFO_TABLE_ADDRESS_COL_NAME, address_entry),
                                (PATIENT_INFO_TABLE_CITY_COL_NAME, city_entry),
                                (PATIENT_INFO_TABLE_MARTIAL_S_COL_NAME, martial_s_entry),
                                (PATIENT_INFO_TABLE_OCCU_COL_NAME, occupation_entry),
                                (PATIENT_INFO_TABLE_DOB_COL_NAME, dob_entry)]
                status, rows = self._db_get_rows(self.patient_info_table, where_params)

                if not status or 0 == len(rows):
                    error_msg = ERROR_GETTING_PATIENT_INFO_FROM_TABLE
                else:
                    print("registered row where ", rows[0])
                    GlobalAppData.set_curr_selected_patient(rows[0])

        return error_msg

    # This function updates the patient info and also saves the new results in global data if successful.
    def db_update_patient_info(self, name_entry, gender_entry,
                               age_entry, contact_no_entry,
                               address_entry, city_entry,
                               martial_s_entry, occupation_entry,
                               dob_entry, patient_id):

        values = [patient_id, name_entry, gender_entry, age_entry, contact_no_entry,
                  address_entry, city_entry, martial_s_entry, occupation_entry,
                  dob_entry]

        patient_info_col = [PATIENT_INFO_TABLE_ID_COL_NAME,
                            PATIENT_INFO_TABLE_NAME_COL_NAME,
                            PATIENT_INFO_TABLE_GENDER_COL_NAME,
                            PATIENT_INFO_TABLE_AGE_COL_NAME,
                            PATIENT_INFO_TABLE_CONTACT_NO_COL_NAME,
                            PATIENT_INFO_TABLE_ADDRESS_COL_NAME,
                            PATIENT_INFO_TABLE_CITY_COL_NAME,
                            PATIENT_INFO_TABLE_MARTIAL_S_COL_NAME,
                            PATIENT_INFO_TABLE_OCCU_COL_NAME,
                            PATIENT_INFO_TABLE_DOB_COL_NAME]
        status = self._db_update(self.patient_info_table, patient_info_col, values,
                                 [(PATIENT_INFO_TABLE_ID_COL_NAME, patient_id)])

        error_msg = ""

        if not status:
            error_msg = ERROR_UPDATING_PATIENT_TABLE
        else:
            where_params = [(PATIENT_INFO_TABLE_ID_COL_NAME, patient_id)]
            status, rows = self._db_get_rows(self.patient_info_table, where_params)

            if not status or 0 == len(rows):
                error_msg = ERROR_GETTING_PATIENT_INFO_FROM_TABLE
            else:
                # we don't expect more than one rows returned here, safe to pick the first one.
                print(rows[0])
                GlobalAppData.set_curr_selected_patient(rows[0])

        return error_msg

    # Getter interface functions
    def db_get_doctor_name(self):
        # This function should be called once doctor info is retrieved by the App return error message in
        # case doctor info not present.
        error_msg = ""
        if None == self.doctor_info:
            error_msg = ERROR_DOCTOR_INFO_NOT_PRESENT

        return error_msg, self.doctor_info[DOCTOR_INFO_NAME_INDEX]

    # Initialize the class data members.
    def __init__(self):

        self.doctor_info = None
        self.patient_info_table = None
        self.medical_record_table = None

        # List containing any error message encountered during init
        self.error = []
        try:
            self.db_connector = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_USER_PASSWORD
            )

            self.db_cursor = self.db_connector.cursor()
            self.db_cursor.execute("SHOW DATABASES")

            print("DbController:Init: checking databases in DB host...")
            for db in self.db_cursor:
                # Check the substring and look for docspace DB
                # set error in case docspace DB is not found
                print(db)

        except Exception as e:
            print("DbController: Init Exception received while connecting to Database \n", e)
            self.error.append(DB_CONNECTION_ERROR)
