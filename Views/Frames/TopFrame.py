"""Contains TopFrame class"""

from tkinter import ttk, TOP
from PIL import Image, ImageTk


def make_settings_visible():
    """Reaction to user requesting to open the account settings (click on profile picture / settings icon)"""
    pass


class TopFrame(ttk.Frame):
    """References a TopFrame object for the banner of the MainFrame after login"""

    def __init__(self, master):
        self.height = 100
        ttk.Frame.__init__(self, master)

        # frame for profile picture
        self.frm_prof_pic = ttk.Frame(
            master=self, width=self.height, height=self.height)

        # open profile picture, resize, and store as instance variable
        prof_pic_orig = Image.open("thriftanyLion.png")
        prof_pic_resize = prof_pic_orig.resize(
            (self.height, self.height))
        self.prof_pic = ImageTk.PhotoImage(prof_pic_resize)

        # create button for profile picture
        # cannot figure out why it looks like ths!
        self.img_label = ttk.Label(image=self.prof_pic)
        self.btn_prof_pic = ttk.Button(
            master=self.frm_prof_pic, image=self.prof_pic, command=make_settings_visible)

        self.btn_prof_pic.pack()

        # frame for logo
        self.frm_logo = ttk.Frame(
            master=self, height=self.height, width=500)

        # open logo, resize, and store as instance variable
        logo_orig = Image.open("ct_wordart.png")
        logo_resize = logo_orig.resize((400, 100))
        self.logo = ImageTk.PhotoImage(logo_resize)
        self.lbl_logo = ttk.Label(master=self.frm_logo, image=self.logo)

        self.lbl_logo.pack()

        # Rank and Transactions (we will need data to populate rank and transaction within "text" attribute of each Label)
        self.frm_rank = ttk.Frame(
            master=self, height=self.height, width=200)
        self.lbl_rank = ttk.Label(master=self.frm_rank, text=f"Rank : ")
        self.lbl_completed_trans = ttk.Label(
            master=self.frm_rank, text=f"Completed Transactions : ")

        self.lbl_rank.pack(side=TOP)
        self.lbl_completed_trans.pack(side=TOP)

        self.frm_logo.grid(row=0, column=1, rowspan=2,
                           padx=50, sticky="n")
        self.frm_prof_pic.grid(row=0, column=0)
        self.frm_rank.grid(row=0, column=2, rowspan=2)
