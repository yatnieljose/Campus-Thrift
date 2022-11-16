from tkinter import *
from tkinter import ttk
import sys
sys.path.append('..')
import ct_tk

import json
from pathlib import Path

filepath = '../acc_info.json'
filename = 'acc_info.json'
acc_file = Path(filename)

if (not(acc_file.exists())):
    with open('acc_info.json', 'w') as new_file:
        json.dump({}, new_file)

class SignUpTk:

    def __init__(self, master):

        root = master

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        self.logo_photo = PhotoImage(master = master, file = 'psu_logo.png')
        self.sign_up_photo = PhotoImage(master = master, file = 'sign_up.png')

        ttk.Label(self.frame_header, image = self.logo_photo).grid(row = 0, column = 0)
        ttk.Label(self.frame_header, image = self.sign_up_photo).grid(row = 0, column = 1)
        ttk.Label(self.frame_header, image = self.logo_photo).grid(row = 0, column = 2)
        
        ttk.Label(self.frame_content, text = 'Full Name:').grid(row = 1, column = 2, pady = 10, sticky = 'w')
        self.entry_name = ttk.Entry(self.frame_content, width = 30, font = ('Arial', 10))
        self.entry_name.grid(row = 2, column = 2)

        ttk.Label(self.frame_content, text = 'EMail:').grid(row = 3, column = 2, pady = 10, sticky = 'w')
        self.entry_email = ttk.Entry(self.frame_content, width = 30, font = ('Arial', 10))
        self.entry_email.grid(row = 4, column = 2)

        ttk.Label(self.frame_content, text = 'Password:').grid(row = 5, column = 2, pady = 10, sticky = 'w')
        self.entry_password = ttk.Entry(self.frame_content, width = 30, font = ('Arial', 10), show = '*')
        self.entry_password.grid(row = 6, column = 2)

        ttk.Label(self.frame_content, text = 'Confirm Password:').grid(row = 7, column = 2, pady = 10, sticky = 'w')
        self.entry_confirm_pw = ttk.Entry(self.frame_content, width = 30, font = ('Arial', 10), show = '*')
        self.entry_confirm_pw.grid(row = 8, column = 2)

        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 9, column = 2, pady = 20)

    def submit(self):
        
        with open(filename, 'r') as acc_file:
            acc_data = json.load(acc_file)
        
        if(self.check_pw()):
            acc_id = self.entry_email.get()
            acc_data[acc_id] = {}
            acc_data[acc_id]['name'] = self.entry_name.get()
            acc_data[acc_id]['password'] = self.entry_password.get()
            with open (filename, 'w') as acc_write:
                json.dump(acc_data, acc_write)
            root.destroy()
        else:
            self.entry_password.delete(0, len(self.entry_password.get()))
            self.entry_confirm_pw.delete(0, len(self.entry_confirm_pw.get()))
            messagebox.showinfo(title = 'Failure!', message = 'Passwords did not match')

    def check_pw(self):
        return(self.entry_password.get() == self.entry_confirm_pw.get())


