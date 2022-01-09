import mysql.connector
import os
import pipes
from constant import *

# DB information, TODO: if required move to a text file and read from there instead.
DB_HOST = "localhost"
DB_USER = "root"
# DB_USER_PASSWORD = "homeoPathicDocSpace21"
DB_USER_PASSWORD = "dehradun86"
DB_NAME = "DocSpace"
DB_BACKUP_PATH = "./"


# Class to perform DataBase connection and perform database operations.
class DbController:

    # Function to check if DB is connected succesfully or not after object creation.
    def is_db_connected(self):
        if 0 != len(self.error):
            # Currently we can have only one error message. use index 0, If needed we should
            # append all the error messages
            error_msg = self.error[0]
            return error_msg
        else:
            return ""

    # Function to insert values in the given table.
    def db_insert(self, sql, values, table):
        # Run insert for given table.
        try:
            self.db_cursor.executemany(sql, values)
            self.db_connector.commit()
            return True
        except Exception as e:
            print("DbController:db_insert: Failed to insert query table", DB_NAME + "." + table,
                  " values ", values, " Size ",
                  len(values))
            print("Sql statement ", sql, "exception: ", e)
            return False

    # Function to insert values in the doctor info table for doctor's registration.
    def db_insert_doctor_info(self, values):
        # Form the query and run insert for given table.
        sql = "Insert into " + DB_NAME + "." + DOC_REGISTRATION_TABLE + " " + DOCTOR_INFO_COL + " values " + \
              "(%s, %s, %s, %s, %s, %s, %s)"
        return self.db_insert(sql, values, DOC_REGISTRATION_TABLE)

    # Function to get the rows of a given table
    def db_get_rows(self, table):
        try:
            sql = "select * from " + DB_NAME + "." + table
            self.db_cursor.execute(sql)
            rows = self.db_cursor.fetchall()
            return True, rows
        except Exception as e:
            print("DbController:db_insert: Failed to get rows for table ", DB_NAME + "." + table)
            print("Sql statement ", sql, "exception: ", e)
            return False, None

    # Function to check email column and see if email_address already exists or not.
    # Returns two booleans bool, bool signifying if return status (false if failure, true otherwise),
    # email exists or not (true if exists, false otherwise)
    def check_email_exists(self, email_address):
        ret = self.db_get_rows(DOC_REGISTRATION_TABLE)

        if not ret[0]:
            return False, False, None

        # Iterate over all the rows.
        for row in ret[1]:
            # email is the first column in the doctor_info table.
            # password is the second column in the doctor_info table, return the password as well.
            if row[1] == email_address:
                return True, True, row

        return True, False, None

    # Initialize the class data members.
    def __init__(self):

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
