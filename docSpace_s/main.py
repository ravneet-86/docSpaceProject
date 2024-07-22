import sys
import tkinter as tk
from tkinter import messagebox
from frame_controller import FrameController
from db_controller import DbController
from constant import *
from txHandlers.csv_fileHandler import CsvHandler
from txHandlers.remedy_searcher import RemedySearcher

import os

DOC_SPACE_APP_TITLE = "DocSpace Application"


def close_log_file():
    log_file.close()
    sys.stdout = old_stdout


def on_closing(db_controller, remedy_dba_controller):
    if messagebox.askokcancel("Quit", "Do you want to Quit ?"):
        close_log_file()
        CsvHandler.close_csv_file_handlers()
        root.destroy()


if __name__ == '__main__':

    # Create Log file and map stdout to the log file so that all print goes into the log file.
    print("DocSpaceApp:: Loading please wait...")

    # Create Object of the DB Controller for the Application used by Doctor, Patient frames
    db_controller = DbController(APP_DB_NAME)

    # Create Object of the DB Controller for the Remedy used by the Remedy searcher frame
    remedy_db_controller = DbController(REMEDY_DB_NAME)

    # display the error message and return in case db is not successfully connected.
    error_msg = db_controller.is_db_connected()
    if 0 != len(error_msg):
        messagebox.showerror(ERROR_BOX_TITLE, error_msg)
        close_log_file()
    else:
        print("Main: DataBase Controller created successfully")

        # Before starting the App GUI create a Demon thread to transmit the csv file
        # when data is added in the Database/csv files.
        csv_tx_thread = CsvHandler()
        csv_tx_thread.setDaemon(True)
        csv_tx_thread.start()

        # Create instance of remedy searcher
        remedy_searcher = RemedySearcher(remedy_db_controller)

        # Create root window and set the protocol for closing
        root = tk.Tk()
        root.title(DOC_SPACE_APP_TITLE)

        # Add a menu bar at the top
        menu_bar = tk.Menu(root, font=WIDGET_FONT_1)
        developer_info = tk.Menu(menu_bar, tearoff=0, font=WIDGET_FONT_1)
        developer_info.add_command(label=DEVELOPER_INFO_EMAIL)
        developer_info.add_command(label=DEVELOPER_INFO_MOBILE)
        developer_info.add_separator()
        menu_bar.add_cascade(label="Developer Info", menu=developer_info, font=WIDGET_FONT_1)

        version_info = tk.Menu(menu_bar, tearoff=0, font=WIDGET_FONT_1)
        version_info.add_command(label=APP_RELEASE_VERSION)
        version_info.add_separator()
        menu_bar.add_cascade(label="Version", menu=version_info, font=WIDGET_FONT_1)
        root.config(menu=menu_bar)

        # Set the window closing protocol and provide function to execute when window is tried to closed.
        root.protocol("WM_DELETE_WINDOW", lambda: on_closing(db_controller, remedy_db_controller))

        # Create object of the frame controller.
        frame_controller = FrameController(root, db_controller, remedy_db_controller,
                                           remedy_searcher)
        '''
        try:
            os.remove("./" + "docSpaceApp.log")
        except Exception as e:
            print("DocSpaceApp::Main unable to clean previous log file. exception ", e)
        '''
        old_stdout = sys.stdout
        log_file = open("docSpaceApp.log", "w")
        #sys.stdout = log_file

        frame_controller.start_app_frame()

