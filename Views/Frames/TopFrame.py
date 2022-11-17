from tkinter import *
from tkinter import ttk
import ct_tk
from PIL import Image, ImageTk


def make_settings_visible():
    pass


class TopFrame(ttk.Frame):
    def __init__(self, master):
        # set the height of the frame throughout the class, call super's constructor
        self.height = 100
        ttk.Frame.__init__(self, master, height=500)

        # frame for profile picture
        self.frm_prof_pic = ttk.Frame(
            master=self, width=self.height, height=self.height, padding=(20, 20, 0, 0))

        # open profile picture, resize, and store as instance variable
        prof_pic_orig = Image.open("thriftanyLion.png")
        prof_pic_resize = prof_pic_orig.resize(
            (self.height, self.height))
        self.prof_pic = ImageTk.PhotoImage(prof_pic_resize)

        # create button for profile picture
        # cannot figure out why it looks like ths!
        self.btn_prof_pic = ttk.Button(
            master=self.frm_prof_pic, image=self.prof_pic, command=make_settings_visible)

        self.btn_prof_pic.pack()

        # frame for logo
        self.frm_logo = ttk.Frame(
            master=self, height=self.height, width=500, padding=(50, 20, 0, 0))

        # open logo, resize, and store as instance variable
        logo_orig = Image.open("ct_wordart.png")
        logo_resize = logo_orig.resize((400, 100))
        self.logo = ImageTk.PhotoImage(logo_resize)
        self.lbl_logo = ttk.Label(master=self.frm_logo, image=self.logo)

        self.lbl_logo.pack()

        # Rank and Transactions
        self.frm_rank = ttk.Frame(
            master=self, height=self.height, width=200)
        self.lbl_rank = ttk.Label(master=self.frm_rank, text=f"Rank : ")
        self.lbl_completed_trans = ttk.Label(
            master=self.frm_rank, text=f"Completed Transactions : ")

        self.lbl_rank.pack(side=TOP)
        self.lbl_completed_trans.pack(side=TOP)

        self.frm_prof_pic.pack(side=LEFT)
        self.frm_prof_pic.pack_propagate(0)
        self.frm_logo.pack(side=LEFT)
        self.frm_logo.pack_propagate(0)
        self.frm_rank.pack(side=LEFT)
        self.frm_rank.pack_propagate(0)
