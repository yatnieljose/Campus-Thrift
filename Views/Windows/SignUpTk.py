"""Contains the SignUpTk class"""

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

        ttk.Label(self.frame_content, text='Full Name:').grid(
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

        # check username integrity (6-16 characters)
        if len(self.entry_name.get()) < 6:
            messagebox.showinfo(title='UsernameTooShort',
                                message="Username is too short. Username must be between 6 and 16 characters.")
            return False

        if len(self.entry_name.get()) > 16:
            messagebox.showinfo(title="UsernameTooLong",
                                message="Username is too long. Username must be between 6 and 16 characters.")
            return False

        # check email integrity (conforms to acceptable email format)

        # split into prefix and domain, separated by @
        # check if more than one @
        email_split = self.entry_email.get().split("@")
        if len(email_split) != 2:
            self.email_failure_message()
            return False
        email_prefix = email_split[0]
        email_domain = email_split[1]

        # validate prefix by name length and type of characters allowed
        if not (1 <= len(email_prefix) <= 256):
            self.email_failure_message()
            return False

        # validate prefix ends with alphanumeric character
        if not email_prefix[-1].isalnum():
            self.email_failure_message()
            return False

        # validate every character in prefix is alphanumeric, underscore (_), period(.), or dash(-)
        for c in email_prefix:
            if not (c.isalnum() or c == '_' or c == '.' or c == '-'):
                self.email_failure_message()
                return False

        # split domain by .
        domain_split = email_domain.split(".")
        if (len(domain_split) != 2):
            self.email_failure_message()
            return False
        domain_prefix = domain_split[0]
        domain_suffix = domain_split[1]

        # validate domain prefix
        if not (1 <= len(domain_prefix) <= 64):
            self.email_failure_message()
            return False

        if not domain_prefix[-1].isalnum():
            self.email_failure_message()
            return False

        for c in domain_prefix:
            if not (c.isalnum() or c == "-"):
                self.email_failure_message()
                return False

        # validate domain suffix
        if not (1 <= len(domain_suffix) <= 64):
            self.email_failure_message()
            return False

        if not domain_suffix[-1].isalnum():
            self.email_failure_message()
            return False

        for c in domain_suffix:
            if not (c.isalnum() or c == "-"):
                self.email_failure_message()
                return False

        # check password integrity
        if len(self.entry_password.get()) < 6:
            messagebox.showinfo(title="WrongPasswordFormat",
                                message="Password must be at least 6 characters.")
            return False

        if len(self.entry_password.get()) > 64:
            messagebox.showinfo(title="LongPasswordFormat",
                                message="Password must be 64 characters maximum.")

        # check password match
        if self.entry_password.get() != self.entry_confirm_pw.get():
            messagebox.showinfo(title="PasswordMismatchFormat",
                                message="Passwords do not match.")
            return False

         # check bio integrity (max 256 but no minimum, can be left blank)
         # !!! We need .get() but for a Text widget
        if len(self.entry_bio.get("1.0", "end-1c")) > 256:
            messagebox.showinfo(title="LongBioFormat",
                                message="Bio must be 256 characters maximum.")

        return True

    def email_failure_message(self):
        """Displays a message box indicating that the email format is incorrect"""
        messagebox.showinfo(title="WrongEmailFormat",
                            message="Email format incorrect.")
