"""Contains the SignUpTk class"""

import Models.Validator as Validator
from tkinter import Tk, PhotoImage, Text, messagebox, ttk, END
import sys
import Views.Styling.ct_tk as ct_tk
sys.path.append('..')


class SignUpTk(Tk):
    """Represents a SignUpTk popup window within the LoginFrame object"""

    def __init__(self, controller):
        Tk.__init__(self)
        ct_tk.CT_Tk(self, 'Campus Thrift')
        self.controller = controller

        self.frame_header = ttk.Frame(self)
        self.frame_header.pack()
        self.frame_content = ttk.Frame(self)
        self.frame_content.pack()

        self.logo_photo = PhotoImage(
            master=self.frame_header, file='psu_logo.png')
        self.sign_up_photo = PhotoImage(
            master=self.frame_header, file='sign_up.png')

        ttk.Label(self.frame_header, image=self.logo_photo).grid(
            row=0, column=0)
        ttk.Label(self.frame_header, image=self.sign_up_photo).grid(
            row=0, column=1)
        ttk.Label(self.frame_header, image=self.logo_photo).grid(
            row=0, column=2)

        ttk.Label(self.frame_content, text='Username:').grid(
            row=1, column=2, pady=10, sticky='w')
        self.entry_name = ttk.Entry(
            self.frame_content, width=30, font=('Arial', 10))
        self.entry_name.grid(row=2, column=2)

        ttk.Label(self.frame_content, text='EMail:').grid(
            row=3, column=2, pady=10, sticky='w')
        self.entry_email = ttk.Entry(
            self.frame_content, width=30, font=('Arial', 10))
        self.entry_email.grid(row=4, column=2)

        ttk.Label(self.frame_content, text='Password:').grid(
            row=5, column=2, pady=10, sticky='w')
        self.entry_password = ttk.Entry(
            self.frame_content, width=30, font=('Arial', 10), show='*')
        self.entry_password.grid(row=6, column=2)

        ttk.Label(self.frame_content, text='Confirm Password:').grid(
            row=7, column=2, pady=10, sticky='w')
        self.entry_confirm_pw = ttk.Entry(
            self.frame_content, width=30, font=('Arial', 10), show='*')
        self.entry_confirm_pw.grid(row=8, column=2)

        ttk.Label(self.frame_content, text='Bio:').grid(
            row=9, column=2, pady=10, sticky='w')
        self.entry_bio = Text(
            self.frame_content, width=30, height=10, font=('Arial', 10))
        self.entry_bio.grid(row=10, column=2)

        ttk.Button(self.frame_content, text='Submit',
                   command=self.try_signup).grid(row=11, column=2, pady=20)

    def try_signup(self):
        """Attempts to create new account information based on the given user input"""

        if (self.validate_input()):
            signup_account_info = {'name': self.entry_name.get(), 'email': self.entry_email.get(),
                                   'password': self.entry_password.get(), 'bio': self.entry_bio.get("1.0", END)}

            self.controller.try_signup(signup_account_info)
            self.destroy()
        else:
            self.entry_password.delete(0, len(self.entry_password.get()))
            self.entry_confirm_pw.delete(0, len(self.entry_confirm_pw.get()))

    # Untested -- validate_input()

    def validate_input(self):
        """Check user input to validate account fields"""

        return (
            Validator.validate_name(self.entry_name.get()) and
            Validator.validate_email(self.entry_email.get()) and
            Validator.validate_password(self.entry_password.get(), self.entry_confirm_pw.get()) and
            Validator.validate_bio(self.entry_bio.get("1.0", "end-1c"))
        )
