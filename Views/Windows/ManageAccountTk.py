"""Contains the ManageAccountTk class"""
from tkinter import Tk, ttk
import Views.Styling.ct_tk as ct_tk
from PIL import Image, ImageTk

class ManageAccountTk(Tk):
    """Represents a ManageAccountTk popup window within the TopFrame object"""
    #TopFrame ->

    def __init__(self, account):
        Tk.__init__(self)
        ct_tk.CT_Tk(self, "Manage Account")
        
        self.frame_header = ttk.Frame(self)
        self.frame_content = ttk.Frame(self)

        self.frame_header.pack()
        self.frame_content.pack()
        self.profile_image = Image.open("C:\\Users\\Yatnizel\\Documents\\Penn State\\SWENG 411\\Campus-Thrift-1\\ct_profile.jpeg")
        self.profile_imageTk = ImageTk.PhotoImage(image=self.profile_image)
        self.username = account.get_name
        self.email = account.get_email
        self.password = account.get_password
        self.bio = account.get_bio

        ### Picture is not working for some reason
        #ttk.Label(self.frame_header, image=self.profile_imageTk).grid(
        #    row=0, column=1)

        ttk.Label(self.frame_content, text=self.username).grid(
            row=0, column=1)
        ttk.Label(self.frame_content, text=self.email).grid(
            row=2, column=1)
        ttk.Label(self.frame_content, text=self.password).grid(
            row=4, column=1)
        ttk.Label(self.frame_content, text=self.bio).grid(row=6, column=1)