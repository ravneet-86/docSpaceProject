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
                        Search Remedy  box to display result

'''
ENTER_SYMPTOM = "Enter symptom"


# xFrame class is suppose to create a custom Base TK frame from the root object.
# This Frame has the information to search the remedies for input symptoms.
# This performs a web scraping on materia medica and repository to get the
# matching medicinal remedies
class SearchRemedyFrame:

    # Function which should be called whenever we enter this frame
    def frame_reload(self, full_reload):

        try:
            if full_reload:
                self.search_remedy_entry.delete(0, 'end')
                self.search_result_list_box.delete(0, tk.END)
        except Exception as e:
            print("SearchRemedyFrame::frame_reload:: Exception loading doctor info ", e)

    def list_box_double_click_event_action(self, event):
        print ("WORK IN PROGRESS")

    def update_search_remedy_list(self):
        input_search_string = self.search_remedy_entry.get_text()
        print ("Getting remedies .", input_search_string)
        sources = self.db_controller.get_db_tables()

        print("processing input string ", input_search_string)

        status = True
        # Delete existing results.
        self.search_result_list_box.delete(0, tk.END)

        # Run over all the sources and search the remedy in each of the source
        # source is like a dedicated Table in the data base.
        for source in sources:
            cols = self.db_controller.get_col_names(source)
            print ("Cols for source ", source, " col ", cols)

            remedy_df = None

            # Currently we always query the database
            if 0 != len(input_search_string):
                _, remedy_df = self.db_controller.db_remedy_results(source, input_search_string, cols)
            else:
                print ("Input string is empty")
                self.search_result_list_box.delete(0, tk.END)
                return

            self.search_result_list_box.insert(tk.END, source)
            self.search_result_list_box.insert(tk.END, "\n")

            if remedy_df is None:
                print ("empty df for ", source)
                self.search_result_list_box.insert(tk.END, "\n---------End--------\n")
                continue

            for index, row in remedy_df.iterrows():
                self.search_result_list_box.insert(tk.END, row[0])
                # self.search_result_list_box.insert(tk.END, "\n")
                '''
                for col in row:
                    self.search_result_list_box.insert(tk.END, col)
                    self.search_result_list_box.insert(tk.END, "\n")
                '''
            self.search_result_list_box.insert(tk.END, "\n---------End--------\n")
    # Enter the first back frame which is the entry frame.
    def log_out_event_action(self):
        self.frame.enter_back_frame(1, False)

    # Init the frame class.
    def __init__(self, root, ws, hs, db_controller, remedy_searcher):
        self.db_controller = db_controller
        self.remedy_searcher = remedy_searcher

        # Create a base frame object which has parent as main root window.
        self.frame = BaseFrame(root)

        header_frame = tk.Frame(self.frame)

        tk.Label(header_frame, text=DOC_SPACE, font=WIDGET_FONT_1).grid(
            row=0, column=0)
        tk.Button(header_frame, text=LOG_OUT,
                  command=lambda: self.log_out_event_action(), font=WIDGET_FONT_1).grid(
            row=0, column=1, padx=(ws - 280, 0))
        header_frame.grid(row=0, column=0, sticky='w', pady=(hs / 10.4, 0))

        field_frame = tk.Frame(self.frame)

        row_idx = 0
        self.enter_key_label = tk.Label(field_frame, text=ENTER_SYMPTOM, font=HEADING_FONT)
        self.enter_key_label.grid(row=row_idx, column=0, pady=(0, 40))
        row_idx += 1

        # self.patient_search_str = tk.StringVar()
        # self.patient_search_str.trace("w", lambda name, index, mode: self.update_search_patient_list())
        self.search_remedy_entry = CustomEntry(field_frame, ENTRY_MAX_LEN_20, alpha=True, digit=False,
                                              special_char=False, space_allowed=True,
                                              callback_fun=None,
                                              width=30, font=WIDGET_FONT)

        self.search_remedy_entry.grid(row=row_idx, column=0, pady=(0, 20))

        tk.Button(field_frame, text=SEARCH,
                  command=lambda: self.update_search_remedy_list(), font=WIDGET_FONT_1).grid(
            row=row_idx, column=1, padx=(0, 20))

        row_idx += 1

        # Row 2 45
        self.search_result_list_box = tk.Listbox(field_frame, font=WIDGET_FONT, width=100, height=15)
        self.search_result_list_box.bind("<Double-1>", self.list_box_double_click_event_action)
        self.search_result_list_box.grid(row=row_idx, column=0, rowspan=24, pady=(0, 10))


        field_frame.grid(row='1', column='0', pady=(50, 0))
