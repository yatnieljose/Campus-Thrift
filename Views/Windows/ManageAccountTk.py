"""Contains the ManageAccountTk class"""
from tkinter import Tk, ttk
import Views.Styling.ct_tk as ct_tk
import Views.Styling.ct_style as ct_style
from PIL import Image, ImageTk

class ManageAccountTk(Tk):
    """Represents a ManageAccountTk popup window within the TopFrame object"""
    #TopFrame ->

    def __init__(self, account):
        Tk.__init__(self)
        ct_tk.CT_Tk(self, "Manage Account")
        self.label_style = ct_style.CT_Style().CT_Label()
        self.logout = False
        
        self.frame_header = ttk.Frame(self)
        self.frame_content = ttk.Frame(self)
        #profile_image = Image.open("ct_profile_settings.png")
        #profile_imageTk = ImageTk.PhotoImage(image=profile_image)
        self.username = account.get_name
        self.email = account.get_email
        self.password = account.get_password
        self.bio = account.get_bio

        ### Picture is not working for some reason
        #ttk.Label(self.frame_header, image=profile_imageTk).grid(
        #    row=0, column=1)

        ttk.Label(self.frame_content, text=self.username).grid(row=0, column=1)
        #label_username = .configure(style="TLabel")
        #label_username
        self.username_entry = ttk.Entry(self.frame_content, textvariable="username")
        ttk.Label(self.frame_content, text=self.email).grid(
            row=2, column=1)
        self.email_entry = ttk.Entry(self.frame_content, textvariable="username")
        ttk.Label(self.frame_content, text=self.password).grid(
            row=4, column=1)
        self.username_entry = ttk.Entry(self.frame_content, textvariable="username")
        ttk.Label(self.frame_content, text=self.bio).grid(
            row=6, column=1)

        ttk.Button(self.frame_content, text="Change Profile").grid(row=7, column=0)
        self.logout = ttk.Button(self.frame_content, text="Logout", command=self.logout)
        self.logout.grid(row=7, column=2)

        self.frame_header.pack()
        self.frame_content.pack()

    def logout(self):
        self.logout = True
        print("works")
        self.destroy()