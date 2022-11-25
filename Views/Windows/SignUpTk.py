"""Contains the SignUpTk class"""

from pathlib import Path
import json
from tkinter import *
from tkinter import ttk
import sys
import ct_tk
sys.path.append('..')


FILEPATH = '../acc_info.json'
FILENAME = 'acc_info.json'
ACC_FILE = Path(FILENAME)

if not ACC_FILE.exists():
    with open('acc_info.json', 'w', encoding="utf8") as new_file:
        json.dump({}, new_file)


class SignUpTk(Tk):
    """Represents a SignUpTk popup window within the LoginFrame object"""

    def __init__(self):
        Tk.__init__(self)
        ct_tk.CT_Tk(self, 'Campus Thrift')

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

        ttk.Button(self.frame_content, text='Submit',
                   command=self.submit).grid(row=9, column=2, pady=20)

    def submit(self):

        with open(FILENAME, 'r', encoding="utf8") as ACC_FILE:
            acc_data = json.load(ACC_FILE)

        if (self.check_pw()):
            acc_id = self.entry_email.get()
            acc_data[acc_id] = {}
            acc_data[acc_id]['name'] = self.entry_name.get()
            acc_data[acc_id]['password'] = self.entry_password.get()
            with open(FILENAME, 'w', encoding="utf8") as acc_write:
                json.dump(acc_data, acc_write)
            self.destroy()
        else:
            self.entry_password.delete(0, len(self.entry_password.get()))
            self.entry_confirm_pw.delete(0, len(self.entry_confirm_pw.get()))
            messagebox.showinfo(
                title='Failure!', message='Passwords did not match')

    def check_pw(self):
        return (self.entry_password.get() == self.entry_confirm_pw.get())
