import tkinter as tk
from frames.base_frame import BaseFrame
from constant import *
from utils import *
from frames.custom_entry import CustomEntry
from tkinter import messagebox

'''
                                    Doctor Registration
                    * are mandatory fields.

                    Name
                    
                    Email

                    Password

                    Confirm Password
                    
                    Contact Number
                    
                    Mobile Number
                    
                    Clinic Name
                    
                    Clinic Address
                    
                                    Register        Go Back          Reset
'''

DOCTOR_REGISTRATION = "Doctor Registration"
MANDATORY_FIELDS = "* are mandatory fields"
NAME = "Name *"
EMAIL = "Email *"
PASSWORD = "Password *"
CONFIRM_PASSWORD = "Confirm Password *"
CONTACT_NUMBER = "Contact Number *"
MOBILE_NUMBER = "Mobile Number"
CLINIC_NAME = "Clinic Name "
CLINIC_ADDRESS = "Clinic Address"
REGISTER = "Register"
CANCEL = "Go Back"
RESET = "Reset"


# xFrame class is suppose to create a custom Base TK frame from the root object.
# This Frame has all the login frame widgets (instead of directly parent having it)
class DocRegistrationFrame:

    # Function which should be called whenever we enter this frame
    def frame_reload(self, full_reload):

        if full_reload:
            self.name_entry.delete(0, 'end')
            self.email_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
            self.confirm_password_entry.delete(0, 'end')
            self.mobile_number_entry.delete(0, 'end')
            self.contact_number_entry.delete(0, 'end')
            self.clinic_name_entry.delete(0, 'end')
            self.clinic_address_entry.delete(0, 'end')

        self.password_entry.config(show='*')
        self.show_password.config(text=SHOW_PASSWORD_LABEL)

        # TODO make the focus on first entry i.e name_entry

    # Just reload the frame in case reset is triggered
    def reset_event_action(self):
        self.frame_reload(True)

    # Method to perform the registration step when user clicks on register.
    # this will make a database entry.
    def register_event_action(self):
        # Step 1: Validate the email address
        if not validate_email_address(self.email_entry.get_text()):
            messagebox.showerror(ERROR_BOX_TITLE, ERROR_INVALID_EMAIL)
            return

        msg = ""
        # Step 2: Check all the mandatory items are filled correctly.
        if 0 == len(self.name_entry.get_text()):
            msg = "Please fill Name Entry and try again"
        elif 0 == len(self.email_entry.get_text()):
            msg = "Please fill Email Entry and try again"
        elif 0 == len(self.password_entry.get_text()):
            msg = "Please fill Password Entry and try again"
        elif 0 == len(self.confirm_password_entry.get_text()):
            msg = "Please fill Confirm Password Entry and try again"
        elif 0 == len(self.contact_number_entry.get_text()):
            msg = "Please fill Contact Number Entry and try again"
        # Step 3: make sure that password and confirm password are same
        elif self.password_entry.get_text() != self.confirm_password_entry.get_text():
            msg = "Password and Confirm Password not matching \n Please check and try again"

        if 0 != len(msg):
            messagebox.showerror(ERROR_BOX_TITLE, msg)
            return

        # Step 4: Make sure email address doesn't already exist
        result = self.db_controller.check_email_exists(self.email_entry.get_text())
        if not result[0]:
            messagebox.showerror(ERROR_BOX_TITLE, ERROR_CHECKING_EMAIL_ADDRESS)
        elif result[1]:
            messagebox.showerror(ERROR_BOX_TITLE, EMAIL_ADDRESS_ALREADY_EXIST)
        else:
            # Step 5: All information is fine now add the entry in data base
            value = (self.name_entry.get_text(), self.email_entry.get_text(), self.password_entry.get_text(),
                     self.contact_number_entry.get_text(), self.mobile_number_entry.get_text(),
                     self.clinic_name_entry.get_text(), self.clinic_address_entry.get_text())

            values = [value]
            if self.db_controller.db_insert_doctor_info(values):
                messagebox.showinfo(MESSAGE_BOX_TITLE, REGISTRATION_SUCCESS)

                # TODO: Create a new table for this doctor now.

                # Go back to the back frame which is the login frame for user to login now.
                self.frame.enter_back_frame(1, True)
            else:
                # Failure..
                messagebox.showerror(ERROR_BOX_TITLE, REGISTRATION_FAILURE)

    def go_back_even_action(self):
        # Go back to the login page, reload the contents.
        self.frame.enter_back_frame(1, True)

    # Init the frame class.
    def __init__(self, root, ws, hs, db_controller):

        self.db_controller = db_controller

        # Create a base frame object which has parent as main root window.
        self.frame = BaseFrame(root)

        m_r_idx = 0

        tk.Label(self.frame, text=DOC_SPACE, font=WIDGET_FONT_1).grid(
            row=m_r_idx, column=0, sticky='w')
        tk.Label(self.frame, text=DOCTOR_REGISTRATION, font=HEADING_FONT).grid(
            row=m_r_idx, column=1, columnspan=3, ipadx=400, pady=(hs / 6, 10))
        m_r_idx += 1

        tk.Label(self.frame, text=MANDATORY_FIELDS, font=WIDGET_FONT_SMALL).grid(
            row=m_r_idx, column=1, ipadx=400, columnspan=3)
        m_r_idx += 1

        row_idx = 0
        # Create a separate frame for the fields.
        field_frame = tk.Frame(self.frame)
        field_c_idx = 5
        entry_c_idx = 6
        field_pady = 10

        tk.Label(field_frame, text=NAME, font=WIDGET_FONT).grid(
            row=row_idx, column=field_c_idx, sticky='w', pady=(50, field_pady))
        self.name_entry = CustomEntry(field_frame, ENTRY_MAX_LEN_20, alpha=True,
                                      digit=False, special_char=False, space_allowed=True, width=30, font=WIDGET_FONT)
        self.name_entry.grid(row=row_idx, column=entry_c_idx, pady=(20, field_pady))
        row_idx += 1

        tk.Label(field_frame, text=EMAIL, font=WIDGET_FONT).grid(
            row=row_idx, column=field_c_idx, sticky='w', padx=(0, field_pady))
        self.email_entry = CustomEntry(field_frame, ENTRY_MAX_LEN_30, alpha=True,
                                       digit=True, special_char=True, width=30, font=WIDGET_FONT)
        self.email_entry.grid(row=row_idx, column=entry_c_idx, pady=(0, field_pady))
        row_idx += 1

        tk.Label(field_frame, text=PASSWORD, font=WIDGET_FONT).grid(
            row=row_idx, column=field_c_idx, sticky='w', pady=(0, field_pady))
        self.password_entry = CustomEntry(field_frame, ENTRY_MAX_LEN_10, alpha=True, digit=True,
                                          special_char=True, show="*", width=30, font=WIDGET_FONT)
        self.password_entry.grid(row=row_idx, column=entry_c_idx, pady=(0, field_pady))
        self.show_password = tk.Button(field_frame, text=SHOW_PASSWORD_LABEL, font=WIDGET_FONT,
                                       command=lambda: show_password_event_action(self.password_entry,
                                                                                  self.show_password))
        self.show_password.grid(row=row_idx, column=entry_c_idx + 1, padx=(30, 0), pady=(0, field_pady))

        row_idx += 1

        tk.Label(field_frame, text=CONFIRM_PASSWORD, font=WIDGET_FONT).grid(
            row=row_idx, column=field_c_idx, sticky='w', pady=(0, field_pady))
        self.confirm_password_entry = CustomEntry(field_frame, ENTRY_MAX_LEN_10, alpha=True, digit=True,
                                                  special_char=True, show="*", width=30, font=WIDGET_FONT)
        self.confirm_password_entry.grid(row=row_idx, column=entry_c_idx, pady=(0, field_pady))
        row_idx += 1

        tk.Label(field_frame, text=CONTACT_NUMBER, font=WIDGET_FONT).grid(
            row=row_idx, column=field_c_idx, sticky='w', pady=(0, field_pady))
        self.contact_number_entry = CustomEntry(field_frame, ENTRY_MAX_LEN_12, alpha=False,
                                                digit=True, special_char=False, width=30, font=WIDGET_FONT)
        self.contact_number_entry.grid(row=row_idx, column=entry_c_idx, pady=(0, field_pady))
        row_idx += 1

        tk.Label(field_frame, text=MOBILE_NUMBER, font=WIDGET_FONT).grid(
            row=row_idx, column=field_c_idx, sticky='w', pady=(0, field_pady))
        self.mobile_number_entry = CustomEntry(field_frame, ENTRY_MAX_LEN_10, alpha=False,
                                               digit=True, special_char=False, width=30, font=WIDGET_FONT)
        self.mobile_number_entry.grid(row=row_idx, column=entry_c_idx, pady=(0, field_pady))
        row_idx += 1

        tk.Label(field_frame, text=CLINIC_NAME, font=WIDGET_FONT).grid(
            row=row_idx, column=field_c_idx, sticky='w', pady=(0, field_pady))
        self.clinic_name_entry = CustomEntry(field_frame, ENTRY_MAX_LEN_20, width=30, alpha=True,
                                             digit=True, special_char=True, space_allowed=True, font=WIDGET_FONT)
        self.clinic_name_entry.grid(row=row_idx, column=entry_c_idx, pady=(0, field_pady))
        row_idx += 1

        tk.Label(field_frame, text=CLINIC_ADDRESS, font=WIDGET_FONT).grid(
            row=row_idx, column=field_c_idx, sticky='w', pady=(0, field_pady))
        self.clinic_address_entry = CustomEntry(field_frame, ENTRY_MAX_LEN_50, alpha=True,
                                                digit=True, special_char=True, space_allowed=True, width=30,
                                                font=WIDGET_FONT)
        self.clinic_address_entry.grid(row=row_idx, column=entry_c_idx, pady=(0, field_pady))
        row_idx += 1

        field_c_idx = field_c_idx

        tk.Button(field_frame, text=REGISTER, command=lambda: self.register_event_action(), font=WIDGET_FONT).grid(
            row=row_idx, column=field_c_idx)
        field_c_idx += 1

        tk.Button(field_frame, text=CANCEL, font=WIDGET_FONT, command=lambda: self.go_back_even_action()).grid(
            row=row_idx, column=field_c_idx)
        field_c_idx += 1

        tk.Button(field_frame, text=RESET, font=WIDGET_FONT, command=lambda: self.reset_event_action()).grid(
            row=row_idx, column=field_c_idx)

        field_frame.grid(row=m_r_idx, column=2, sticky='w', padx=(350, 0), rowspan=row_idx)
