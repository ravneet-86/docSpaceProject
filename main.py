import sys
import tkinter as tk
from tkinter import messagebox
from frame_controller import FrameController
from db_controller import DbController
from constant import *
from txHandlers.csv_fileHandler import CsvHandler

DOC_SPACE_APP_TITLE = "DocSpace Application"


def close_log_file():
    log_file.close()
    sys.stdout = old_stdout


def on_closing(db_controller):
    if messagebox.askokcancel("Quit", "Do you want to Quit ?"):
        close_log_file()
        CsvHandler.close_csv_file_handlers()
        root.destroy()


if __name__ == '__main__':

    # Create Log file and map stdout to the log file so that all print goes into the log file.
    old_stdout = sys.stdout
    log_file = open("docSpaceApp.log", "w")
    #sys.stdout = log_file

    # Create Object of the DB Controller
    db_controller = DbController()

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
        root.protocol("WM_DELETE_WINDOW", lambda: on_closing(db_controller))

        # Create object of the frame controller.
        frame_controller = FrameController(root, db_controller)
        frame_controller.start_app_frame()

