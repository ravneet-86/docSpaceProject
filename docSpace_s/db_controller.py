import mysql.connector
import os
import pipes
from constant import *
from utils import *
from patient_details import PatientDetails
import pandas as pd
from global_app_data import *
from datetime import datetime
from txHandlers.csv_fileHandler import CsvHandler

ENABLE_DB_DEBUG = True


# Class to perform DataBase connection and perform database operations.
class DbController:

    # Below are the core SQL Implementation functions use to query the Database using
    # mySql queries. These are not meant to be called outside of the DB Controller.

    def _db_delete_table(self, table):
        # Run insert for given table.
        try:
            sql = "drop table " + self.db_name + "." + table

            if ENABLE_DB_DEBUG:
                print("dbController:db_delete_table Deleting table with query ", sql)
            self.db_cursor.execute(sql)
            self.db_connector.commit()
            return True
        except Exception as e:
            print("DbController:_db_create_table: Failed to run create table query DB: ", self.db_name)
            print("Sql statement ", sql, "exception: ", e)
            return False

    def _db_create_table(self, table):
        # Run insert for given table.
        try:
            sql = "create table " + self.db_name + "." + table

            if ENABLE_DB_DEBUG:
                print("dbController:db_create_table Creating table with query ", sql)
            self.db_cursor.execute(sql)
            self.db_connector.commit()
            return True
        except Exception as e:
            print("DbController:_db_create_table: Failed to run create table query DB: ", self.db_name)
            print("Sql statement ", sql, "exception: ", e)
            return False

    def _db_insert(self, table, column_string, values):
        # Run insert for given table.
        try:
            sql = "Insert into " + self.db_name + "." + table + " " + column_string + " values "

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
            print("DbController:db_insert: Failed to insert query table", self.db_name + "." + table,
                  " values ", values, " Size ",
                  len(values))
            print("Sql statement ", sql, "exception: ", e)
            return False

    def _db_update(self, table, column_name_list, values, where_params):
        # Example update anand_patient_info set name = "sarv" where patient_id = 1 and date = 1990-12-2;
        value_idx = 0
        sql = "update " + self.db_name + "." + table + " set "
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
            print("DbController:db_update: Failed to update query table", self.db_name + "." + table,
                  " values ", values, " Size ",
                  len(values))
            print("Sql statement ", sql, "exception: ", e)
            return False

    # Function to get the last inserted row in the given table
    # Note this will work only for table which has single auto increment primary key.
    def _db_get_last_inserted_row_m2(self, table, key_id):
        try:
            sql = "select * from " + self.db_name + "." + table + " where " + key_id + "=(select MAX(" + key_id +")" \
                  + " from " + self.db_name + "." + table + ");"

            if ENABLE_DB_DEBUG:
                print("_db_get_last_inserted_row_m2:_db_get_rows Running select query ", sql)
            self.db_cursor.execute(sql)
            rows = self.db_cursor.fetchall()
            return True, rows

        except Exception as e:
            print("DbController:_db_get_last_inserted_row: Failed to get rows for table ", self.db_name + "." + table)
            print("Sql statement ", sql, "exception: ", e)
            return False, None

    # Function to get the last inserted row in the given table
    # Note this will work only for table which has single auto increment primary key.
    def _db_get_last_inserted_row(self, table, key_id):
        try:
            sql = "select * from " + self.db_name + "." + table + " where " + key_id + " = ( select last_insert_id() );"

            if ENABLE_DB_DEBUG:
                print("_db_get_last_inserted_row:_db_get_rows Running select query ", sql)
            self.db_cursor.execute(sql)
            rows = self.db_cursor.fetchall()
            return True, rows

        except Exception as e:
            print("DbController:_db_get_last_inserted_row: Failed to get rows for table ", self.db_name + "." + table)
            print("Sql statement ", sql, "exception: ", e)
            return False, None

    # Function to get the rows of a given table
    def _db_get_rows(self, table):
        try:
            sql = "select * from " + self.db_name + "." + table

            if ENABLE_DB_DEBUG:
                print("dbController:_db_get_rows Running select query ", sql)
            self.db_cursor.execute(sql)
            rows = self.db_cursor.fetchall()
            return True, rows
        except Exception as e:
            print("DbController:db_insert: Failed to get rows for table ", self.db_name + "." + table)
            print("Sql statement ", sql, "exception: ", e)
            return False, None

    # Function to get the rows of a given table under the select where query using where_params
    def _db_get_rows(self, table, where_params):
        index = 0
        for param in where_params:
            # Form the select where query if its the first parameter
            if 0 == index:
                sql = "select * from " + self.db_name + "." + table + " where " + \
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
            print("DbController:db_get_rows where: Failed to get rows for table ", self.db_name + "." + table)
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
                    sql = "select * from " + self.db_name + "." + table + " where " + \
                          param[0] + " like ('%" + param[1] + "%')"
                else:  # False indicates we should get the rows which start with the parameter string
                    sql = "select * from " + self.db_name + "." + table + " where " + \
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
            print("DbController:db_get_rows_like where: Failed to get rows for table ", self.db_name + "." + table)
            print("Sql statement ", sql, " where params ", like_params, "exception: ", e)
            return False, None

    def get_col_names(self, table_name):
        try:
            sql = "describe " + table_name + ";"
            self.db_cursor.execute(sql)
            rows = self.db_cursor.fetchall()
            # This will return full description as list, we need to get the col name from this
            # which is the first entry.

            col = []
            for row in rows:
                col.append(row[0])

            return col
        except Exception as e:
            print("db_controller:_get_col_names: Exception in getting column details table_name ",
                    table_name, "Exception: ", e)

    def get_db_tables(self):
        try:
            self.db_cursor.execute("show tables")
            sources = []
            rows = self.db_cursor.fetchall()

            for row in rows:
                row = row[0].replace(',', '')
                sources.append(row)

            print ("Total remedy sources ", sources)
            return sources
        except Exception as e:
            print("db_controller: get_db_tables: exception: ", e)
            return None

    def _db_get_csv_file_name(self, table_name):
        # Get the last record added in the csv file table. At this point we expect atleast
        # one record to be present. As a record is added if we are successfully create the table.
        status, rows = self._db_get_last_inserted_row_m2(table_name, FILE_INFO_TABLE_INSERT_ID_COL_NAME)
        print(rows)
        if status is True and len(rows) != 0:
            return rows[0][FILE_INFO_TABLE_FILE_NAME_COL_INDEX]
        else:
            print("dbController::_db_get_csv_file_name Cannot get csv file from the DB ", table_name)
            return None

    def _db_update_csv_file(self, table_identifier, values):

        try:
            csv_file = None
            is_csv_file_update_required = False

            if table_identifier == MEDICAL_RECORD_TYPE_STRING:
                if CsvHandler.is_new_csv_file_needed(self.medical_record_csv_file, table_identifier):
                    csv_file = self.create_csv_file_info_table_and_file(self.medical_record_table, False)

                if csv_file is None:
                    csv_file = self.medical_record_csv_file
                else:
                    self.medical_record_csv_file = csv_file
                    is_csv_file_update_required = True
            elif table_identifier == PATIENT_INFO_TYPE_STRING:
                if CsvHandler.is_new_csv_file_needed(self.patient_info_csv_file, table_identifier):
                    csv_file = self.create_csv_file_info_table_and_file(self.patient_info_table, False)

                if csv_file is None:
                    csv_file = self.patient_info_csv_file
                else:
                    self.patient_info_csv_file = csv_file
                    is_csv_file_update_required = True
            else:
                # This is the case of DOCTOR INFO.
                if CsvHandler.is_new_csv_file_needed(self.doctor_info_csv_file, table_identifier):
                    csv_file = self.create_csv_file_info_table_and_file(self.doctor_info_table, False)

                if csv_file is None:
                    csv_file = self.doctor_info_csv_file
                else:
                    self.doctor_info_csv_file = csv_file
                    is_csv_file_update_required = True

            if csv_file is not None:
                CsvHandler.save_record_to_csv_file(csv_file, table_identifier, values,
                                                   is_csv_file_update_required)
        except Exception as e:
            print("Exception::_db_update_csv_file in updating csv ", table_identifier, " values ", values,
                  " exception ", e)

    def create_csv_file_info_table_and_file(self, base_table_name, create_table_needed):
        # We don't check the return status because even if this fails we still go ahead
        # as we have already registered the user.
        csv_file_name = ""
        values = []
        try:
            file_info_table_name = get_csv_file_info_table_name(base_table_name)

            status = True
            if create_table_needed:
                table_sql = file_info_table_name + CREATE_TABLE_CSV_FILE_INFO_STRING
                status = self._db_create_table(table_sql)

            if status:
                # Now create CSV files and add that into the File info table
                csv_file_name = create_csv_file_name(file_info_table_name)
                values = [csv_file_name, datetime.now().strftime("%Y-%m-%d"), False]
                self._db_insert(file_info_table_name, FILE_INFO_TABLE_COL_STRING_FIRST_THREE, values)
                return csv_file_name
        except Exception as e:
            print("db_controller::create_csv_file_info_table_and_file failed to create CSV file table ",
                  e, " base table ", base_table_name, " sql table ", table_sql,
                  " csv file name ", csv_file_name, " values ", values)
            return None

    # Below are the interface functions which are accessed by the Application frames
    # to Query or Get Data already Queried from DB. TODO: Move them to different file specific to Doctor
    # Patient DB Access.
    # Function to check if DB is connected successfully or not after object creation.
    def is_db_connected(self):
        if 0 != len(self.error):
            # Currently we can have only one error message. use index 0, If needed we should
            # append all the error messages
            error_msg = self.error[0]
            return error_msg
        else:
            return ""

    # Below functions are specific to doctor and patient tables in the DOC Space DB/Application.
    # TODO: Move them to a different file.
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

                    self.patient_info_csv_file = self._db_get_csv_file_name(
                                                 get_csv_file_info_table_name(self.patient_info_table))
                    self.medical_record_csv_file = self._db_get_csv_file_name(
                                                 get_csv_file_info_table_name(self.medical_record_table))
                    self.doctor_info_csv_file = self._db_get_csv_file_name(
                                                get_csv_file_info_table_name(DOCTOR_INFO_TABLE))

                    print("CSV File name ", self.patient_info_csv_file, " - ", self.medical_record_csv_file)

                    return error_msg

            # Email is present as non-zero rows are returned, but password didn't match.
            error_msg = ERROR_PASSWORD_NOT_MATCHING

        return error_msg

    # Below functions are specific to doctor and patient tables in the DOC Space DB/Application.
    # TODO: Move them to a different file.
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

    # Below functions are specific to doctor and patient tables in the DOC Space DB/Application.
    # TODO: Move them to a different file.
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
        else:
            # step 4: Now create the corresponding CSV File info tables.
            self.create_csv_file_info_table_and_file(patient_info_table, True)
            self.create_csv_file_info_table_and_file(medical_record_table, True)

            # DOCTOR INFO CSV table is already created by the Admin and also first csv file details are
            # already inserted. So just get the csv file name from the table.
            self.doctor_info_csv_file = self._db_get_csv_file_name(get_csv_file_info_table_name(DOCTOR_INFO_TABLE))

            # DB table is already created by the Administrator update an entry in this table
            self._db_update_csv_file(DOCTOR_INFO_TABLE, values)
        return error_msg

    # Below functions are to doctor and patient tables in the DOC Space DB/Application.
    # TODO: Move them to a different file.
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

    # Below functions are specific to doctor and patient tables in the DOC Space DB/Application.
    # TODO: Move them to a different file.
    def get_all_medical_records(self, patient_id):
        where_params = [(MEDICAL_RECORD_TABLE_ID_COL_NAME, patient_id)]

        status, rows = self._db_get_rows(self.medical_record_table, where_params)
        error_msg = ""
        if not status:
            error_msg = ERROR_GETTING_MEDICAL_RECORDS

        print("get_all_medical_records records ", rows)
        return error_msg, rows

    # Below functions are specific to doctor and patient tables in the DOC Space DB/Application.
    # TODO: Move them to a different file.
    def db_save_patient_medical_record(self, values):
        # Check if date is valid or not
        status, error_msg = validate_date_field(values[MEDICAL_RECORD_TABLE_NEXT_VISIT_INDEX])
        if not status:
            return error_msg

        # Check if given medical record already exists or not
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
                # Event if it is an existing record we add a new row in the csv file instead of updating the
                # current one.
                self._db_update_csv_file(MEDICAL_RECORD_TYPE_STRING, values)
        else:
            # Insert the data received in the Data base.
            status = self._db_insert(self.medical_record_table, MEDICAL_RECORD_INFO_COL,
                                     values)

            if not status:
                error_msg = ERROR_INSERTING_MEDICAL_RECORD_TABLE
            else:
                # Save the medical record in the corresponding csv file.
                self._db_update_csv_file(MEDICAL_RECORD_TYPE_STRING, values)
        return error_msg

    # Below functions are specific to doctor and patient tables in the DOC Space DB/Application.
    # TODO: Move them to a different file.
    # Function to insert values in the doctor info table for doctor's registration.
    def db_register_patient_info(self, name_entry, gender_entry,
                                 age_entry, contact_no_entry,
                                 address_entry, city_entry,
                                 martial_s_entry, occupation_entry,
                                 dob_entry):

        error_msg = ""
        # Validate date into appropriate format, it should be in the format YYYY-MM-DD
        # dob_entry = "STR_TO_DATE('" + dob_entry + "', '%d-%m-%y')"
        # Form the query and run insert for given table.
        if 0 == len(dob_entry):
            dob_entry = '0000-0-0'
        else:
            ret, error_msg = validate_date_field(dob_entry)
            if not ret:
                return error_msg

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
            status, rows = self._db_get_last_inserted_row(self.patient_info_table,
                                                          PATIENT_INFO_TABLE_ID_COL_NAME)

            if status and 0 != len(rows):
                print("registered row ", rows[0])
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

            # Save patient info in the csv file.
            self._db_update_csv_file(PATIENT_INFO_TYPE_STRING,  values)

        return error_msg

    # Below functions are specific to doctor and patient tables in the DOC Space DB/Application.
    # TODO: Move them to a different file.
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

            # Now add the patient info in the csv file, please note even for same patient we add a new record
            # instead of searching and updating a current one.
            self._db_update_csv_file(PATIENT_INFO_TYPE_STRING, values)

        return error_msg

    def create_database_dump(self, name, event):
        try:
            file_name = self.db_name + name + ".sql"
            dump_cmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + \
                       self.db_name + " > " + pipes.quote(DB_BACKUP_PATH) + "/" + file_name
            os.system(dump_cmd)
            import time
            time.sleep(0.3)
            GlobalAppData.set_gen_back_up_files_status(True)
            GlobalAppData.set_gen_back_up_files_name([file_name])
            event.set()
            #return True, file_name
        except Exception as e:
            print("DbController: Exception while dumping the Database name ", name, "exception ", e)
            GlobalAppData.set_gen_back_up_files_status(False)
            GlobalAppData.set_gen_back_up_files_name([None])
            #return False, None

    # Getter interface functions

    def db_get_patient_info_csv_file(self):
        return self.patient_info_csv_file

    def db_get_medical_record_info_csv_file(self):
        return self.medical_record_csv_file

    def db_get_doctor_info_csv_file(self):
        return self.doctor_info_csv_file

    def db_get_doctor_name(self):
        # This function should be called once doctor info is retrieved by the App return error message in
        # case doctor info not present.
        error_msg = ""
        if None == self.doctor_info:
            error_msg = ERROR_DOCTOR_INFO_NOT_PRESENT

        return error_msg, self.doctor_info[DOCTOR_INFO_NAME_INDEX]

    def db_remedy_results(self, table_name, like_str, cols):
        # Leave the first column which is the remedy name we want to search only
        # the descrition.
        like_params = []
        for col in cols:
            like_params.append((col, like_str))

        print ("db_remedy_search results")
        print (like_params)
        # Parameter containsOrStartWith set to True to indicates contains.
        return self._db_get_rows_like(table_name, like_params, True)

    # Initialize the class data members.
    def __init__(self, db_name):

        self.db_name = db_name
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
                # TODO: Check the substring and look for docspace and Remedy DB
                # set error in case docspace DB is not found
                print(db)

            # Set the cursor to use the given data base
            self.db_cursor.execute("use " + self.db_name + ";")

        except Exception as e:
            print("DbController: Init Exception received while connecting to Database \n", e)
            self.error.append(DB_CONNECTION_ERROR)

        # Below variables are specific to doctor and patient tables in the DOC Space DB/Application.
        # TODO: Move them to a different file.
        self.doctor_info = None
        self.patient_info_table = None
        self.medical_record_table = None
        self.patient_info_csv_file = None
        self.medical_record_csv_file = None
        self.doctor_info_csv_file = None


