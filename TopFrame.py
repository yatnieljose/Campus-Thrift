from tkinter import *
from tkinter import ttk


def make_settings_visible():
    pass


class TopFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        # initialize button with user's profile picture
        # dummy button
        self.prof_pic = PhotoImage(file="thriftanyLion.png")
        self.btn_prof_pic = ttk.Button(
            master=self, text="Profile Picture", command=make_settings_visible)

        # Logo
        self.lbl_logo = ttk.Label(master=self, text="Campus Thrift", bd=2)

        # Rank and Transactions
        self.frm_rank = ttk.Frame(master=self, bd=2)
        self.lbl_rank = ttk.Label(master=self.frm_rank, text=f"Rank : ")
        self.lbl_completed_trans = ttk.Label(
            master=self.frm_rank, fg="green", text=f"Completed Transactions : ")
        self.lbl_declined_trans = ttk.Label(
            master=self.frm_rank, fg="red", text=f"Declined Transactions : ")

        self.lbl_rank.grid(row=0, column=0, sticky="ew")
        self.lbl_completed_trans.grid(row=1, column=0, sticky="ew")
        self.lbl_declined_trans.grid(row=2, column=0, sticky="ew")

        self.btn_prof_pic.grid(row=0, column=0, sticky="w")
        self.lbl_logo.grid(row=0, column=1, sticky="nsew")
        self.frm_rank.grid(row=0, column=2, sticky="ew")
