import tkinter as tk
from frames.base_frame import BaseFrame
from frames.custom_entry import CustomEntry
from frames.custom_text import CustomText
from constant import *
from utils import *

'''
    DocSpace                                    LogOut
    Doctor:                Medical Record      Back	
    Patient Id	        Full Name        Gender             Age	
    DOB                 Martial status   Occupation       contact No    
    Symptoms            Symptoms Agg by  Symptoms amel by Symptoms since
    Present Complains   Case Type 
    Physical characterstics
    Physcial General
'''

NEW_MEDICAL_RECORD = "Medical Record"
SYMPTOMS = "Symptoms:"
SYMPTOMS_AGG_BY = "Symptoms\nAggravated By:"
SYMPTOMS_AMEOL_BY = "Symptoms\nAmeoliated By:"
SYMPTOMS_SINCE = "Symptoms\nsince:"
PRESENT_COMPLAIN = "Present\nComplain:"
CASE_TYPE = "Case Type:"
CASE_TYPE_DICT = {
                    "Chronic": "1",
                    "Acute": "2",
                    "General": "3"
                 }
PHYSICAL_CHAR = "Physical Characteristics"
PHYSICAL_CHAR_PARAMS = ["Back:", "Chest:", "Ear:", "Eye:", "Face:", "HEAD:",
                        "Lips:", "Mouth:", "Nose:", "Teeth:", "Throat:", "Tongue:"]

PHYSICAL_GENERAL = "Physical General"
PHYSICAL_GENERAL_PARAMS = ["Appetite:", "Thirst:", "Urine:", "Stool:", "Sleep:",
                           "Perspiration:", "Addictions:", "Desires:", "Aversions:",
                           "Thermal Reaction:", "Allergy:", "Mental Symptoms:"]

SYMPTOMS_INFO = "Symptoms Information"
PATIENT_DETAILS="Patient Details"

HISTORY = "History"
HISTORY_PARAMS = ["Past:", "Family:", "Menstrual:"]

MEDICINE_INFO = "Medicine Information"
MEDICINE_INFO_PARAMS = ["Medicine:", "Dose:", "Potency:", "Days:"]
INVESTIGATION = "Investigation:"
SAVE_RECORD = "Save Medical Record"


# xFrame class is suppose to create a custom Base TK frame from the root object.
# This Frame has all the login frame widgets (instead of directly parent having it)
class MedicalRecordFrame:

    # Function which should be called whenever we enter this frame
    def frame_reload(self, full_reload):
        print()

    # Enter the first back frame which is the login frame on log out don't do full reload, as we
    # want user name password to remain filled.
    def log_out_event_action(self):
        self.frame.enter_back_frame(1, False)

    # Enter the second back frame which is the patient frame.
    def go_back_event_action(self):
        self.frame.enter_back_frame(2, False)

    def create_physical_label_frame(self, phy_char_entry, label_str, label_params, f_r_idx, reps=1):

        phy_char_label_frame = tk.LabelFrame(self.frame, text=label_str, font=WIDGET_FONT_1)
        phy_char_label_frame.grid(row=f_r_idx, column=0, sticky='w', pady=(10, 0), padx=(5, 0))

        c_idx = 0
        r_idx = 0
        idx = 0

        for rep in range(reps):
            for param in label_params:
                tk.Label(phy_char_label_frame, text=param, font=WIDGET_FONT).grid(row=r_idx, column=c_idx)
                c_idx += 1
                phy_char_entry.append(CustomEntry(phy_char_label_frame, max_len=20, alpha=True,
                                                  digit=True,
                                                  special_char=True,
                                                  space_allowed=True,
                                                  width=20,
                                                  font=WIDGET_FONT
                                                  ))
                phy_char_entry[idx].grid(row=r_idx, column=c_idx, padx=(0, 5), pady=(0, 5))
                idx += 1

                if idx == 4 or idx == 8:
                    r_idx += 1
                    c_idx = 0
                else:
                    c_idx += 1

            r_idx += 1
            c_idx = 0

    # Init the frame class.
    def __init__(self, root, ws, hs):

        # Create a base frame object which has parent as main root window.
        self.frame = BaseFrame(root)

        set_grid_row_column_configure(self.frame, 3, 1)

        header_frame = tk.Frame(self.frame)
        tk.Label(header_frame, text=DOC_SPACE, font=WIDGET_FONT_1).grid(row=0, column=0)
        tk.Button(header_frame, text=LOG_OUT,
                  command=lambda: self.log_out_event_action(), font=WIDGET_FONT_1).grid(
                  row=0, column=1, padx=(ws-280, 0))

        set_grid_row_column_configure(header_frame, 1, 2)
        header_frame.grid(row=0, column=0, pady=(10, 0), sticky='w')

        header_frame_1 = tk.Frame(self.frame)
        self.doctor_name_label = tk.Label(header_frame_1, text=DOCTOR_NAME, font=HEADING_FONT, width=30)
        self.doctor_name_label.grid(row=0, column=0, sticky='w')
        tk.Label(header_frame_1, text=NEW_MEDICAL_RECORD, font=HEADING_FONT).grid(row=0,
                                                                                  column=6,
                                                                                  padx=(100, 0))
        tk.Button(header_frame_1, text=GO_BACK,
                  command=lambda: self.go_back_event_action(), font=WIDGET_FONT_1).grid(
                  row=0, column=7, padx=(330, 0))
        set_grid_row_column_configure(header_frame_1, 1, 8)
        header_frame_1.grid(row=1, column=0, sticky='w')

        patient_details_frame = tk.LabelFrame(self.frame, text=PATIENT_DETAILS, font=WIDGET_FONT_1)
        patient_details_frame.grid(row=2, column=0, sticky='w', pady=(10, 0), padx=(5, 0))

        c_idx = 0
        padx = 100

        tk.Label(patient_details_frame, text=PATIENT_ID, font=WIDGET_FONT).grid(row=0, column=c_idx)
        c_idx += 1
        self.patient_id_entry = CustomEntry(patient_details_frame, ENTRY_MAX_LEN_10, alpha=True,
                                            digit=False,
                                            special_char=False, space_allowed=True, width=10,
                                            font=WIDGET_FONT,
                                            state='disabled')
        self.patient_id_entry.set_text("PS1")
        #self.patient_id_entry.configure({"disabledbackground": "white"})
        #self.patient_id_entry.configure({"disabledforeground": "black"})
        self.patient_id_entry.grid(row=0, column=c_idx)
        c_idx += 1

        tk.Label(patient_details_frame, text=PATIENT_NAME, font=WIDGET_FONT).grid(row=0,
                                                                                  column=c_idx,
                                                                                  padx=(padx, 0))
        c_idx += 1
        self.patient_name_entry = CustomEntry(patient_details_frame, ENTRY_MAX_LEN_20, alpha=True,
                                              digit=False,
                                              special_char=False, space_allowed=True, width=20,
                                              font=WIDGET_FONT,
                                              state='disabled')
        self.patient_name_entry.set_text("12345678912345678901")
        #self.patient_name_entry.configure({"disabledbackground": "white"})
        #self.patient_name_entry.configure({"disabledforeground": "black"})
        self.patient_name_entry.grid(row=0, column=c_idx)
        c_idx += 1

        tk.Label(patient_details_frame, text=PATIENT_GENDER, font=WIDGET_FONT).grid(row=0,
                                                                                    column=c_idx,
                                                                                    padx=(padx, 0))
        c_idx += 1
        self.patient_gender_entry = CustomEntry(patient_details_frame, ENTRY_MAX_LEN_6, alpha=True,
                                                digit=False,
                                                special_char=False, space_allowed=False, width=12,
                                                font=WIDGET_FONT,
                                                state='disabled')
        self.patient_gender_entry.set_text("12345678912345678901")
        #self.patient_gender_entry.configure({"disabledbackground": "white"})
        #self.patient_gender_entry.configure({"disabledforeground": "black"})
        self.patient_gender_entry.grid(row=0, column=c_idx)
        c_idx += 1

        tk.Label(patient_details_frame, text=PATIENT_AGE, font=WIDGET_FONT).grid(row=0,
                                                                                 column=c_idx,
                                                                                 padx=(padx, 0))
        c_idx += 1
        self.patient_age_entry = CustomEntry(patient_details_frame, ENTRY_MAX_LEN_3, alpha=False,
                                             digit=True,
                                             special_char=False, space_allowed=False, width=3,
                                             font=WIDGET_FONT,
                                             state='disabled')
        self.patient_age_entry.set_text("12345678912345678901")
        #self.patient_age_entry.configure({"disabledbackground": "white"})
        #self.patient_age_entry.configure({"disabledforeground": "black"})
        self.patient_age_entry.grid(row=0, column=c_idx)
        c_idx += 1
        #tk.Label(info_frame, text=PATIENT_DOB, font=WIDGET_FONT).grid(row=2, column=4, padx=(200, 0))
        c_idx = 0
        tk.Label(patient_details_frame, text=PATIENT_DOB, font=WIDGET_FONT).grid(row=1,
                                                                                 column=c_idx,
                                                                                 pady=(10, 0))
        c_idx += 1
        self.patient_dob_entry = CustomEntry(patient_details_frame, ENTRY_MAX_LEN_10, alpha=False,
                                             digit=True,
                                             special_char=False, space_allowed=True, width=10,
                                             font=WIDGET_FONT,
                                             state='disabled')
        self.patient_dob_entry.set_text("02 01 1960")
        #self.patient_dob_entry.configure({"disabledbackground": "white"})
        #self.patient_dob_entry.configure({"disabledforeground": "black"})
        self.patient_dob_entry.grid(row=1, column=c_idx)
        c_idx += 1

        tk.Label(patient_details_frame, text=PATIENT_OCCUPATION, font=WIDGET_FONT).grid(row=1,
                                                                                        column=c_idx,
                                                                                        padx=(padx, 0))
        c_idx += 1
        self.patient_occ_entry = CustomEntry(patient_details_frame, ENTRY_MAX_LEN_20, alpha=True,
                                             digit=False,
                                             special_char=False, space_allowed=False, width=20,
                                             font=WIDGET_FONT,
                                             state='disabled')
        self.patient_occ_entry.set_text("12345678912345678901")
        #self.patient_occ_entry.configure({"disabledbackground": "white"})
        #self.patient_occ_entry.configure({"disabledforeground": "black"})
        self.patient_occ_entry.grid(row=1, column=c_idx)
        c_idx += 1

        tk.Label(patient_details_frame, text=PATIENT_MARTIAL_S, font=WIDGET_FONT).grid(row=1,
                                                                                       column=c_idx,
                                                                                       padx=(padx, 0))
        c_idx += 1
        self.patient_martial_s_entry = CustomEntry(patient_details_frame, ENTRY_MAX_LEN_10, alpha=True,
                                                   digit=False,
                                                   special_char=False, space_allowed=False, width=10,
                                                   font=WIDGET_FONT,
                                                   state='disabled')
        self.patient_martial_s_entry.set_text("12345678912345678901")
        #self.patient_martial_s_entry.configure({"disabledbackground": "white"})
        #self.patient_martial_s_entry.configure({"disabledforeground": "black"})
        self.patient_martial_s_entry.grid(row=1, column=c_idx)
        c_idx += 1

        tk.Label(patient_details_frame, text=PATIENT_CONTACT_NO, font=WIDGET_FONT).grid(row=1,
                                                                                        column=c_idx,
                                                                                        padx=(padx, 0))
        c_idx += 1
        self.patient_contact_entry = CustomEntry(patient_details_frame, ENTRY_MAX_LEN_12, alpha=False,
                                                 digit=True,
                                                 special_char=False, space_allowed=False, width=12,
                                                 font=WIDGET_FONT,
                                                 state='disabled')
        self.patient_contact_entry.set_text("12345678912345678901")
        #self.patient_contact_entry.configure({"disabledbackground": "white"})
        #self.patient_contact_entry.configure({"disabledforeground": "black"})
        self.patient_contact_entry.grid(row=1, column=c_idx)
        c_idx += 1

        symptoms_info_frame = tk.LabelFrame(self.frame, text=SYMPTOMS_INFO, font=WIDGET_FONT_1)
        symptoms_info_frame.grid(row=3, column=0, sticky='w', pady=(10, 0), padx=(5, 0))

        c_idx = 0
        tk.Label(symptoms_info_frame, text=SYMPTOMS, font=WIDGET_FONT).grid(row=0,
                                                                            column=c_idx,
                                                                            pady=(10, 0))
        c_idx += 1
        self.patient_symptoms_entry = CustomText(symptoms_info_frame, max_len=50, alpha=True,
                                                 digit=True,
                                                 special_char=True,
                                                 space_allowed=True,
                                                 width=20, height=3,
                                                 font=WIDGET_FONT
                                                 )
        self.patient_symptoms_entry.grid(row=0, column=c_idx)
        c_idx += 1

        tk.Label(symptoms_info_frame, text=SYMPTOMS_AGG_BY, font=WIDGET_FONT).grid(row=0,
                                                                                   column=c_idx)
        c_idx += 1
        self.patient_agg_entry = CustomText(symptoms_info_frame, max_len=50, alpha=True, digit=True,
                                            special_char=True,
                                            space_allowed=True,
                                            width=20, height=3,
                                            font=WIDGET_FONT
                                            )
        self.patient_agg_entry.grid(row=0, column=c_idx)
        c_idx += 1

        tk.Label(symptoms_info_frame, text=SYMPTOMS_AMEOL_BY, font=WIDGET_FONT).grid(row=0,
                                                                                     column=c_idx)
        c_idx += 1
        self.patient_ameol_entry = CustomText(symptoms_info_frame, max_len=50, alpha=True,
                                              digit=True,
                                              special_char=True,
                                              space_allowed=True,
                                              width=20, height=3,
                                              font=WIDGET_FONT
                                              )
        self.patient_ameol_entry.grid(row=0, column=c_idx)
        c_idx += 1

        tk.Label(symptoms_info_frame, text=SYMPTOMS_SINCE, font=WIDGET_FONT).grid(row=0, column=c_idx)
        c_idx += 1
        self.patient_sym_since_entry = CustomText(symptoms_info_frame, max_len=50, alpha=True,
                                                  digit=True,
                                                  special_char=True,
                                                  space_allowed=True,
                                                  width=20, height=3,
                                                  font=WIDGET_FONT
                                                  )
        self.patient_sym_since_entry.grid(row=0, column=c_idx)

        c_idx = 0
        tk.Label(symptoms_info_frame, text=PRESENT_COMPLAIN, font=WIDGET_FONT).grid(row=1,
                                                                                    column=c_idx)
                                                                           #, pady=(10, 0))
        c_idx += 1

        self.patient_present_complain_entry = CustomText(symptoms_info_frame, max_len=50, alpha=True,
                                                         digit=True,
                                                         special_char=True,
                                                         space_allowed=True,
                                                         width=20, height=3,
                                                         font=WIDGET_FONT
                                                         )
        self.patient_present_complain_entry.grid(row=1, column=c_idx, pady=(10, 5))
        c_idx += 1

        tk.Label(symptoms_info_frame, text=CASE_TYPE, font=WIDGET_FONT).grid(row=1,
                                                                             column=c_idx)
        c_idx += 1
        # Dictionary to create multiple buttons

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        for (text, value) in CASE_TYPE_DICT.items():
            tk.Radiobutton(symptoms_info_frame, text=text,
                           value=value).grid(row=1, column=c_idx)
            c_idx += 1

        self.phy_char_entry = []

        r_idx = 4
        self.create_physical_label_frame(self.phy_char_entry, PHYSICAL_CHAR, PHYSICAL_CHAR_PARAMS, r_idx)
        r_idx += 1

        self.phy_general_entry = []
        self.create_physical_label_frame(self.phy_general_entry, PHYSICAL_GENERAL,
                                         PHYSICAL_GENERAL_PARAMS,
                                         r_idx)
        r_idx += 1
        self.history_entry = []
        self.create_physical_label_frame(self.history_entry, HISTORY,
                                         HISTORY_PARAMS,
                                         r_idx)
        r_idx += 1

        self.medicine_info_entry = []
        self.create_physical_label_frame(self.medicine_info_entry, MEDICINE_INFO,
                                         MEDICINE_INFO_PARAMS,
                                         r_idx, 8)
        r_idx += 1
        end_frame = tk.Frame(self.frame)
        end_frame.grid(row=r_idx, column=0, sticky='w', pady=(10, 0), padx=(5, 0))

        tk.Label(end_frame, text=INVESTIGATION, font=WIDGET_FONT).grid(row=0,
                                                                       column=0,
                                                                       padx=(0, 5), pady=(0, 5)
                                                                       )

        self.patient_investigation_entry = CustomText(end_frame, max_len=50, alpha=True,
                                                      digit=True,
                                                      special_char=True,
                                                      space_allowed=True,
                                                      width=40, height=3,
                                                      font=WIDGET_FONT
                                                      )
        self.patient_investigation_entry.grid(row=0, column=1)

        tk.Button(end_frame, text=SAVE_RECORD, font=WIDGET_FONT).grid(row=0,
                                                                      column=2,
                                                                      padx=(80, 0))

