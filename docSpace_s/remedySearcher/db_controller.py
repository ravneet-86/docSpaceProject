import mysql.connector
import os
import pipes

import pandas as pd
from datetime import datetime
import pymysql
from sqlalchemy import create_engine

DB_HOST = "localhost"
DB_USER = "root"
# DB_USER_PASSWORD = "homeoPathicDocSpace21"
DB_USER_PASSWORD = "dehradun86"
DB_BACKUP_PATH = "./"
DB_CONNECTION_ERROR = "FAILED TO CONNECT TO DB"

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
            print("DbController:_db_delete_table: Failed to run create table query DB: ", self.db_name)
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

    def update_df_to_db(self, df, table_name):
        '''
        df.to_sql(self.db_name + "." + table_name, self.db_connector,
                  if_exists='replace', index=False)
        '''

        df.to_sql(table_name, con=self.engine, if_exists='replace',
                  index=False, chunksize=1000)


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
                # Check the substring and look for docspace DB
                # set error in case docspace DB is not found
                print(db)

            self.engine = create_engine("mysql+pymysql://" +
                                                DB_USER + ":" +
                                                DB_USER_PASSWORD + "@" +
                                                DB_HOST + "/" +
                                                self.db_name)

        except Exception as e:
            print("DbController: Init Exception received while connecting to Database \n", e)
            self.error.append(DB_CONNECTION_ERROR)



