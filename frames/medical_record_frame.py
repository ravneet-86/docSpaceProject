import tkinter as tk
from frames.base_frame import BaseFrame
from frames.custom_entry import CustomEntry
from frames.custom_text import CustomText
from constant import *
from utils import *
from global_app_data import GlobalAppData
from datetime import datetime
from tkinter import messagebox

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
PATIENT_DETAILS = "Patient Details"

HISTORY = "History"
HISTORY_PARAMS = ["Past:", "Family:", "Menstrual:"]

MEDICINE_INFO = "Medicine Information"
MEDICINE_INFO_PARAMS = ["Medicine:", "Dose:", "Potency:", "Days:", "Amount:"]
INVESTIGATION = "Investigation:"
SAVE_RECORD = "Save Medical Record"
TOTAL_AMOUNT = "Total Amount"
RECORD_DATE = "Record Date:"
NEXT_DATE = "Next Date:"
GENERATE_PRESCRIPTION = "Generate Prescription"
NUM_OF_MEDICAL_INFO_ENTRIES = 8


# xFrame class is suppose to create a custom Base TK frame from the root object.
# This Frame has all the login frame widgets (instead of directly parent having it)
class MedicalRecordFrame:

    # Function which should be called whenever we enter this frame
    def frame_reload(self, full_reload):
        self.set_patient_info()

        if GlobalAppData.get_curr_medical_record() is not None:
            self.set_medical_record(GlobalAppData.get_curr_medical_record())
            # Reset the data to None so that i can't be used again.
            GlobalAppData.set_curr_medical_record(None)
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

    def set_medical_record(self, medical_record):
        self.patient_id_entry.set_text(medical_record[MEDICAL_RECORD_TABLE_ID_INDEX])
        self.record_date_entry.set_text(medical_record[MEDICAL_RECORD_TABLE_RECORD_DATE_INDEX])
        self.case_type_var.set(medical_record[MEDICAL_RECORD_TABLE_CASE_TYPE_INDEX])
        self.patient_symptoms_entry.set_text(medical_record[MEDICAL_RECORD_TABLE_SYMPTOMS_INDEX])
        self.patient_agg_entry.set_text(medical_record[MEDICAL_RECORD_TABLE_SYMPTOMS_AGG_BY_INDEX])
        self.patient_ameol_entry.set_text(medical_record[MEDICAL_RECORD_TABLE_SYMPTOMS_AMEOL_BY_INDEX])
        self.patient_sym_since_entry.set_text(medical_record[MEDICAL_RECORD_TABLE_SYMPTOMS_SINCE_INDEX])
        self.patient_present_complain_entry.set_text(medical_record[MEDICAL_RECORD_TABLE_PRESENT_COMPLAINS_INDEX])
        self.phy_general_entry[0].set_text(medical_record[MEDICAL_RECORD_TABLE_APPETITE_INDEX])  # 'appetite'
        self.phy_general_entry[1].set_text(medical_record[MEDICAL_RECORD_TABLE_THIRST_INDEX])  # 'thirst'
        self.phy_general_entry[2].set_text(medical_record[MEDICAL_RECORD_TABLE_URINE_INDEX])  # 'urine'
        self.phy_general_entry[3].set_text(medical_record[MEDICAL_RECORD_TABLE_STOOL_INDEX])  # 'stool'
        self.phy_general_entry[4].set_text(medical_record[MEDICAL_RECORD_TABLE_SLEEP_INDEX])  # 'sleep'
        self.phy_general_entry[5].set_text(medical_record[MEDICAL_RECORD_TABLE_PERSPIRATION_INDEX])  # 'perspiration'
        self.phy_general_entry[6].set_text(medical_record[MEDICAL_RECORD_TABLE_ADDICTIONS_INDEX])  # 'addiction'
        self.phy_general_entry[7].set_text(medical_record[MEDICAL_RECORD_TABLE_DESIRES_INDEX])  # 'desires'
        self.phy_general_entry[8].set_text(medical_record[MEDICAL_RECORD_TABLE_AVERSIONS_INDEX])  # 'aversions'
        self.phy_general_entry[9].set_text(medical_record[MEDICAL_RECORD_TABLE_THERMAL_REACTION_INDEX])  # 'thermal_reaction'
        self.phy_general_entry[10].set_text(medical_record[MEDICAL_RECORD_TABLE_ALLERGY_INDEX])  # 'allergy'
        self.phy_general_entry[11].set_text(medical_record[MEDICAL_RECORD_TABLE_MENTAL_SYMPTOMS_INDEX])  # 'mental_symptoms'
        self.phy_char_entry[0].set_text(medical_record[MEDICAL_RECORD_TABLE_BACK_INDEX])  # 'back'
        self.phy_char_entry[1].set_text(medical_record[MEDICAL_RECORD_TABLE_CHEST_INDEX])  # 'chest'
        self.phy_char_entry[2].set_text(medical_record[MEDICAL_RECORD_TABLE_EAR_INDEX])  # 'ear'
        self.phy_char_entry[3].set_text(medical_record[MEDICAL_RECORD_TABLE_EYE_INDEX])  # 'eye'
        self.phy_char_entry[4].set_text(medical_record[MEDICAL_RECORD_TABLE_FACE_INDEX])  # 'face'
        self.phy_char_entry[5].set_text(medical_record[MEDICAL_RECORD_TABLE_HEAD_INDEX])  # 'head'
        self.phy_char_entry[6].set_text(medical_record[MEDICAL_RECORD_TABLE_LIPS_INDEX])  # 'lips'
        self.phy_char_entry[7].set_text(medical_record[MEDICAL_RECORD_TABLE_MOUTH_INDEX])  # 'mouth'
        self.phy_char_entry[8].set_text(medical_record[MEDICAL_RECORD_TABLE_NOSE_INDEX])  # 'nose'
        self.phy_char_entry[9].set_text(medical_record[MEDICAL_RECORD_TABLE_TEETH_INDEX])  # 'teeth'
        self.phy_char_entry[10].set_text(medical_record[MEDICAL_RECORD_TABLE_THROAT_INDEX])  # 'throat'
        self.phy_char_entry[11].set_text(medical_record[MEDICAL_RECORD_TABLE_TONGUE_INDEX])  # 'tongue'
        self.history_entry[0].set_text(medical_record[MEDICAL_RECORD_TABLE_PAST_HISTORY_INDEX])  # 'past_history'
        self.history_entry[1].set_text(medical_record[MEDICAL_RECORD_TABLE_FAMILY_HISTORY_INDEX])  # 'family_history'
        self.history_entry[2].set_text(medical_record[MEDICAL_RECORD_TABLE_MENSTRUAL_HISTORY_INDEX])  # 'menstrual_history'
        self.patient_investigation_entry.set_text(medical_record[MEDICAL_RECORD_TABLE_INVESTIGATION_INDEX])  # 'Investigation'
        self.set_medicine_info_list(0, medical_record[MEDICAL_RECORD_TABLE_MEDICINE_INDEX])  # 'medicine'
        self.set_medicine_info_list(1, medical_record[MEDICAL_RECORD_TABLE_DOSE_INDEX])  # dose
        self.set_medicine_info_list(2, medical_record[MEDICAL_RECORD_TABLE_POTENCY_INDEX])  # potency
        self.set_medicine_info_list(3, medical_record[MEDICAL_RECORD_TABLE_DAYS_INDEX])  # days
        self.next_date_entry.set_text(medical_record[MEDICAL_RECORD_TABLE_NEXT_VISIT_INDEX])  # 'next_visit_date'
        self.set_medicine_info_list(4, medical_record[MEDICAL_RECORD_TABLE_AMOUNT_INDEX])  # 'amount'

    # Enter the first back frame which is the login frame on log out don't do full reload, as we
    # want user name password to remain filled.
    def log_out_event_action(self):
        self.frame.enter_back_frame(1, False)

    # Enter the second back frame which is the patient frame.
    def go_back_event_action(self):
        self.frame.enter_back_frame(2, False)

    def generate_prescription_event_action(self):
        print("generate")

    def set_patient_info(self):
        patient_details = GlobalAppData.get_curr_selected_patient()

        self.patient_id_entry.set_text(patient_details[PATIENT_INFO_ID_INDEX])
        self.patient_name_entry.set_text(patient_details[PATIENT_INFO_NAME_INDEX])
        self.patient_gender_entry.set_text(patient_details[PATIENT_INFO_GENDER_INDEX])
        self.patient_martial_s_entry.set_text(patient_details[PATIENT_INFO_MARTIAL_STATUS_INDEX])
        self.patient_age_entry.set_text(patient_details[PATIENT_INFO_AGE_INDEX])
        self.patient_dob_entry.set_text(patient_details[PATIENT_INFO_DOB_INDEX])
        self.patient_occ_entry.set_text(patient_details[PATIENT_INFO_OCCUPATION_INDEX])
        self.patient_contact_entry.set_text(patient_details[PATIENT_INFO_CONTACT_NO_INDEX])

    def get_medicine_info_list(self, index):
        info_list = []
        for i in range(NUM_OF_MEDICAL_INFO_ENTRIES):
            info_list.append(self.medicine_info_entry[index].get_text())
            index += len(MEDICINE_INFO_PARAMS)
        return encode_single_value(info_list, ',')

    def set_medicine_info_list(self, index, medicine_info_string):
        info_list = decode_single_value(medicine_info_string, ',')

        # a good to have check, we should always follow this.
        if None != info_list and len(info_list) == NUM_OF_MEDICAL_INFO_ENTRIES:
            for i in range(NUM_OF_MEDICAL_INFO_ENTRIES):
                self.medicine_info_entry[index].set_text(info_list[i])
                index += len(MEDICINE_INFO_PARAMS)
        else:
            print("medical_record_frame::set_medicine_info_list list mismatch for index " + str(index) +
                  " info list ", info_list)

    # Function will save the medical record in the data base and generates the prescription.
    def save_medical_record_event_action(self):
        values = [self.patient_id_entry.get_text(),
                  self.record_date_entry.get_text(),
                  self.case_type_var.get(),
                  self.patient_symptoms_entry.get_text(),
                  self.patient_agg_entry.get_text(),
                  self.patient_ameol_entry.get_text(),
                  self.patient_sym_since_entry.get_text(),
                  self.patient_present_complain_entry.get_text(),
                  self.phy_general_entry[0].get_text(),  # 'appetite'
                  self.phy_general_entry[1].get_text(),  # 'thirst'
                  self.phy_general_entry[2].get_text(),  # 'urine'
                  self.phy_general_entry[3].get_text(),  # 'stool'
                  self.phy_general_entry[4].get_text(),  # 'sleep'
                  self.phy_general_entry[5].get_text(),  # 'perspiration'
                  self.phy_general_entry[6].get_text(),  # 'addiction'
                  self.phy_general_entry[7].get_text(),  # 'desires'
                  self.phy_general_entry[8].get_text(),  # 'aversions'
                  self.phy_general_entry[9].get_text(),  # 'thermal_reaction'
                  self.phy_general_entry[10].get_text(),  # 'allergy'
                  self.phy_general_entry[11].get_text(),  # 'mental_symptoms'
                  self.phy_char_entry[0].get_text(),  # 'back'
                  self.phy_char_entry[1].get_text(),  # 'chest'
                  self.phy_char_entry[2].get_text(),  # 'ear'
                  self.phy_char_entry[3].get_text(),  # 'eye'
                  self.phy_char_entry[4].get_text(),  # 'face'
                  self.phy_char_entry[5].get_text(),  # 'head'
                  self.phy_char_entry[6].get_text(),  # 'lips'
                  self.phy_char_entry[7].get_text(),  # 'mouth'
                  self.phy_char_entry[8].get_text(),  # 'nose'
                  self.phy_char_entry[9].get_text(),  # 'teeth'
                  self.phy_char_entry[10].get_text(),  # 'throat'
                  self.phy_char_entry[11].get_text(),  # 'tongue'
                  self.history_entry[0].get_text(),  # 'past_history'
                  self.history_entry[1].get_text(),  # 'family_history'
                  self.history_entry[2].get_text(),  # 'menstrual_history'
                  self.patient_investigation_entry.get_text(),  # 'Investigation'
                  self.get_medicine_info_list(0),  # 'medicine'
                  self.get_medicine_info_list(1),  # dose
                  self.get_medicine_info_list(2),  # potency
                  self.get_medicine_info_list(3),  # days
                  self.next_date_entry.get_text(),  # 'next_visit_date'
                  self.get_medicine_info_list(4),  # 'amount'
                  ]
        error_msg = self.db_controller.db_save_patient_medical_record(values)

        if 0 != len(error_msg):
            # Failure..
            messagebox.showerror(ERROR_BOX_TITLE, error_msg)
        else:
            messagebox.showinfo(MESSAGE_BOX_TITLE, MEDICAL_RECORD_SAVED_SUCCESS)

    def create_physical_label_frame(self, phy_char_entry, label_str, label_params, f_r_idx, num_col=4, reps=1):

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
                                                  special_char=False,
                                                  space_allowed=True,
                                                  width=20,
                                                  font=WIDGET_FONT
                                                  ))
                phy_char_entry[idx].grid(row=r_idx, column=c_idx, padx=(0, 5), pady=(0, 5))
                idx += 1

                # if idx == 4 or idx == 8:
                if idx != 0 and idx % num_col == 0:
                    r_idx += 1
                    c_idx = 0
                else:
                    c_idx += 1

            r_idx += 1
            c_idx = 0

    # Init the frame class.
    def __init__(self, root, ws, hs, db_controller):

        # Create a base frame object which has parent as main root window.
        self.frame = BaseFrame(root)
        self.db_controller = db_controller

        set_grid_row_column_configure(self.frame, 3, 1)

        header_frame = tk.Frame(self.frame)
        tk.Label(header_frame, text=DOC_SPACE, font=WIDGET_FONT_1).grid(row=0, column=0)
        tk.Button(header_frame, text=LOG_OUT,
                  command=lambda: self.log_out_event_action(), font=WIDGET_FONT_1).grid(
            row=0, column=1, padx=(ws - 280, 0))

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
        padx = 10

        tk.Label(patient_details_frame, text=PATIENT_ID, font=WIDGET_FONT).grid(row=0, column=c_idx)
        c_idx += 1
        self.patient_id_entry = CustomEntry(patient_details_frame, ENTRY_MAX_LEN_10, alpha=True,
                                            digit=False,
                                            special_char=False, space_allowed=True, width=10,
                                            font=WIDGET_FONT,
                                            state='disabled')
        self.patient_id_entry.set_text("PS1")
        # self.patient_id_entry.configure({"disabledbackground": "white"})
        # self.patient_id_entry.configure({"disabledforeground": "black"})
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
        # self.patient_name_entry.configure({"disabledbackground": "white"})
        # self.patient_name_entry.configure({"disabledforeground": "black"})
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
        # self.patient_gender_entry.configure({"disabledbackground": "white"})
        # self.patient_gender_entry.configure({"disabledforeground": "black"})
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
        # self.patient_age_entry.configure({"disabledbackground": "white"})
        # self.patient_age_entry.configure({"disabledforeground": "black"})
        self.patient_age_entry.grid(row=0, column=c_idx)
        c_idx += 1
        # tk.Label(info_frame, text=PATIENT_DOB, font=WIDGET_FONT).grid(row=2, column=4, padx=(200, 0))
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
        # self.patient_dob_entry.configure({"disabledbackground": "white"})
        # self.patient_dob_entry.configure({"disabledforeground": "black"})
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
        # self.patient_occ_entry.configure({"disabledbackground": "white"})
        # self.patient_occ_entry.configure({"disabledforeground": "black"})
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
        # self.patient_martial_s_entry.configure({"disabledbackground": "white"})
        # self.patient_martial_s_entry.configure({"disabledforeground": "black"})
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
        # self.patient_contact_entry.configure({"disabledbackground": "white"})
        # self.patient_contact_entry.configure({"disabledforeground": "black"})
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
        # , pady=(10, 0))
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
        # Create a variable to track the value of group of radio buttons.
        self.case_type_var = tk.StringVar(symptoms_info_frame, "1")

        # Loop is used to create multiple Radio buttons
        # rather than creating each button separately
        for (text, value) in CASE_TYPE_DICT.items():
            tk.Radiobutton(symptoms_info_frame, text=text, variable=self.case_type_var,
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
                                         r_idx, 5,  # num of columns in the label frame
                                         NUM_OF_MEDICAL_INFO_ENTRIES)
        r_idx += 1

        end_frame = tk.Frame(self.frame)
        end_frame.grid(row=r_idx, column=0, sticky='w', pady=(10, 0), padx=(5, 0))

        c_idx = 0
        tk.Label(end_frame, text=INVESTIGATION, font=WIDGET_FONT).grid(row=0,
                                                                       column=c_idx,
                                                                       padx=(0, 5), pady=(0, 5)
                                                                       )
        c_idx += 1
        self.patient_investigation_entry = CustomText(end_frame, max_len=50, alpha=True,
                                                      digit=True,
                                                      special_char=True,
                                                      space_allowed=True,
                                                      width=40, height=3,
                                                      font=WIDGET_FONT
                                                      )
        self.patient_investigation_entry.grid(row=0, column=c_idx, padx=(0, 10))
        c_idx += 1

        tk.Label(end_frame, text=RECORD_DATE, font=WIDGET_FONT).grid(row=0,
                                                                     column=c_idx)
        c_idx += 1
        self.record_date_entry = CustomEntry(end_frame, ENTRY_MAX_LEN_10, alpha=False,
                                             digit=True,
                                             special_char=False, space_allowed=True, width=10,
                                             font=WIDGET_FONT,
                                             state='disabled')
        # datetime object containing current date and time
        self.record_date_entry.set_text(datetime.now().strftime("%Y-%m-%d"))
        self.record_date_entry.grid(row=0, column=c_idx, padx=(0, 10))
        c_idx += 1

        tk.Label(end_frame, text=NEXT_DATE, font=WIDGET_FONT).grid(row=0,
                                                                   column=c_idx)
        c_idx += 1

        self.next_date_entry = CustomEntry(end_frame, ENTRY_MAX_LEN_10, alpha=False,
                                           digit=True,
                                           special_char=False, space_allowed=True, width=10,
                                           font=WIDGET_FONT
                                           )
        # TODO: Add 15 days to the current date
        self.next_date_entry.set_text(datetime.now().strftime("%Y-%m-%d"))
        self.next_date_entry.grid(row=0, column=c_idx, padx=(0, 10))
        c_idx += 1

        tk.Label(end_frame, text=TOTAL_AMOUNT, font=WIDGET_FONT).grid(row=0,
                                                                      column=c_idx, padx=(0, 10))
        c_idx += 1

        self.total_amount_entry = CustomEntry(end_frame, ENTRY_MAX_LEN_6, alpha=False,
                                              digit=True,
                                              special_char=False, space_allowed=False, width=6,
                                              font=WIDGET_FONT
                                              )
        self.total_amount_entry.grid(row=0, column=c_idx, padx=(0, 10))

        tk.Button(end_frame, text=SAVE_RECORD, font=WIDGET_FONT,
                  command=lambda: self.save_medical_record_event_action()).grid(row=1,
                                                                                column=1, pady=(50, 0),
                                                                                sticky='e')

        tk.Button(end_frame, text=GENERATE_PRESCRIPTION, font=WIDGET_FONT,
                  command=lambda: self.generate_prescription_event_action()).grid(row=1,
                                                                                  column=3, pady=(50, 0),
                                                                                  sticky='e')
