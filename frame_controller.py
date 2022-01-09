import tkinter as tk
from tkinter import ttk
from frames.login_frame import LoginFrame
from frames.entry_frame import EntryFrame
from frames.patient_frame import PatientFrame
from frames.medical_record_frame import MedicalRecordFrame
from frames.doc_registration_frame import DocRegistrationFrame
from utils import *


# Frame Controller class which is will create and initialize all the frames which is needed
# in the application.
class FrameController:

    # Method to start the application start up frame.
    def start_app_frame(self):
        print ("FrameController:start_app_frame: Starting Doc Space App...")
        self.login_frame.frame.display_frame()
        self.root.mainloop()

    # Init the frame controller class.
    def __init__(self, root, db_controller):

        self.root = root
        self.db_controller = db_controller

        # get screen width and height
        ws = self.root.winfo_screenwidth()  # width of the screen
        hs = self.root.winfo_screenheight()  # height of the screen

        w = ws - 100  # width for the Tk root
        h = hs - 200  # height for the Tk root

        # set the dimensions of the screen and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (ws, hs, 0, 0))
        #self.root.geometry('+%d+%d' % (w, h))
        #self.root.geometry('%dx%d' % (ws, hs))
        #self.root.resizable(True, True)
        root.state('zoomed')
        print ("FrameController:Init: window width ", ws, "window height ", hs)
        set_grid_row_column_configure(self.root, 1, 1)

        '''
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        canvas = tk.Canvas(self.main_frame, background="blue")

        yscrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=canvas.yview)
        xscrollbar = ttk.Scrollbar(self.main_frame, orient=tk.HORIZONTAL, command=canvas.xview)

        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        canvas.configure(yscrollcommand=yscrollbar.set)
        canvas.configure(xscrollcommand=xscrollbar.set)

        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.root_frame = tk.Frame(canvas, background='green')
        canvas.create_window((0, 0), window=self.root_frame, anchor='nw')
        
        self.main_frame = tk.Frame(self.root, background='green')
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        self.root_frame = tk.Frame(self.main_frame, background='red')
        self.root_frame.pack(fill=tk.BOTH, expand=1)
        '''
        # create all frames needed in the application.
        self.login_frame = LoginFrame(self.root, ws, hs, self.db_controller)
        self.doc_registration_frame = DocRegistrationFrame(self.root, ws, hs, self.db_controller)
        self.entry_frame = EntryFrame(self.root, ws, hs)
        self.patient_frame = PatientFrame(self.root, ws, hs)
        self.medical_record_frame = MedicalRecordFrame(self.root, ws, hs)

        # Add back and next frames for each applicable frames created in last step.
        # From Login Frame we can go next to:
        # Main Entry frame after successful login.
        # Doctor Registration frame to register.
        # There is no back frame.
        #self.login_frame.frame.add_next_frame(self.entry_frame)
        self.login_frame.frame.add_next_frame(self.medical_record_frame)
        self.login_frame.frame.add_next_frame(self.doc_registration_frame)

        # From Doc Registration frame we don't go to any next frame.
        # We can go back to login frame.
        self.doc_registration_frame.frame.add_back_frame(self.login_frame)

        # From Entry Frame we can go next to:
        # Patient frame to check the patient details.
        # We can go back to login frame
        self.entry_frame.frame.add_next_frame(self.patient_frame)
        self.entry_frame.frame.add_back_frame(self.login_frame)

        # From Patient Frame we can go next to:
        # Medical record frame
        # We can go back to login frame or entry frame
        self.patient_frame.frame.add_next_frame(self.medical_record_frame)
        self.patient_frame.frame.add_back_frame(self.login_frame)
        self.patient_frame.frame.add_back_frame(self.entry_frame)

        # From Patient Frame we can go next to:
        # TODO: -------
        # We can go back to login frame or patient frame
        self.medical_record_frame.frame.add_back_frame(self.login_frame)
        self.medical_record_frame.frame.add_back_frame(self.patient_frame)

        print ("FrameController:Init: Frame Controller created successfully")