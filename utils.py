import tkinter as tk
import re
from constant import *


def validate_email_address(email_address):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # pass the regular expression
    # and the string into the fullmatch() method
    if re.fullmatch(regex, email_address):
        return True
    else:
        return False


def show_password_event_action(entry, button):
    if entry.cget('show') == '':
        entry.config(show='*')
        button.config(text=SHOW_PASSWORD_LABEL)
    else:
        entry.config(show='')
        button.config(text='Hide Password')


def set_grid_row_column_configure(frame, num_rows, num_columns):
    '''
    for row_idx in range(num_rows):
        tk.Grid.rowconfigure(frame, index=row_idx, weight=1)

    for col_idx in range(num_columns):
        tk.Grid.columnconfigure(frame, index=col_idx, weight=1)
    '''