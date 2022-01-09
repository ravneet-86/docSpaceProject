import tkinter as tk

ALLOWED_SPECIAL_CHAR = '[@_!$%^&*()<>?/\|}{~:]#-+;:?'


class CustomText(tk.Text):

    # Initialize the class
    def __init__(self, master=None, max_len=10, alpha=True, digit=False, special_char=False,
                 space_allowed=False, **kwargs):
        self.max_len = max_len
        self.alpha = alpha
        self.digit = digit
        self.special_char = special_char
        self.space_allowed = space_allowed

        self.var = tk.StringVar()

        tk.Text.__init__(self, master, **kwargs)
        self.bind('<KeyRelease>', self.check)

    def update_text(self, str_len, text_str):
        print("updating str ", str_len, "new str",  self.get('1.0', 'end')[:str_len])
        self.delete("0.0", "end")
        self.insert("end", text_str[:str_len])

    # Check is called each time a new character is entered, check if the enter character or the string
    # we have up till now is valid or not.
    def check(self, *args):

        print('CustomText: inside check a key is pressed: ', self.get('1.0', 'end'))

        try:

            # We can have length less than 1 for the case where backspace is given and it was the last
            # character in the Entry box. So it is ok to ignore this case.
            if len(self.get('1.0', 'end')) < 1:
                print("CustomText:check: Cannot process text with length its ok", len(self.get('1.0', 'end')),
                      " less than 1 text ", self.get('1.0', 'end'))
                return

            # Remove any trailing or preceding new lines
            #text_str = self.get('1.0', 'end')[:(len(self.get('1.0', 'end')) - 1)]
            text_str = self.get('1.0', 'end').strip('\n')

            if len(text_str) < 1:
                return

            # Check if alphabets are allowed, every time check the latest element
            char = text_str[len(text_str) - 1]

            print('char is :', char, " max len ", self.max_len, " str ", text_str, " len ", len(text_str))
            # if the latest character is newline we don't need to process anything
            if '\n' == char:
                print('newline just return')
                return

            # Flag which is set in case we want to update the text box and remove this char if it is
            # not allowed. If char is allowed no update is needed.
            update_needed = False
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
                if not self.alpha:
                    update_needed = True
            elif '0' <= char <= '9':
                if not self.digit:
                    update_needed = True
            elif char in ALLOWED_SPECIAL_CHAR:
                # This is a special character, first check if space is allowed or not
                if char == ' ':
                    if not self.space_allowed:
                        update_needed = True
                elif not self.special_char:
                    update_needed = True
            else:
                # We don't need to process all other special characters
                return

            print('update needed ', update_needed, "max_len ", self.max_len, "char ",
                  text_str[len(text_str)-1])

            if update_needed:
                self.update_text(len(text_str) - 1, text_str)

            newline_cnt = text_str.count('\n')
            if (len(text_str) - newline_cnt) > self.max_len:
                self.update_text(self.max_len + newline_cnt, text_str)

        except Exception as e:
            print("CustomText:check: Exception received while processing text ", e)
            print("CustomText:check: Cannot process text length ", len(self.get('1.0', 'end')),
                  " text ", self.get('1.0', 'end'))

    # Get the text for this Entry
    def get_text(self):
        text = self.get('1.0', 'end').strip()
        text = text.strip('\n')
        return text

    # Get the text for this Entry
    def set_text(self, text):
        #First delete all old text.
        self.delete(0, "end")
        self.insert("end", text)
