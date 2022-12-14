"""Contains the ManageAccountTk class"""
from tkinter import Tk, ttk, PhotoImage, messagebox, Text, END
import Views.Styling.ct_tk as ct_tk
import Views.Styling.ct_style as ct_style
from PIL import Image, ImageTk
import Models.Validator as Validator


class ManageAccountTk(Tk):
    """Represents a ManageAccountTk popup window within the TopFrame object"""
    # TopFrame ->

    def __init__(self, controller, traceback):
        Tk.__init__(self)
        ct_tk.CT_Tk(self, "Manage Account")
        self.label_style = ct_style.CT_Style().CT_Label()

        self.controller = controller
        self.account = self.controller.get_current_account()
        self.traceback = traceback

        # important account information
        self.username = None
        self.email = None
        self.password = None
        self.bio = None

        # Create header frame
        self.frame_header = ttk.Frame(self)

        self.logo_photo = PhotoImage(
            master=self.frame_header, file='psu_logo.png')

        ttk.Label(self.frame_header, image=self.logo_photo).grid(
            row=0, column=0)
        ttk.Label(self.frame_header, text="Manage Account").grid(
            row=0, column=1)
        ttk.Label(self.frame_header, image=self.logo_photo).grid(
            row=0, column=2)

        # create content frame
        self.frame_content = ttk.Frame(self)

        # important UI information
        self.lbl_username = None
        self.lbl_email = None
        self.lbl_password = None
        self.lbl_bio = None
        self.btn_edit = None
        self.btn_logout = None

        self.entry_username = None
        self.entry_email = None
        self.entry_bio = None

        # pack into window, pack content into the content frame
        self.frame_header.pack()
        self.frame_content.pack()
        self.pack_content()

    def get_account_details(self):
        """Creates variables representing important account details"""

        self.username = self.account.get_name
        self.email = self.account.get_email
        self.password = self.account.get_password
        self.bio = self.account.get_bio

    def pack_content(self):
        """Packs the frame with the initial interface of this object"""

        # get the account details and create labels for each field
        self.get_account_details()
        self.lbl_username = self.create_lbl_username()
        self.lbl_email = self.create_lbl_email()
        self.lbl_password = self.create_lbl_password()
        self.lbl_bio = self.create_lbl_bio()
        self.btn_edit = self.create_btn_edit()
        self.btn_logout = self.create_btn_logout()

        # username row
        ttk.Label(self.frame_content, text="Username : ").grid(row=0, column=0)
        self.lbl_username.grid(
            row=0, column=1, columnspan=2)

        # email row
        ttk.Label(self.frame_content, text="Email : ").grid(row=1, column=0)
        self.lbl_email.grid(
            row=1, column=1, columnspan=2)

        # password row
        ttk.Label(self.frame_content, text="Password : ").grid(row=2, column=0)
        self.lbl_password.grid(
            row=2, column=1, columnspan=2)

        # bio row
        ttk.Label(self.frame_content, text="Bio : ").grid(row=3, column=0)
        self.lbl_bio.grid(row=3, column=1, rowspan=3, columnspan=2)

        # what the HECK is wrong with self.btn_edit?!?!?!
        self.btn_edit.grid(row=6, column=0)
        self.btn_logout.grid(row=6, column=2)

    def edit_account(self):
        """Launches entry widgets to let user set account attributes"""

        # delete all widgets in content frame
        for widget in self.frame_content.winfo_children():
            widget.destroy()

        # username row
        ttk.Label(self.frame_content, text="Username : ").grid(row=0, column=0)
        self.entry_username = ttk.Entry(self.frame_content)
        self.entry_username.insert(0, self.username)
        self.entry_username.grid(row=0, column=1, columnspan=2)

        # email row
        ttk.Label(self.frame_content, text="Email : ").grid(row=1, column=0)
        self.entry_email = ttk.Entry(self.frame_content)
        self.entry_email.insert(0, self.email)
        self.entry_email.grid(row=1, column=1, columnspan=2)

        # password row
        ttk.Label(self.frame_content, text="Password : ").grid(row=2, column=0)
        ttk.Button(self.frame_content, text="Change Password",
                   command=self.change_password).grid(row=2, column=1, columnspan=2)

        # bio row
        ttk.Label(self.frame_content, text="Bio : ").grid(row=3, column=0)
        self.entry_bio = Text(
            self.frame_content, width=30, height=10, font=('Arial', 10))
        self.entry_bio.insert("1.0", self.bio)
        self.entry_bio.grid(row=3, column=1, columnspan=2)

        # Save and Cancel buttons
        ttk.Button(self.frame_content, text="Save",
                   command=self.save_changes).grid(row=6, column=0)
        ttk.Button(self.frame_content, text="Cancel",
                   command=self.revert).grid(row=6, column=2)

    def save_changes(self):
        """Validates and saves account changes"""

        account_updated = False

        # if username is changed and it is valid, change it in DB!
        if self.entry_username.get() != self.username:
            if Validator.validate_name(self.entry_username.get()):
                self.controller.update_username(self.entry_username.get())
                account_updated = True
            else:
                self.entry_username.delete(0, "end")
                self.entry_username.insert(0, self.username)
                return

        # if email is changed and it is valid, change it in DB!
        if self.entry_email.get() != self.email:
            if Validator.validate_email(self.entry_email.get()):
                self.controller.update_email(self.entry_email.get())
                account_updated = True
            else:
                self.entry_email.delete(0, "end")
                self.entry_email.insert(0, self.email)
                return

        # if bio is changed and it is valid, change it in DB!
        if self.entry_bio.get("1.0", END) != self.bio:
            if Validator.validate_bio(self.bio):
                self.controller.update_bio(self.entry_bio.get("1.0", END))
                account_updated = True
            else:
                self.entry_bio.delete("1.0", END)
                self.entry_bio.insert("1.0", self.bio)
                return

        # if the account has been updated in DB, revert to orginal content frame
        if account_updated:
            self.revert()
            self.pack_content()

    def revert(self):
        """Reverts the content frame back to its starting state"""

        for widget in self.frame_content.winfo_children():
            widget.destroy()

        self.pack_content()

    def logout(self):
        """Logs the user out of Campus Thrift"""

        self.traceback.logout()
        self.destroy()

    def change_password(self):
        """Allows the user their change password"""

        # destroy all widgets in content frame
        for widget in self.frame_content.winfo_children():
            widget.destroy()

        # password ana confirm_pw label and entry fields
        self.lbl_new_password = ttk.Label(
            self.frame_content, text="New Password")
        self.entry_new_password = ttk.Entry(
            self.frame_content, width=30, font=("Arial", 10), show="*")
        self.lbl_confirm_pw = ttk.Label(
            self.frame_content, text="Confirm Password")
        self.entry_confirm_pw = ttk.Entry(
            self.frame_content, width=30, font=("Arial", 10), show="*")

        # grid the labels and entries to content frame
        self.lbl_new_password.grid(row=0, column=0, columnspan=3)
        self.entry_new_password.grid(row=1, column=0, columnspan=3)
        self.lbl_confirm_pw.grid(row=2, column=0, columnspan=3)
        self.entry_confirm_pw.grid(row=4, column=0, columnspan=3)

        # Save and Cancel buttons
        ttk.Button(self.frame_content, text="Save",
                   command=self.save_password).grid(row=5, column=0)
        ttk.Button(self.frame_content, text="Cancel",
                   command=self.revert).grid(row=5, column=2)

    def save_password(self):
        """Saves new password to the database"""

        new_pw = self.entry_new_password.get()
        confirm_pw = self.entry_confirm_pw.get()

        # if password info is valid, update it in DB and revert back to original content frame
        if Validator.validate_password(new_pw, confirm_pw):
            self.controller.update_pw(new_pw)
            self.revert()
        # else keep trying
        else:
            self.entry_new_password.delete(
                0, len(self.entry_new_password.get()))
            self.entry_confirm_pw.delete(0, len(self.entry_confirm_pw.get()))

    def create_lbl_username(self):
        """Creates a username label"""
        return ttk.Label(self.frame_content, text=self.username)

    def create_lbl_email(self):
        """Creates an email label"""
        return ttk.Label(self.frame_content, text=self.email)

    def create_lbl_password(self):
        """Creates a password label"""
        return ttk.Label(self.frame_content, text=self.password)

    def create_lbl_bio(self):
        """Creates a bio label"""
        return ttk.Label(self.frame_content, text=self.bio)

    def create_btn_edit(self):
        """Creates an Edit button"""
        return ttk.Button(self.frame_content, text="Edit Profile",
                          command=self.edit_account)

    def create_btn_logout(self):
        """Creates a logout button"""
        return ttk.Button(self.frame_content, text="Logout",
                          command=self.logout)
