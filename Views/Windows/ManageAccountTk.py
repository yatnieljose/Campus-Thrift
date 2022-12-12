"""Contains the ManageAccountTk class"""
from tkinter import Tk, ttk, messagebox
import Views.Styling.ct_tk as ct_tk
import Views.Styling.ct_style as ct_style
from PIL import Image, ImageTk


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

        self.frame_header = ttk.Frame(self)
        self.frame_content = ttk.Frame(self)
        #profile_image = Image.open("ct_profile_settings.png")
        #profile_imageTk = ImageTk.PhotoImage(image=profile_image)
        self.username = self.account.get_name
        self.email = self.account.get_email
        self.password = self.account.get_password
        self.bio = self.account.get_bio

        # Picture is not working for some reason
        # ttk.Label(self.frame_header, image=profile_imageTk).grid(
        #    row=0, column=1)

        ttk.Label(self.frame_content, text=self.username).grid(row=0, column=1)
        # label_username = .configure(style="TLabel")
        # label_username
        self.username_entry = ttk.Entry(
            self.frame_content, textvariable="username")
        ttk.Label(self.frame_content, text=self.email).grid(
            row=2, column=1)
        self.email_entry = ttk.Entry(self.frame_content, textvariable="email")
        ttk.Label(self.frame_content, text=self.password).grid(
            row=4, column=1)
        self.bio_entry = ttk.Entry(self.frame_content, textvariable="bio")
        ttk.Label(self.frame_content, text=self.bio).grid(
            row=6, column=1)

        self.btn_change_password = ttk.Button(self.frame_content, text="Change Password", command=self.change_password).grid(
            row=11, column=0)
        self.lbl_new_password = None
        self.entry_new_password = None
        self.lbl_confirm_pw = None
        self.entry_confirm_pw = None
        self.btn_save_pw = None

        ttk.Button(self.frame_content, text="Logout",
                   command=self.logout).grid(row=11, column=2)

        self.frame_header.pack()
        self.frame_content.pack()

    def logout(self):
        """Logs the user out of Campus Thrift"""
        self.traceback.logout()
        self.destroy()

    def change_password(self):
        """Allows the user their change password and/or bio"""
        self.lbl_new_password = ttk.Label(
            self.frame_content, text="New Password").grid(row=7, column=1)
        self.entry_new_password = ttk.Entry(self.frame_content, width=30, font=(
            "Arial", 10), show="*").grid(row=8, column=1)
        self.lbl_confirm_pw = ttk.Label(
            self.frame_content, text="Confirm Password").grid(row=9, column=1)
        self.entry_confirm_pw = ttk.Entry(self.frame_content, width=30, font=(
            "Arial", 10), show="*").grid(row=10, column=1)
        self.btn_save_pw = ttk.Button(
            self.frame_content, text="Save", command=self.save_password).grid(row=11, column=0)
        self.btn_change_password.destroy()

    def save_password(self):
        """Saves new password to the database"""
        new_pw = self.entry_new_password.get()
        confirm_pw = self.entry_confirm_pw.get()

        if (new_pw == confirm_pw):
            self.traceback.update_pw(new_pw)
            self.lbl_new_password.destroy()
            self.lbl_confirm_pw.destroy()
            self.btn_save_pw.destroy()
            self.btn_change_password = ttk.Button(self.frame_content, text="Change Password", command=self.change_password).grid(
                row=11, column=0)
        else:
            self.new_password.delete(0, len(self.new_password.get()))
            self.confirm_pw.delete(0, len(self.confirm_pw.get()))
            messagebox.showinfo(title="Password Mismatch",
                                message="Passwords do not match")
