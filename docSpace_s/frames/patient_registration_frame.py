import tkinter as tk
from frames.base_frame import BaseFrame
from constant import *
from frames.custom_entry import CustomEntry
from frames.custom_text import CustomText
from tkinter import messagebox

REGISTER_PATIENT = "Register Patient"
RESET = "Reset"

'''
DocSpace                                                            log out
                    Please Enter Patient Details
                        Name
                        Gender
                        Age
                        Contact
                        Address
                        City
                        Martial Status
                        Occupation
                        Date of Birth
                        Doctor Information

'''

ENTER_PATIENT_DETAILS = "Please Enter Patient Details below:"
MANDATORY = "*"


# xFrame class is suppose to create a custom Base TK frame from the root object.
# This Frame has all the entry frame widgets (instead of directly parent having it)
class PatientRegistrationFrame:

    # Function which should be called whenever we enter this frame
    def frame_reload(self, full_reload):
        self.patient_name_entry.set_text(""),
        self.patient_gender_entry.set_text(""),
        self.patient_age_entry.set_text(""),
        self.patient_contact_entry.set_text(""),
        self.patient_address_entry.set_text(""),
        self.patient_city_entry.set_text(""),
        self.patient_martial_s_entry.set_text(""),
        self.patient_occ_entry.set_text(""),
        self.patient_dob_entry.set_text("")

    # Enter the first back frame which is the login frame on log out don't do full reload, as we
    # want user name password to remain filled.
    def log_out_event_action(self):
        self.frame.enter_back_frame(1, False)

    # Enter the second back frame which is the entry frame on go back out don't do full reload.
    def go_back_event_action(self):
        self.frame.enter_back_frame(2, False)

    # Does the data base call to register the patient into the patient data base for the logged in docter.
    def register_patient_event_action(self):

        # First check if name is entered by the user or not.
        if 0 == len(self.patient_name_entry.get_text()):
            messagebox.showerror(ERROR_BOX_TITLE, "Please fill Name Entry and try again")
            return

        # Check if a patient with given details already exist or not by name.
        status, patient_details_str = self.db_controller.db_check_patient_exist_by_name(
                                      self.patient_name_entry.get_text())

        if not status:
            messagebox.showerror(ERROR_BOX_TITLE, ERROR_PATIENT_REGISTRATION_CHECK_USER_EXIST_IN_DB_FAILURE)
            return

        register_user = True
        # In case patient already exist, indicate to the user and move to search window.
        if patient_details_str is not None and 0 != len(patient_details_str):
            register_user = messagebox.askyesno(self.patient_name_entry.get_text() + " Already Exists, press 'yes' to "
                                                                                     "create new user 'no' to go back",
                                                message=patient_details_str)

        error_msg = ""
        # If register user is 'yes' save the user info in Database.
        if register_user:

            error_msg = self.db_controller.db_register_patient_info(self.patient_name_entry.get_text(),
                                                                    self.patient_gender_entry.get_text(),
                                                                    self.patient_age_entry.get_text(),
                                                                    self.patient_contact_entry.get_text(),
                                                                    self.patient_address_entry.get_text(),
                                                                    self.patient_city_entry.get_text(),
                                                                    self.patient_martial_s_entry.get_text(),
                                                                    self.patient_occ_entry.get_text(),
                                                                    self.patient_dob_entry.get_text())
        else:
            # Go back to Entry page where user can see the search result of the existing users.
            self.frame.enter_back_frame(2, True)
            return

        if len(error_msg) != 0:
            messagebox.showerror(ERROR_BOX_TITLE, error_msg)
            return

        messagebox.showinfo(MESSAGE_BOX_TITLE, PATIENT_REGISTRATION_SUCCESS)
        # Go next to the add medical record frame/page.
        print("Patient_registration:: going to next frame medical record")
        self.frame.enter_next_frame(1, True)

    # Init the frame class.
    def __init__(self, root, ws, hs, db_controller):
        self.db_controller = db_controller

        # Create a base frame object which has parent as main root window.
        self.frame = BaseFrame(root)

        header_frame = tk.Frame(self.frame)

        tk.Label(header_frame, text=DOC_SPACE, font=WIDGET_FONT_1).grid(
            row=0, column=0)
        tk.Button(header_frame, text=LOG_OUT,
                  command=lambda: self.log_out_event_action(), font=WIDGET_FONT_1).grid(
            row=0, column=1, padx=(ws - 280, 0))
        tk.Label(header_frame, text=ENTER_PATIENT_DETAILS, font=HEADING_FONT).grid(row=1, column=1,
                                                                                   columnspan=4)

        tk.Label(header_frame, text=MANDATORY_FIELDS, font=WIDGET_FONT_SMALL).grid(
                 row=2, column=1, ipadx=400, columnspan=3)

        tk.Button(header_frame, text=GO_BACK,
                  command=lambda: self.go_back_event_action(),
                  font=WIDGET_FONT_1).grid(row=1, column=5)
        header_frame.grid(row=0, column=0, pady=(hs / 10.4, 0))

        info_frame = tk.Frame(self.frame)
        info_frame.grid(row=1, column=0, pady=(10, 0))
        r_idx = 0
        padx = 100
        pady = 7

        tk.Label(info_frame, text=PATIENT_NAME + MANDATORY, font=WIDGET_FONT).grid(row=r_idx, column=0,
                                                                                   padx=(padx, 0), pady=(pady, 0))
        self.patient_name_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_20, alpha=True, digit=False,
                                              special_char=False, space_allowed=True, width=20,
                                              font=WIDGET_FONT)
        self.patient_name_entry.configure({"disabledbackground": "white"})
        self.patient_name_entry.configure({"disabledforeground": "black"})
        self.patient_name_entry.grid(row=r_idx, column=1)
        r_idx += 1

        tk.Label(info_frame, text=PATIENT_GENDER, font=WIDGET_FONT).grid(row=r_idx, column=0,
                                                                         padx=(padx, 0), pady=(pady, 0)
                                                                         )
        self.patient_gender_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_6, alpha=True, digit=False,
                                                special_char=False, space_allowed=False, width=12,
                                                font=WIDGET_FONT)
        self.patient_gender_entry.configure({"disabledbackground": "white"})
        self.patient_gender_entry.configure({"disabledforeground": "black"})
        self.patient_gender_entry.grid(row=r_idx, column=1)
        r_idx += 1

        tk.Label(info_frame, text=PATIENT_AGE, font=WIDGET_FONT).grid(row=r_idx, column=0,
                                                                      padx=(padx, 0), pady=(pady, 0))
        self.patient_age_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_3, alpha=False, digit=True,
                                             special_char=False, space_allowed=False, width=3,
                                             font=WIDGET_FONT)
        self.patient_age_entry.configure({"disabledbackground": "white"})
        self.patient_age_entry.configure({"disabledforeground": "black"})
        self.patient_age_entry.grid(row=r_idx, column=1)
        r_idx += 1

        tk.Label(info_frame, text=PATIENT_DOB, font=WIDGET_FONT).grid(row=r_idx, column=0,
                                                                      padx=(padx, 0), pady=(pady, 0))
        self.patient_dob_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_10, alpha=False, digit=True,
                                             special_char=True, space_allowed=True, width=10,
                                             font=WIDGET_FONT)
        self.patient_dob_entry.configure({"disabledbackground": "white"})
        self.patient_dob_entry.configure({"disabledforeground": "black"})
        self.patient_dob_entry.grid(row=r_idx, column=1)
        r_idx += 1

        tk.Label(info_frame, text=PATIENT_OCCUPATION, font=WIDGET_FONT).grid(row=r_idx, column=0,
                                                                             padx=(padx, 0), pady=(pady, 0))
        self.patient_occ_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_20, alpha=True, digit=False,
                                             special_char=False, space_allowed=True, width=20,
                                             font=WIDGET_FONT)
        self.patient_occ_entry.configure({"disabledbackground": "white"})
        self.patient_occ_entry.configure({"disabledforeground": "black"})
        self.patient_occ_entry.grid(row=r_idx, column=1)
        r_idx += 1

        tk.Label(info_frame, text=PATIENT_MARTIAL_S, font=WIDGET_FONT).grid(row=r_idx, column=0,
                                                                            padx=(padx, 0), pady=(pady, 0))
        self.patient_martial_s_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_10, alpha=True, digit=False,
                                                   special_char=False, space_allowed=False, width=10,
                                                   font=WIDGET_FONT)
        self.patient_martial_s_entry.configure({"disabledbackground": "white"})
        self.patient_martial_s_entry.configure({"disabledforeground": "black"})
        self.patient_martial_s_entry.grid(row=r_idx, column=1)
        r_idx += 1

        tk.Label(info_frame, text=PATIENT_CONTACT_NO, font=WIDGET_FONT).grid(row=r_idx, column=0,
                                                                             padx=(padx, 0), pady=(pady, 0))
        self.patient_contact_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_12, alpha=False, digit=True,
                                                 special_char=False, space_allowed=False, width=12,
                                                 font=WIDGET_FONT)
        self.patient_contact_entry.configure({"disabledbackground": "white"})
        self.patient_contact_entry.configure({"disabledforeground": "black"})
        self.patient_contact_entry.grid(row=r_idx, column=1)
        r_idx += 1

        tk.Label(info_frame, text=PATIENT_ADDRESS, font=WIDGET_FONT).grid(row=r_idx, column=0,
                                                                          padx=(padx, 0), pady=(pady, 0))
        self.patient_address_entry = CustomText(info_frame, ENTRY_MAX_LEN_50, alpha=True, digit=True,
                                                special_char=True, space_allowed=True, width=20,
                                                font=WIDGET_FONT, height=3)
        self.patient_address_entry.grid(row=r_idx, column=1, pady=(pady, 0))
        r_idx += 1

        tk.Label(info_frame, text=PATIENT_CITY, font=WIDGET_FONT).grid(row=r_idx, column=0,
                                                                       padx=(padx, 0), pady=(pady, 0))
        self.patient_city_entry = CustomEntry(info_frame, ENTRY_MAX_LEN_10, alpha=True, digit=False,
                                              special_char=False, space_allowed=True, width=10,
                                              font=WIDGET_FONT)
        self.patient_city_entry.configure({"disabledbackground": "white"})
        self.patient_city_entry.configure({"disabledforeground": "black"})
        self.patient_city_entry.grid(row=r_idx, column=1, pady=(pady, 0))
        r_idx += 1

        tk.Button(info_frame, text=REGISTER_PATIENT, font=WIDGET_FONT,
                  command=lambda: self.register_patient_event_action()).grid(row=r_idx, column=0,
                                                                             padx=(padx, 0),
                                                                             pady=(pady + 20, 0))

        tk.Button(info_frame, text=RESET, font=WIDGET_FONT).grid(row=r_idx, column=1,
                                                                 padx=(padx, 0), pady=(pady + 20, 0))
