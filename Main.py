from tkinter import *
from tkinter import ttk
from Views.Frames.TopFrame import *
from Views.Frames.PreLoginFrame import PreLoginFrame

# this class contains a main window that loads different frame instances based on state
# this class contains an Account object pulled from the database in the event of login

# initially shows login/sign up page when called (when app is initialized)
# then shows different fields depending on whether login or sign up is selected
# changes window to show main screen if login is successfu; (while simultaneously loading login
# info)

window = Tk()
window.title("Campus Thrift")
window.resizable(width=False, height=False)

# must first show login/signup frames, and then show main frames (TopFrame, a "MidFrame" with
# window options MyListings and ListingSearch)


# needs configured
window.rowconfigure([0, 1, 2], minsize=200)
window.columnconfigure(0, minsize=1000)


# first create a frame object for sign up and login that shows up immediately
frm_init = PreLoginFrame(window)

# create these components after successful login
frm_top = TopFrame(window)


frm_choice = Frame(master=window)
frm_bot = Frame(master=window)

# need configured with full scope of post-login frames
frm_top.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
frm_choice.grid(row=1, column=0, padx=25)
frm_bot.grid(row=2, column=0, padx=10)


window.mainloop()
