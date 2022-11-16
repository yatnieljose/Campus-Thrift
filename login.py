from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
sys.path.append('..')
import ct_tk
#import listing
import sign_up
import json

filename = 'acc_info.json'

class LoginFrame:

    def __init__(self, master):    

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        self.lion_photo = PhotoImage(file = 'thriftanyLion.png')
        self.wordart_photo = PhotoImage(file = 'ct_wordart.png')
        
        ttk.Label(self.frame_header, image = self.wordart_photo).grid(row = 0, column = 0)
        ttk.Label(self.frame_content, image = self.lion_photo).grid(row = 1, column = 1, padx = 5, columnspan = 2, sticky = 'we')
        ttk.Label(self.frame_content, text = 'Username:').grid(row = 3, column = 1, padx = 5, sticky = 'w')
        ttk.Label(self.frame_content, text = 'Password:').grid(row = 3, column = 2, padx = 5, sticky = 'w')
        ttk.Button(self.frame_content, text = 'Sign up', command = self.sign_up).grid(row = 3, column = 0, padx = 5, pady = 5)
        ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0)
        #Entry widgets
        self.entry_username = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_password = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_username.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')
        self.entry_password.grid(row = 4, column = 2)

    def submit(self):
        name = self.entry_username.get()
        password = self.entry_password.get()
        self.clear()
        
        with open(filename, 'r') as acc_file:
            acc_data = json.load(acc_file)

        account_login = acc_data[name]

        if(account_login['password'] == password):
            messagebox.showinfo(title = 'Success!', message = 'Login Successful')
    
    def clear(self):
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')

    def sign_up(self):
        sign_up.main()
