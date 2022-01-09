import tkinter as tk
from frames.base_frame import BaseFrame
from constant import *
from global_app_data import GlobalAppData
from frames.custom_entry import CustomEntry

'''
                                                            log out
                    Welcome "Doctor Name"
                        Register New Patient
                        Search Patient
                        Doctor Information

'''

WELCOME_LABEL = "Welcome "
REGISTER_NEW_PATENT = "Register New Patient"
BACK_UP_DATA = "Backup Data"
SEARCH_PATIENT = "Search Patient by Name"
UPDATE_DOC_INFO = "Update Doctor Information"


# xFrame class is suppose to create a custom Base TK frame from the root object.
# This Frame has all the entry frame widgets (instead of directly parent having it)
class EntryFrame:

    # Function which should be called whenever we enter this frame
    def frame_reload(self, full_reload):

        try:
            # Load the Doctor Name for Global app data.
            doctor_name = WELCOME_LABEL + GlobalAppData.get_logged_in_doc_info()[0]
            self.doctor_name_label.config(text=doctor_name)
            self.patient_name_entry.delete(0, 'end')
        except Exception as e:
            print("EntryFrame::frame_reload:: Exception loading doctor info ", e)

    # Enter the first back frame which is the login frame on log out don't do full reload, as we
    # want user name password to remain filled.
    def log_out_event_action(self):
        self.frame.enter_back_frame(1, False)

    # Init the frame class.
    def __init__(self, root, ws, hs):

        # Create a base frame object which has parent as main root window.
        self.frame = BaseFrame(root)

        header_frame = tk.Frame(self.frame)

        tk.Label(header_frame, text=DOC_SPACE, font=WIDGET_FONT_1).grid(
                 row=0, column=0)
        tk.Button(header_frame, text=LOG_OUT,
                  command=lambda: self.log_out_event_action(), font=WIDGET_FONT_1).grid(
                  row=0, column=1, padx=(ws-280, 0))
        header_frame.grid(row=0, column=0, sticky='w', pady=(hs/10.4, 0))

        field_frame = tk.Frame(self.frame)

        row_idx = 0
        self.doctor_name_label = tk.Label(field_frame, text=WELCOME_LABEL, font=HEADING_FONT)
        self.doctor_name_label.grid(row=row_idx, column=0, columnspan='9', pady=(0, 50))
        row_idx += 1

        # Row 2
        self.patient_name_entry = CustomEntry(field_frame, ENTRY_MAX_LEN_20, alpha=True, digit=False,
                                              special_char=False, space_allowed=True, width=30, font=WIDGET_FONT)
        self.patient_name_entry.grid(row=row_idx, column=1, pady=(0, 10))
        row_idx += 1

        # Row 3
        tk.Button(field_frame, text=SEARCH_PATIENT,
                  command=lambda: self.frame.enter_next_frame(1, True), font=WIDGET_FONT).grid(
                  row=row_idx, column=1, pady=(0, 30))
        row_idx += 1

        # Row 4
        tk.Button(field_frame, text=REGISTER_NEW_PATENT,
                  command=lambda: self.frame.enter_back_frame(1, True), font=WIDGET_FONT).grid(
                  row=row_idx, column=1, pady=(0, 30))
        row_idx += 1

        tk.Button(field_frame, text=UPDATE_DOC_INFO,
                  command=lambda: self.frame.enter_back_frame(1, True), font=WIDGET_FONT).grid(
                  row=row_idx, column=1, pady=(0, 30))
        row_idx += 1

        tk.Button(field_frame, text=BACK_UP_DATA,
                  command=lambda: self.frame.enter_back_frame(1, True), font=WIDGET_FONT).grid(
                  row=row_idx, column=1, pady=(0, 30))

        field_frame.grid(row='1', column='0', pady=(50, 0))