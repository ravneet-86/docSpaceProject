import tkinter as tk
from utils import *
from tkinter import ttk


# Base Frame class is suppose to create a TK frame from the root object.
class BaseFrame(tk.Frame):

    # Method to display the frame
    def display_frame(self, use_pack=True):
        if not use_pack:
            self.grid(row=0, column=0, sticky='nsew')
        else:
            self.main_frame.pack(fill=tk.BOTH, expand=1)

    # Method to go to next frame from this frame.
    def enter_next_frame(self, n_idx, full_reload, use_pack=True):
        if not use_pack:
            self.grid_remove()
        else:
            self.main_frame.pack_forget()

        try:
            self.next_frames[n_idx].frame_reload(full_reload)

            if not use_pack:
                self.next_frames[n_idx].frame.grid(row=0, column=0)
            else:
                #
                self.next_frames[n_idx].frame.main_frame.pack(fill=tk.BOTH, expand=1)
                self.next_frames[n_idx].frame.main_frame.wait_visibility()
        except Exception as e:
            print("LoginFrame: Out of bound encountered ", n_idx, " using 0, exception: ", e)
            self.next_frames[0].grid(row=0, column=0)

    # Method to go to back frame from this frame.
    def enter_back_frame(self, n_idx, full_reload, use_pack=True):
        if not use_pack:
            self.grid_remove()
        else:
            self.main_frame.pack_forget()

        try:
            self.back_frames[n_idx].frame_reload(full_reload)

            if not use_pack:
                self.back_frames[n_idx].frame.grid(row=0, column=0)
            else:
                self.back_frames[n_idx].frame.main_frame.pack(fill=tk.BOTH, expand=1)
        except Exception as e:
            print("LoginFrame: Out of bound encountered ", n_idx, " using 0, exception: ", e)
            self.back_frames[0].grid(row=0, column=0)

    # Method to add the next frame from this frame can go to. There can be multiple next frames.
    def add_next_frame(self, frame):
        self.next_frames.append(frame)

    # Method to go to the back frame from this frame. There can be only one back frame.
    def add_back_frame(self, frame):
        self.back_frames.append(frame)

    def update(self):
        "Update the canvas and the scrollregion"
        self.update_idletasks()

    def fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"
        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)

    # Init the Base frame class.
    def __init__(self, root):

        self.root = root

        # Each Base frame class has a main frame within which a canvas and scroll bar
        # is kept.
        # This main frame is the frame which is destroyed once user clicks to go on next
        # frame. This is regenerated once this frame is entered.
        self.main_frame = tk.Frame(self.root)
        #self.main_frame.pack(fill=tk.BOTH, expand=1)

        self.canvas = tk.Canvas(self.main_frame) #, highlightbackground="red", highlightcolor ="yellow")

        yscrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        xscrollbar = ttk.Scrollbar(self.main_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)

        xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.canvas.configure(yscrollcommand=yscrollbar.set)
        self.canvas.configure(xscrollcommand=xscrollbar.set)

        #self.canvas.bind('<Configure>', lambda e: self.canvas.
        #                                configure(scrollregion=self.canvas.bbox("all")))

        #canvas.bind('<Configure>', self.fill_canvas)

        '''
        self.root_frame = tk.Frame(canvas, background='green')
        canvas.create_window((0, 0), window=self.root_frame, anchor='nw')

        self.main_frame = tk.Frame(self.root, background='green')
        self.main_frame.pack(fill=tk.BOTH, expand=1)

        self.root_frame = tk.Frame(self.main_frame, background='red')
        self.root_frame.pack(fill=tk.BOTH, expand=1)
        '''
        # Basic objects needed by a frame can be moved to base class later if data structure increases.
        # This is the frame object which has parent as main root window.
        #tk.Frame.__init__(self, root, background='yellow')
        # This is frame is created inside the canvas, This is a hack to allow scroll
        # on any element we add inside this frame.
        # All widgets will be added within this frame.
        tk.Frame.__init__(self, self.canvas)
        self.windows_item = self.canvas.create_window((0, 0), window=self, anchor='nw')

        self.canvas.bind('<Configure>', lambda e: self.canvas.
                         configure(scrollregion=self.canvas.bbox(self.windows_item)))

        '''
        for row_idx in range(1):
            tk.Grid.rowconfigure(self, index=row_idx, weight=1)

        for col_idx in range(1):
            tk.Grid.columnconfigure(self, index=col_idx, weight=1)
        '''
        # Initialize the list of back frame to this/current frame,
        # this would be set by the caller explicitly if required.
        # Note 0 index is always used by current frame object.
        self.back_frames = []
        self.back_frames.append(self)

        # Initialize the list of next frames with this/current frame,
        # this would be set by the caller explicitly if required.
        # Note 0 index is always used by current frame object.
        self.next_frames = []
        self.next_frames.append(self)


