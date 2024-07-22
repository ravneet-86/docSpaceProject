import os.path
import tkinter as tk
from tkinter import ttk

import utils
from frames.base_frame import BaseFrame
from constant import *
from frames.custom_entry import CustomEntry
from frames.custom_text import CustomText
from global_app_data import *
from txHandlers.gdrive import Gdrive
from tkinter import messagebox
from datetime import datetime
from db_controller import DbController
from threading import Thread, Event
import glob

BACK_UP_DATA = "Back Up Data to Gdrive"
GENERATE_BACK_UP_FILES = "Generate Backup files"
UPLOAD_BACK_UP_FILES = "Upload Backup files"
ACCESS_TOKEN = "Enter Access Token\nhttps://developers.google.com/oauthplayground"
PARENT_FOLDER = "Parent Folder"
BACK_UP_FILES = "Backup files"
PRE_DUMP_STR = "DB_dump_"
NO_DUMP_FILE_PRESENT = "No Dump file found"
ERROR_GENERATING_DATABASE_DUMP = "Error in Generating Database Dump"
PROGRESS_BAR_GENERATING = "Generating Dump Files..."
UPLOADING_G_DRIVE = "Uploading Dump Files to gDrive..."
NO_DB_DUMP_FILE_GENERATED = "No DataBase Dump file present,\n" \
                            "Please Generate Database Dump before uploading..."
NO_ACCESS_TOKEN_PRESENT = "Please enter a valid Access Token for uploading..."

'''
Tkinter is not inheritently thread safe, it is good idea to run tkinter only in the main
thread while perform other non GUI related tasks in non main thread.
class ProgressBarThread(Thread):
    def __init__(self, name, root, event):
        Thread.__init__(self)
        self.name = name
        self.root = root
        self.event = event
        self.progress_frame = None

    def open_progress_bar(self):
        print("adding progress bar")
        #self.progress_frame = tk.Toplevel(self.root)
        print("adding prgoress bar 1")
        #self.progress_frame.title(self.name)
        print ("adding progres bar 2")
        #p_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", mode="indeterminate")
        print ("adding progress bar 3")
        #p_bar.grid(column=0, row=0)
        print ("adding progress bar 4")
        #p_bar.start(10)
        print ("adding progress bar 5")
        #tk.Label(self.progress_frame, text=self.name).grid(column=0, row=1)
        print("progress pare init done", p_bar_flag)
        while p_bar_flag != True:
            #self.progress_frame.update_idletasks()
            #self.progress_frame.grab_set()
            print("running event loop")
            continue

    def run(self):
        self.open_progress_bar()

    def close_progress_bar(self):
        print("destroying...")
        self.progress_frame.destroy()
'''


# xFrame class is suppose to create a custom Base TK frame from the root object.
# This Frame has all the login frame widgets (instead of directly parent having it)
class BackUpFrame:

    # Function which should be called whenever we enter this frame
    def frame_reload(self, full_reload):
        try:
            # Load the Doctor Name for Global app data.
            error_msg, doctor_name = self.db_controller.db_get_doctor_name()

            doctor_name = DOCTOR_NAME + doctor_name
            if 0 != len(error_msg):
                messagebox.showerror(ERROR_BOX_TITLE, error_msg)
            else:
                self.doctor_name_label.config(text=doctor_name)
        except Exception as e:
            print("BackUpFrame::frame_reload:: Exception loading doctor info ", e)

        # Check if any Dump files already exists if so sort it in order of modification timestamp.
        files = sorted(glob.glob("*" + PRE_DUMP_STR + "*"), reverse=True, key=os.path.getmtime)

        if None != files and len(files) != 0:
            self.files_label[0].config(text=files[0])
        # If there are more than one files clean up and maintain only one file with latest
        # modification timestamp.
        for f_idx in range(1, len(files)):
            os.remove("./"+files[f_idx])

        self.event = Event()

    # Enter the first back frame which is the login frame on log out don't do full reload, as we
    # want username password to remain filled.
    def log_out_event_action(self):
        self.frame.enter_back_frame(1, False)

    # Enter the first back frame which is the entry frame on log out don't do full reload, as we
    # want search result to show in this frame.
    def go_back_event_action(self):
        self.frame.enter_back_frame(2, False)

    def open_progress_bar(self, name):
        # Create a top level window over the current application root window.
        self.progress_frame = tk.Toplevel(self.root)

        # Place the progress bar at the place where back files button is present.
        x, y = self.gen_back_files_button.winfo_rootx(), self.gen_back_files_button.winfo_rooty()

        self.progress_frame.geometry('%dx%d+%d+%d' % (500, 100, x, y))

        self.progress_frame.title(name)
        self.p_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", mode="determinate")
        #self.p_bar.grid(column=0,row=0)
        self.p_bar.pack(fill=tk.BOTH, expand=1)
        self.progress_frame.update_idletasks()
        self.p_bar.update_idletasks()
        #self.p_bar.start(80)
        self.p_bar['value'] = 10
        #tk.Label(self.progress_frame, text=name).grid(column=0, row=1)
        tk.Label(self.progress_frame, text=name).pack(fill=tk.BOTH, expand=1)
        self.progress_frame.grab_set()

    def close_progress_bar(self):
        self.progress_frame.destroy()

    def run_progress_bar(self):
        bar_val = 10
        while not self.event.is_set():
            #self.progress_frame.tkraise()
            self.progress_frame.update_idletasks()
            #self.p_bar.update_idletasks()
            bar_val += 10
            self.p_bar['value'] = bar_val
            if bar_val == 100:
                bar_val = 0
            import time
            time.sleep(0.2)

        if bar_val != 100:
            self.p_bar['value'] = 100
            self.progress_frame.update_idletasks()
        time.sleep(0.1)

    def upload_back_files_event_action(self):
        files = sorted(glob.glob("*" + PRE_DUMP_STR + "*"), reverse=True, key=os.path.getmtime)

        if None != files and len(files) != 0:
            acc_token = self.label_entries[0].get().strip()
            if 0 == len(acc_token):
                messagebox.showerror(ERROR_BOX_TITLE, NO_ACCESS_TOKEN_PRESENT)
                return

            self.open_progress_bar(UPLOADING_G_DRIVE)
            self.event.clear()
            upload_thread = Thread(target=Gdrive.upload_file_to_drive,
                                   args=(acc_token,
                                         "./"+files[0],
                                         self.label_entries[1].get().strip(),
                                         files[0], self.event, ))
            upload_thread.start()

            self.run_progress_bar()
            self.close_progress_bar()

            messagebox.showinfo(MESSAGE_BOX_TITLE, GlobalAppData.get_g_drive_file_upload_result())

        else:
            messagebox.showinfo(MESSAGE_BOX_TITLE, ERROR_GENERATING_DATABASE_DUMP)

    def gen_back_up_files_event_action(self):
        self.open_progress_bar(PROGRESS_BAR_GENERATING)
        #self.progress_bar_thread.start()

        self.event.clear()
        db_dump_thread = Thread(target=DbController.create_database_dump,
                                args=(PRE_DUMP_STR + utils.get_time_stamp(), self.event, ))
        db_dump_thread.start()
        # status, dump_file_name = DbController.create_database_dump(PRE_DUMP_STR + utils.get_time_stamp())
        self.run_progress_bar()
        self.close_progress_bar()

        status = GlobalAppData.get_gen_back_up_files_status()

        # Currently, we dump everything in one file so just update the first label to reflect the file name
        if not status:
            messagebox.showerror(ERROR_BOX_TITLE, ERROR_GENERATING_DATABASE_DUMP)
        else:
            self.files_label[0].config(text=GlobalAppData.get_gen_back_up_files_name())

    # Init the frame class.
    def __init__(self, root, ws, hs, db_controller):

        # Create a base frame object which has parent as main root window.
        self.frame = BaseFrame(root)
        self.db_controller = db_controller
        self.root = root
        self.event = Event()

        header_frame = tk.Frame(self.frame)
        tk.Label(header_frame, text=DOC_SPACE, font=WIDGET_FONT_1).grid(row=0, column=0)
        tk.Button(header_frame, text=LOG_OUT,
                  command=lambda: self.log_out_event_action(), font=WIDGET_FONT_1).grid(
            row=0, column=1, padx=(ws - 280, 0))
        header_frame.grid(row=0, column=0, pady=(10, 0), sticky='w')

        header_frame_1 = tk.Frame(self.frame)
        self.doctor_name_label = tk.Label(header_frame_1, text=DOCTOR_NAME, font=HEADING_FONT, width=30)
        self.doctor_name_label.grid(row=1, column=0, sticky='w')
        tk.Label(header_frame_1, text=BACK_UP_DATA, font=HEADING_FONT).grid(row=1, column=6, padx=(100, 0))
        tk.Button(header_frame_1, text=GO_BACK,
                  command=lambda: self.go_back_event_action(), font=WIDGET_FONT_1).grid(
            row=1, column=7, padx=(330, 0))
        header_frame_1.grid(row=1, column=0, sticky='w')

        details_frame = tk.Frame(self.frame)
        self.gen_back_files_button = tk.Button(details_frame, text=GENERATE_BACK_UP_FILES,
                                               command=lambda: self.gen_back_up_files_event_action(),
                                               font=WIDGET_FONT)
        self.gen_back_files_button.grid(row=0, column=0)
        files_label_frame = tk.LabelFrame(details_frame, text=BACK_UP_FILES, font=WIDGET_FONT)

        self.files_label = []
        for l_idx in range(1):
            self.files_label.append(tk.Label(files_label_frame, text=NO_DUMP_FILE_PRESENT, font=WIDGET_FONT))
            self.files_label[l_idx].grid(row=l_idx + 1, column=0, padx=(20, 10), pady=(10, 10))

        files_label_frame.grid(row=0, column=1, padx=(30, 0))

        label_names = [ACCESS_TOKEN, PARENT_FOLDER]
        c_idx = 0
        r_idx = 1
        self.label_entries = []
        for label_name in label_names:
            tk.Label(details_frame, text=label_name, font=WIDGET_FONT).grid(row=r_idx,
                                                                            column=0, pady=(10, 0))
            self.label_entries.append(tk.Entry(details_frame, width=20, font=WIDGET_FONT))
            self.label_entries[r_idx-1].grid(row=r_idx, column=1, padx=(30, 0), pady=(20, 0))
            r_idx = r_idx + 1

        tk.Button(details_frame, text=UPLOAD_BACK_UP_FILES,
                  command=lambda: self.upload_back_files_event_action(), font=WIDGET_FONT).grid(
            row=r_idx, column=0, pady=(40, 0), sticky='e')

        details_frame.grid(row=r_idx, column=0, sticky='ew', pady=(80, 0), padx=(300, 0))
