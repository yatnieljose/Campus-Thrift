import tkinter as tk
from tkinter import ttk


def make_settings_visible():
    pass


class TopFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # initialize button with user's profile picture
        # dummy button
        self.prof_pic = tk.PhotoImage(file="thriftanyLion.png")
        self.btn_prof_pic = tk.Button(
            master=self, text="Profile Picture", command=make_settings_visible)

        # Logo
        self.lbl_logo = tk.Label(master=self, text="Campus Thrift", bd=2)

        # Rank and Transactions
        self.frm_rank = tk.Frame(master=self, relief=tk.RIDGE, bd=2)
        self.lbl_rank = tk.Label(master=self.frm_rank, text=f"Rank : ")
        self.lbl_completed_trans = tk.Label(
            master=self.frm_rank, fg="green", text=f"Completed Transactions : ")
        self.lbl_declined_trans = tk.Label(
            master=self.frm_rank, fg="red", text=f"Declined Transactions : ")

        self.lbl_rank.grid(row=0, column=0, sticky="ew")
        self.lbl_completed_trans.grid(row=1, column=0, sticky="ew")
        self.lbl_declined_trans.grid(row=2, column=0, sticky="ew")

        self.btn_prof_pic.grid(row=0, column=0, sticky="w")
        self.lbl_logo.grid(row=0, column=1, sticky="nsew")
        self.frm_rank.grid(row=0, column=2, sticky="ew")
