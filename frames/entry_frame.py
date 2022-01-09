import tkinter as tk
from frames.base_frame import BaseFrame
from constant import *
from frames.custom_entry import CustomEntry
from tkinter import messagebox
from utils import *
from global_app_data import *

'''
                                                            log out
                    Welcome "Doctor Name"
                        Register New Patient
                        Search Patient
                        Doctor Information

'''

WELCOME_LABEL = "Welcome Doctor: "
REGISTER_NEW_PATENT = "Register New Patient"
BACK_UP_DATA = "Backup Data"
SEARCH_PATIENT_LABEL = "Search For Patient Above"
UPDATE_DOC_INFO = "Update Doctor Information"


# xFrame class is suppose to create a custom Base TK frame from the root object.
# This Frame has all the entry frame widgets (instead of directly parent having it)
class EntryFrame:

    # Function which should be called whenever we enter this frame
    def frame_reload(self, full_reload):

        try:
            # Load the Doctor Name for Global app data.
            error_msg, doctor_name = self.db_controller.db_get_doctor_name()

            doctor_name = WELCOME_LABEL + doctor_name
            if 0 != len(error_msg):
                messagebox.showerror(ERROR_BOX_TITLE, error_msg)
            else:
                self.doctor_name_label.config(text=doctor_name)
                if full_reload:
                    self.patient_name_entry.delete(0, 'end')
        except Exception as e:
            print("EntryFrame::frame_reload:: Exception loading doctor info ", e)

    # Enter the first back frame which is the login frame on log out don't do full reload, as we
    # want user name password to remain filled.
    def log_out_event_action(self):
        self.frame.enter_back_frame(1, False)

    # Enter register patient frame this is at index 2.
    def register_patient_event_action(self):
        self.frame.enter_next_frame(2, False)

    def search_patient_event_action(self):
        self.frame.enter_next_frame(1, True)

    def get_search_results(self, search_str):
        return self.patient_result_df[(self.patient_result_df.name.str.contains(search_str, regex=True, na=False,
                                                                                flags=re.IGNORECASE)) |
                                      (self.patient_result_df.city.str.contains(search_str, regex=True, na=False,
                                                                                flags=re.IGNORECASE)) |
                                      (self.patient_result_df.occupation.str.contains(search_str, regex=True, na=False,
                                                                                      flags=re.IGNORECASE))].values.tolist()

    def list_box_double_click_event_action(self, event):
        # Curr selection is a tuple with first index refers to the index in the list box search display list.
        cur_selection = self.search_result_list_box.curselection()
        if 0 != len(self.curr_search_results_display):
            print(self.curr_search_results_display[cur_selection[0]])

            # Save the patient details in the global class so that can be accessed by further frames like
            # patient frame/medical record frame.
            GlobalAppData.set_curr_selected_patient(self.curr_search_results_display[cur_selection[0]])
            # Go to patient frame which has patient details for the user selected patient
            self.frame.enter_next_frame(1, True)

    def update_search_patient_list(self, patient_search_str):

        # Basic idea is to query the data base for the search results for patients
        # only if the first character of the patient search string is changed.
        # If so we query the DB for all the result and save them, if the first
        # character is not changed then we used the existing saved results to get
        # results.
        # Get the input search string
        input_search_string = patient_search_str.get()
        update_search_string = ""

        print("processing input string ", input_search_string)

        status = True
        if 0 != len(input_search_string):
            # First char is changed, first update the patient result data frame.
            if self.patient_result_df is None or self.patient_result_df.empty or \
                    (0 == len(self.curr_search_string)) or \
                    self.curr_search_string[0] != input_search_string[0]:
                # Query the data base using the input search string and get results.
                # TODO: Currently we over write the existing data frame, but for optimization it make sense
                # to keep the current data and instead of query the data base once the string changes
                # we can check in the existing results if data exists or not.
                status, self.patient_result_df = self.db_controller.db_get_all_patient(input_search_string[0])

            self.curr_search_string = input_search_string
        else:
            self.curr_search_string = ""

        print("doing search for ", self.curr_search_string, "df ", self.patient_result_df)

        # Delete existing results.
        self.search_result_list_box.delete(0, tk.END)

        self.curr_search_results_display = []

        if not status:
            self.search_result_list_box.insert(tk.END,
                                               get_patient_row_as_str(ERROR_SEARCHING_DATA_BASE_ENTRY_SEARCH_RESULTS))
            return
        else:
            # use the data frame to get the search results.
            if 0 != len(self.curr_search_string):
                self.curr_search_results_display = self.get_search_results(self.curr_search_string)

        print("updating patient list box ", self.curr_search_string, "\n", self.curr_search_results_display)

        # Update new results.
        for result in self.curr_search_results_display:
            # print("Results are ", result)
            self.search_result_list_box.insert(tk.END, get_patient_row_as_str([result]))

    # Init the frame class.
    def __init__(self, root, ws, hs, db_controller):

        self.db_controller = db_controller

        # Create a base frame object which has parent as main root window.
        self.frame = BaseFrame(root)

        self.curr_search_string = ""
        self.patient_result_df = None
        self.curr_search_results_display = []

        header_frame = tk.Frame(self.frame)

        tk.Label(header_frame, text=DOC_SPACE, font=WIDGET_FONT_1).grid(
            row=0, column=0)
        tk.Button(header_frame, text=LOG_OUT,
                  command=lambda: self.log_out_event_action(), font=WIDGET_FONT_1).grid(
            row=0, column=1, padx=(ws - 280, 0))
        header_frame.grid(row=0, column=0, sticky='w', pady=(hs / 10.4, 0))

        field_frame = tk.Frame(self.frame)

        row_idx = 0
        self.doctor_name_label = tk.Label(field_frame, text=WELCOME_LABEL, font=HEADING_FONT)
        self.doctor_name_label.grid(row=row_idx, column=0, columnspan='9', pady=(0, 50))
        row_idx += 1

        # Row 2 45
        self.search_result_list_box = tk.Listbox(field_frame, font=WIDGET_FONT, width=100, height=15)
        self.search_result_list_box.bind("<Double-1>", self.list_box_double_click_event_action)
        self.search_result_list_box.grid(row=row_idx, column=2, rowspan=24, pady=(0, 10), padx=(10, 0))

        # self.patient_search_str = tk.StringVar()
        # self.patient_search_str.trace("w", lambda name, index, mode: self.update_search_patient_list())
        self.patient_name_entry = CustomEntry(field_frame, ENTRY_MAX_LEN_20, alpha=True, digit=False,
                                              special_char=False, space_allowed=True,
                                              callback_fun=lambda patient_search_str:
                                              self.update_search_patient_list(patient_search_str),
                                              width=30, font=WIDGET_FONT)
        self.patient_name_entry.grid(row=row_idx, column=1, pady=(0, 10))

        row_idx += 1

        # Row 3
        tk.Label(field_frame, text=SEARCH_PATIENT_LABEL,
                 font=WIDGET_FONT).grid(
            row=row_idx, column=1, pady=(0, 30))
        row_idx += 1

        # Row 4
        tk.Button(field_frame, text=REGISTER_NEW_PATENT,
                  command=lambda: self.register_patient_event_action(), font=WIDGET_FONT).grid(
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
