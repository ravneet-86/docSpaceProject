import tkinter as tk


class CustomEntry(tk.Entry):

    # Initialize the class
    def __init__(self, master=None, max_len=10, alpha=True, digit=False, special_char=False,
                 space_allowed=False, **kwargs):
        self.var = tk.StringVar()
        self.max_len = max_len
        self.alpha = alpha
        self.digit = digit
        self.special_char = special_char
        self.space_allowed = space_allowed

        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.var.trace('w', self.check)

    def update_text(self, str_len):
        self.var.set(self.get()[:str_len])

    # Check is called each time a new character is entered, check if the enter character or the string
    # we have up till now is valid or not.
    def check(self, *args):

        try:
            # We can have length less than 1 for the case where backspace is given and it was the last
            # character in the Entry box. So it is ok to ignore this case.
            if len(self.get()) < 1:
                print("CustomEntry:check: Cannot process text with length ", len(self.get()),
                      "less than 1 text ", self.get(), " var ", self.var)
                return

            # Check if alphabets are allowed, every time check the latest element
            char = self.get()[len(self.get()) - 1]

            # Flag which is set in case we want to update the text box and remove this char if it is
            # not allowed. If char is allowed no update is needed.
            update_needed = False
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
                if not self.alpha:
                    update_needed = True
            elif '0' <= char <= '9':
                if not self.digit:
                    update_needed = True
            else:
                # This is a special character, first check if space is allowed or not
                if char == ' ':
                    if not self.space_allowed:
                        update_needed = True
                elif not self.special_char:
                    update_needed = True

            if update_needed:
                self.update_text(len(self.get()) - 1)

            if len(self.get()) > self.max_len:
                self.update_text(self.max_len)

        except Exception as e:
            print("CustomEntry:check: Exception received while processing text ", e)
            print("CustomEntry:check: Cannot process text length ", len(self.get()),
                  " text ", self.get(), " var ", self.var)

    # Get the text for this Entry
    def get_text(self):
        return self.get().strip()

    # Get the text for this Entry
    def set_text(self, text):
        self.var.set(text)