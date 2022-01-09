import tkinter as tk
from frames.base_frame import BaseFrame
from frames.custom_entry import CustomEntry
from constant import *
from utils import *
from tkinter import messagebox
from global_app_data import GlobalAppData
'''
                                    Doctor Space Login
                    Please Enter your username(email) and password

                    Username/Email

                    Password                    show password

                                                Forget password
                                Login
                                New User Registration       

'''
HEADING_LABEL_1 = "Please Enter your Email/Username and Password"
FORGET_PASSWORD_BUTTON = "Forget Password"
LOGIN_BUTTON = "Login"
REGISTER_BUTTON = "New User Registration"


# xFrame class is suppose to create a custom Base TK frame from the root object.
# This Frame has all the login frame widgets (instead of directly parent having it)
class LoginFrame:

    # Function which should be called whenever we enter this frame
    def frame_reload(self, full_reload):
        if full_reload:
            self.email_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

        self.password_entry.config(show='*')
        self.show_password.config(text=SHOW_PASSWORD_LABEL)

    # Frame/Page to go once user clicks on login
    def login_event_action(self):

        msg = ""
        if 0 == len(self.email_entry.get_text()):
            msg = "Please fill Email Entry and try again"
        elif 0 == len(self.password_entry.get_text()):
            msg = "Please fill Password Entry and try again"
        else:
            if not validate_email_address(self.email_entry.get_text()):
                msg = ERROR_INVALID_EMAIL

        if 0 != len(msg):
            messagebox.showerror(ERROR_BOX_TITLE, msg)
            return

        result = self.db_controller.check_email_exists(self.email_entry.get_text())
        # First entry indicates if error or not while checking email list, if true
        # second entry indicate if user exist or not.
        if not result[0]:
            messagebox.showerror(ERROR_BOX_TITLE, ERROR_CHECKING_EMAIL_ADDRESS)
        elif not result[1]:
            messagebox.showerror(ERROR_BOX_TITLE, ERROR_EMAIL_USER_NOT_EXIST)
        else:
            # True indicates that user exists, now check the password field and make sure that
            # password matches, 3rd entry in the result tuple holds the complete row of the doctor information
            # 2nd entry gives the password.
            if self.password_entry.get_text() != result[2][2]:
                messagebox.showerror(ERROR_BOX_TITLE, ERROR_PASSWORD_NOT_MATCHING)
                return

            # Save the doctor information in the global data structure for quick use across Application frames.
            GlobalAppData.set_logged_in_doc_info(result[2])
            print("logged in ", GlobalAppData.get_logged_in_doc_info())

            # Enter the next frame which is entry frame.
            self.frame.enter_next_frame(1, True)

    # Frame/Page to go once user clicks on new user registration
    def register_doc_event_action(self):
        self.frame.enter_next_frame(2, True)

    # Init the frame class.
    def __init__(self, root, ws, hs, db_controller):

        self.db_controller = db_controller

        # Create a base frame object which has parent as main root window.
        self.frame = BaseFrame(root)

        '''
        for n in range(5):
            parent.columnconfigure(n, weight=1)
            parent.rowconfigure(n, weight=1)
        '''

        # Row 0
        tk.Label(self.frame, text=DOC_SPACE, font=WIDGET_FONT_1).grid(
                 row=0, column=0, sticky='w')
        tk.Label(self.frame, text=DOC_SPACE_HEADING_LABEL_0, font=HEADING_FONT).grid(
                 row=0, column=1, columnspan=2, pady=(hs/6, 10))

        # Row 1
        tk.Label(self.frame, text=HEADING_LABEL_1, font=HEADING_FONT_1).grid(
                 row=1, column=1, columnspan=2, pady=(10, 30))

        # Row 2
        tk.Label(self.frame, text=EMAIL_LABEL, font=WIDGET_FONT).grid(
                 row=2, column=0, padx=(ws/5, 30))
        self.email_entry = CustomEntry(self.frame, ENTRY_MAX_LEN_30, alpha=True,
                                       digit=True, special_char=True, width=30, font=WIDGET_FONT)
        self.email_entry.grid(row=2, column=1, columnspan=2)

        # Row 3
        tk.Label(self.frame, text=PASSWORD_LABEL, font=WIDGET_FONT).grid(
                 row=3, column=0, padx=(ws/5, 30))
        self.password_entry = CustomEntry(self.frame, ENTRY_MAX_LEN_10, alpha=True, digit=True,
                                          special_char=True, show="*", width=30, font=WIDGET_FONT)
        self.password_entry.grid(row=3, column=1, columnspan=2)
        self.show_password = tk.Button(self.frame, text=SHOW_PASSWORD_LABEL,
                                       command=lambda: show_password_event_action(
                                       self.password_entry, self.show_password), font=WIDGET_FONT)

        self.show_password.grid(row=3, column=4)

        # Row 4
        tk.Button(self.frame, text=FORGET_PASSWORD_BUTTON, font=WIDGET_FONT).grid(row=4, column=4)

        # Row 5
        tk.Button(self.frame, text=LOGIN_BUTTON, command=lambda: self.login_event_action(),
                  font=WIDGET_FONT).grid(
                  row=5, column=2, sticky='w', padx=70)

        # Row 6
        tk.Button(self.frame, text=REGISTER_BUTTON, command=lambda: self.register_doc_event_action(),
                  font=WIDGET_FONT).grid(row=6, column=2, sticky='w')
