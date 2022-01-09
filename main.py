import sys
import tkinter as tk
from tkinter import messagebox
from frame_controller import FrameController
from db_controller import DbController
from constant import *

DOC_SPACE_APP_TITLE = "DocSpace Application"


def close_log_file():
    log_file.close()
    sys.stdout = old_stdout


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to Quit ?"):
        close_log_file()
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

        # Create root window and set the protocol for closing
        root = tk.Tk()
        root.title(DOC_SPACE_APP_TITLE)

        # Set the window closing protocol and provide function to execute when window is tried to closed.
        root.protocol("WM_DELETE_WINDOW", on_closing)

        # Create object of the frame controller.
        frame_controller = FrameController(root, db_controller)
        frame_controller.start_app_frame()

