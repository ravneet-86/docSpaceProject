import tkinter as tk
from tkinter import ttk

import utils
from frames.base_frame import BaseFrame
from constant import *
from frames.custom_entry import CustomEntry
from frames.custom_text import CustomText
from global_app_data import *
from tkinter import messagebox

'''
    DocSpace                                    LogOut
    Doctor:                Patient Details      Back	
    Patient Id	    Full Name       Gender      Age	
    
    DOB            Martial status  Occupation    contact No    
    Address                    City
    
    Medical Records    startDate endDate search
    Record Date+Case Type+ Symtoms + Investiagation         More Info		 	

'''
PATIENT_DETAILS = "Patient Details"
EDIT_PATIENT_INFO = "Check to Edit Patient Info"
UPDATE_PATIENT_INFO = "Update Patient Info"
MEDICAL_RECORDS = "Medical Records:"
ADD_MEDICAL_RECORD = "Add a Medical Record"
START_DATE = "Start Date"
END_DATE = "End Date"
SEARCH = "SEARCH"


# xFrame class is suppose to create a custom Base TK frame from the root object.
# This Frame has all the login frame widgets (instead of directly parent having it)
class PatientFrame:

    # Function which should be called whenever we enter this frame
    def frame_reload(self, full_reload):
        self.set_patient_info()

        error_msg, self.medical_records = self.db_controller.get_all_medical_records(self.patient_id_entry.get_text())
        self.list_box.delete(0, tk.END)
        if 0 != len(error_msg):
            messagebox.showerror(ERROR_BOX_TITLE, error_msg)
        else:
            for idx in range(len(self.medical_records)):
                self.list_box.insert(tk.END, utils.get_medical_record_as_str(self.medical_records[idx]))

        try:
            # Load the Doctor Name for Global app data.
            error_msg, doctor_name = self.db_controller.db_get_doctor_name()

            doctor_name = DOCTOR_NAME + doctor_name
            if 0 != len(error_msg):
                messagebox.showerror(ERROR_BOX_TITLE, error_msg)
            else:
                self.doctor_name_label.config(text=doctor_name)

        except Exception as e:
            print("MedicalRecordFrame::frame_reload:: Exception loading doctor info ", e)

        self.check_button_var.set(False)
        self.check_button_event_action()

    # Enter the first back frame which is the login frame on log out don't do full reload, as we
    # want user name password to remain filled.
    def log_out_event_action(self):
        self.frame.enter_back_frame(1, False)

    # Enter the first back frame which is the entry frame on log out don't do full reload, as we
    # want search result to show in this frame.
    def go_back_event_action(self):
        self.frame.enter_back_frame(2, False)

    def add_medical_record_event_action(self):
        self.frame.enter_next_frame(1, True)

    def update_patient_info_event_action(self):
        error_msg = self.db_controller.db_update_patient_info(self.patient_name_entry.get_text(),
                                                              self.patient_gender_entry.get_text(),
                                                              self.patient_age_entry.get_text(),
                                                              self.patient_contact_entry.get_text(),
                                                              self.patient_address_entry.get("1.0", tk.END),
                                                              self.patient_city_entry.get_text(),
                                                              self.patient_martial_s_entry.get_text(),
                                                              self.patient_occ_entry.get_text(),
                                                              self.patient_dob_entry.get_text(),
                                                              self.patient_id_entry.get_text())

        if 0 != len(error_msg):
            messagebox.showerror(ERROR_BOX_TITLE, error_msg)
        else:
            messagebox.showinfo(MESSAGE_BOX_TITLE, PATIENT_REGISTRATION_SUCCESS)

        self.set_patient_info()

    def list_box_double_click_event_action(self, event):
        # item = self.tree_view.selection()[0]
        # item = self.tree_view.identify('item', event.x, event.y)
        # print("you clicked on", self.tree_view.item(item, "text"))
        # item = self.tree_view.selection()
        # print("you clicked on", self.tree_view.item(item, "values")[0])
        # Curr selection is a tuple with first index refers to the index in the list box search display list.
        cur_selection = self.list_box.curselection()

        if None != self.medical_records and 0 != len(self.medical_records):
            print(self.medical_records[cur_selection[0]])

            # Save the Medical record in the global class so that can be accessed by further frames like
            # patient frame/medical record frame.
            # please note this record is only used when we double click a record in patient frame.
            # So it is responsibility of patient frame to reset it once it has consumed this. To prevent
            # unwanted usage of this record.
            GlobalAppData.set_curr_medical_record(self.medical_records[cur_selection[0]])
            # Go to Medical record frame which will display this medical record selected.
            self.frame.enter_next_frame(1, True)
        else:
            print("Patient_frame::list_box_double_click_event_action No medical record present ")

    def set_patient_info(self):
        patient_details = GlobalAppData.get_curr_selected_patient()

        self.patient_id_entry.set_text(patient_details[PATIENT_INFO_ID_INDEX])
        self.patient_name_entry.set_text(patient_details[PATIENT_INFO_NAME_INDEX])
        self.patient_gender_entry.set_text(patient_details[PATIENT_INFO_GENDER_INDEX])
        self.patient_martial_s_entry.set_text(patient_details[PATIENT_INFO_MARTIAL_STATUS_INDEX])
        self.patient_age_entry.set_text(patient_details[PATIENT_INFO_AGE_INDEX])
        self.patient_address_entry.delete(1.0, "end")
        self.patient_address_entry.insert("end", patient_details[PATIENT_INFO_ADDRESS_INDEX])
        self.patient_city_entry.set_text(patient_details[PATIENT_INFO_CITY_INDEX])
        self.patient_dob_entry.set_text(patient_details[PATIENT_INFO_DOB_INDEX])
        self.patient_occ_entry.set_text(patient_details[PATIENT_INFO_OCCUPATION_INDEX])
        self.patient_contact_entry.set_text(patient_details[PATIENT_INFO_CONTACT_NO_INDEX])

    # Action to perform when user clicks on event to check the button to update user info.
    def check_button_event_action(self):
        if self.check_button_var.get():
            self.patient_name_entry.configure(state='normal')
            self.patient_gender_entry.configure(state='normal')
            self.patient_martial_s_entry.configure(state='normal')
            self.patient_age_entry.configure(state='normal')
            self.patient_address_entry.configure(state='normal')
            self.patient_city_entry.configure(state='normal')
            self.patient_dob_entry.configure(state='normal')
            self.patient_occ_entry.configure(state='normal')
            self.patient_contact_entry.configure(state='normal')
            self.update_patient_info.grid(row=4, column=6)
        else:
            # TODO: Load default values which should be what we have currently in data base.
            self.patient_name_entry.configure(state='disabled')
            self.patient_gender_entry.configure(state='disabled')
            self.patient_martial_s_entry.configure(state='disabled')
            self.patient_age_entry.configure(state='disabled')
            self.patient_address_entry.configure(state='disabled')
            self.patient_city_entry.configure(state='disabled')
            self.patient_dob_entry.configure(state='disabled')
            self.patient_occ_entry.configure(state='disabled')
            self.patient_contact_entry.configure(state='disabled')
            self.update_patient_info.grid_remove()

    # Init the frame class.
    def __init__(self, root, ws, hs, db_controller):

        # Create a base frame object which has parent as main root window.
        self.frame = BaseFrame(root)
        self.db_controller = db_controller
        self.medical_records = None

        header_frame = tk.Frame(self.frame)
        tk.Label(header_frame, text=DOC_SPACE, font=WIDGET_FONT_1).grid(row=0, column=0)
        tk.Button(header_frame, text=LOG_OUT,
                  command=lambda: self.log_out_event_action(), font=WIDGET_FONT_1).grid(
            row=0, column=1, padx=(ws - 280, 0))
        header_frame.grid(row=0, column=0, pady=(10, 0), sticky='w')

        header_frame_1 = tk.Frame(self.frame)
        self.doctor_name_label = tk.Label(header_frame_1, text=DOCTOR_NAME, font=HEADING_FONT, width=30)
        self.doctor_name_label.grid(row=1, column=0, sticky='w')
        tk.Label(header_frame_1, text=PATIENT_DETAILS, font=HEADING_FONT).grid(row=1, column=6, padx=(100, 0))
        tk.Button(header_frame_1, text=GO_BACK,
                  command=lambda: self.go_back_event_action(), font=WIDGET_FONT_1).grid(
            row=1, column=7, padx=(330, 0))
        header_frame_1.grid(row=1, column=0, sticky='w')

        info_frame = tk.Frame(self.frame)
        c_idx = 0
        padx = 100

        tk.Label(info_frame, text=PATIENT_ID, font=WIDGET_FONT).grid(row=2, column=c_idx)
        c_idx += 1
        self.patient_id_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_10, alpha=True, digit=False,
                                            special_char=False, space_allowed=True, width=10, font=WIDGET_FONT,
                                            state='disabled')
        self.patient_id_entry.set_text("PS1")
        self.patient_id_entry.configure({"disabledbackground": "white"})
        self.patient_id_entry.configure({"disabledforeground": "black"})
        self.patient_id_entry.grid(row=2, column=c_idx)
        c_idx += 1

        tk.Label(info_frame, text=PATIENT_NAME, font=WIDGET_FONT).grid(row=2, column=c_idx, padx=(padx, 0))
        c_idx += 1
        self.patient_name_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_20, alpha=True, digit=False,
                                              special_char=False, space_allowed=True, width=20, font=WIDGET_FONT,
                                              state='disabled')
        self.patient_name_entry.set_text("12345678912345678901")
        self.patient_name_entry.configure({"disabledbackground": "white"})
        self.patient_name_entry.configure({"disabledforeground": "black"})
        self.patient_name_entry.grid(row=2, column=c_idx)
        c_idx += 1

        tk.Label(info_frame, text=PATIENT_GENDER, font=WIDGET_FONT).grid(row=2, column=c_idx, padx=(padx, 0))
        c_idx += 1
        self.patient_gender_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_6, alpha=True, digit=False,
                                                special_char=False, space_allowed=False, width=12, font=WIDGET_FONT,
                                                state='disabled')
        self.patient_gender_entry.set_text("12345678912345678901")
        self.patient_gender_entry.configure({"disabledbackground": "white"})
        self.patient_gender_entry.configure({"disabledforeground": "black"})
        self.patient_gender_entry.grid(row=2, column=c_idx)
        c_idx += 1

        tk.Label(info_frame, text=PATIENT_AGE, font=WIDGET_FONT).grid(row=2, column=c_idx, padx=(padx, 0))
        c_idx += 1
        self.patient_age_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_3, alpha=False, digit=True,
                                             special_char=False, space_allowed=False, width=3, font=WIDGET_FONT,
                                             state='disabled')
        self.patient_age_entry.set_text("12345678912345678901")
        self.patient_age_entry.configure({"disabledbackground": "white"})
        self.patient_age_entry.configure({"disabledforeground": "black"})
        self.patient_age_entry.grid(row=2, column=c_idx)
        print(c_idx)
        c_idx += 1
        # tk.Label(info_frame, text=PATIENT_DOB, font=WIDGET_FONT).grid(row=2, column=4, padx=(200, 0))
        c_idx = 0
        tk.Label(info_frame, text=PATIENT_DOB, font=WIDGET_FONT).grid(row=3, column=c_idx, pady=(10, 0))
        c_idx += 1
        self.patient_dob_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_10, alpha=False, digit=True,
                                             special_char=False, space_allowed=True, width=10, font=WIDGET_FONT,
                                             state='disabled')
        self.patient_dob_entry.set_text("02 01 1960")
        self.patient_dob_entry.configure({"disabledbackground": "white"})
        self.patient_dob_entry.configure({"disabledforeground": "black"})
        self.patient_dob_entry.grid(row=3, column=c_idx)
        c_idx += 1

        tk.Label(info_frame, text=PATIENT_OCCUPATION, font=WIDGET_FONT).grid(row=3, column=c_idx, padx=(padx, 0))
        c_idx += 1
        self.patient_occ_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_20, alpha=True, digit=False,
                                             special_char=False, space_allowed=False, width=20, font=WIDGET_FONT,
                                             state='disabled')
        self.patient_occ_entry.set_text("12345678912345678901")
        self.patient_occ_entry.configure({"disabledbackground": "white"})
        self.patient_occ_entry.configure({"disabledforeground": "black"})
        self.patient_occ_entry.grid(row=3, column=c_idx)
        c_idx += 1

        tk.Label(info_frame, text=PATIENT_MARTIAL_S, font=WIDGET_FONT).grid(row=3, column=c_idx, padx=(padx, 0))
        c_idx += 1
        self.patient_martial_s_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_10, alpha=True, digit=False,
                                                   special_char=False, space_allowed=False, width=10, font=WIDGET_FONT,
                                                   state='disabled')
        self.patient_martial_s_entry.set_text("12345678912345678901")
        self.patient_martial_s_entry.configure({"disabledbackground": "white"})
        self.patient_martial_s_entry.configure({"disabledforeground": "black"})
        self.patient_martial_s_entry.grid(row=3, column=c_idx)
        c_idx += 1

        tk.Label(info_frame, text=PATIENT_CONTACT_NO, font=WIDGET_FONT).grid(row=3, column=c_idx, padx=(padx, 0))
        c_idx += 1
        self.patient_contact_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_12, alpha=False, digit=True,
                                                 special_char=False, space_allowed=False, width=12, font=WIDGET_FONT,
                                                 state='disabled')
        self.patient_contact_entry.set_text("12345678912345678901")
        self.patient_contact_entry.configure({"disabledbackground": "white"})
        self.patient_contact_entry.configure({"disabledforeground": "black"})
        self.patient_contact_entry.grid(row=3, column=c_idx)
        c_idx += 1

        c_idx = 0
        tk.Label(info_frame, text=PATIENT_ADDRESS, font=WIDGET_FONT).grid(row=4, column=c_idx)
        c_idx += 1
        self.patient_address_entry = tk.Text(info_frame, width=20, font=WIDGET_FONT,
                                             height=3)
        # self.patient_address_entry.insert("end", "12345678912345678901 asdfasdf asdfasdfsadf asdfsadfasdf asdfsadfasdfasdfasdfsadfdsaf")
        # self.patient_address_entry.config(state='disabled')
        self.patient_address_entry.grid(row=4, column=c_idx, pady=(10, 0))
        c_idx += 1

        tk.Label(info_frame, text=PATIENT_CITY, font=WIDGET_FONT).grid(row=4, column=c_idx, sticky='e')
        c_idx += 1
        self.patient_city_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_10, alpha=True, digit=False,
                                              special_char=False, space_allowed=True, width=10, font=WIDGET_FONT,
                                              state='disabled')
        self.patient_city_entry.set_text("1234567890")
        self.patient_city_entry.configure({"disabledbackground": "white"})
        self.patient_city_entry.configure({"disabledforeground": "black"})
        self.patient_city_entry.grid(row=4, column=c_idx, sticky='w')
        c_idx += 1

        self.check_button_var = tk.BooleanVar()
        self.check_button_var.set(False)
        self.check_button = tk.Checkbutton(info_frame, text=EDIT_PATIENT_INFO, font=WIDGET_FONT,
                                           var=self.check_button_var, command=self.check_button_event_action)
        self.check_button.grid(row=4, column=c_idx)
        c_idx += 1
        self.update_patient_info = tk.Button(info_frame, text=UPDATE_PATIENT_INFO,
                                             command=self.update_patient_info_event_action, font=WIDGET_FONT)
        self.update_patient_info.grid(row=4, column=6)

        tk.Label(info_frame, text=MEDICAL_RECORDS, font=WIDGET_FONT).grid(row=5, column=0, pady=(20, 0), ipadx=20)
        tk.Button(info_frame, text=ADD_MEDICAL_RECORD, font=WIDGET_FONT,
                  command=self.add_medical_record_event_action).grid(row=5, column=6, pady=(20, 0))
        # tk.Label(info_frame, text=START_DATE, font=WIDGET_FONT).grid(row=5, column=1)
        # tk.Label(info_frame, text=END_DATE, font=WIDGET_FONT).grid(row=5, column=2)
        # tk.Button(info_frame, text=SEARCH, font=WIDGET_FONT).grid(row=5, column=3)

        info_frame.grid(row=2, column=0, sticky='w', pady=(20, 0))

        '''
        tree_view_grid = tk.Frame(self.frame)
        self.tree_view = ttk.Treeview(tree_view_grid, columns=1, show="headings", height='10')
        self.tree_view.heading(1, text="Medical Records")
        for i in range(400):
            val = str(i) + (' testasdfsafddsafdsfdsfsafsfsffsasdfsafsaf 13243243232324234 sadfsfdsafsadfdsafsf')
            self.tree_view.insert("", 'end', value=val)
        self.tree_view.bind("<Double-1>", self.tree_view_double_click_event_action)
        self.tree_view.grid(row=0, column=0, ipadx=10, padx=(20,0))


        tree_view_grid.grid(row=3, column=0, sticky='w', pady=(20, 0))
        '''
        list_box_grid = tk.Frame(self.frame)
        self.list_box = tk.Listbox(list_box_grid, font=WIDGET_FONT, height=20, width=120)
        #        self.list_box.heading(1, text="Medical Records")
        #        for i in range(400):
        #            val = str(i) + (' testasdfsafddsafdsfdsfsafsfsffsasdfsafsaf 13243243232324234 sadfsfdsafsadfdsafsf asdfasfadsfs 213213213123213213213123213213213 asdfsfdasfsadfafxbxbcnbcncnxcncxnxcncxnzbcxzxzvzvzxvzxvxczvxzvxzvcxzvcxzbvnmhjryertq224545yhghdgncvbxvxvxzbx estasdfsafddsafdsfdsfsafsfsffsasdfsafsaf 13243243232324234 sadfsfdsafsadfdsafsf asdfasfadsfs 213213213123213213213123213213213 asdfsfdasfsadfafxbxbcnbcncnxcncxnxcncxnzbcxzxzvzvzxvzxvxczvxzvxzvcxzvcxzbvnmhjryertq224545yhghdgncvbxvxvxzbx')
        #            self.list_box.insert(i, val)
        self.list_box.bind("<Double-1>", self.list_box_double_click_event_action)
        self.list_box.grid(row=0, column=0, ipadx=10, padx=(20, 0))

        scroll_bar = tk.Scrollbar(list_box_grid, orient='vertical', command=self.list_box.yview)
        scroll_bar.grid(row=0, column=1, sticky='ns')

        # Attaching Listbox to Scrollbar
        # Since we need to have a vertical
        # scroll we use yscrollcommand
        self.list_box.configure(yscrollcommand=scroll_bar.set)

        list_box_grid.grid(row=3, column=0, sticky='w', pady=(10, 0))
