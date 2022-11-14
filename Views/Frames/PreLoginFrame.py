from tkinter import *
from tkinter import ttk

# The active frame before the activation of a successful login

class PreLoginFrame(ttk.Frame) :
    def __init__(self, master) :
        ttk.Frame.__init__(self, master)

        # needs to set up login frame, including "sign up" and "sign in" buttons
        # "sign in" is already refreshed on screen so "sign in" button initially does nothing
        # "sign up" button pulls up sign up screen (if not already up)
        # "sign in" button pulls up sign up screen (if not already up)
        # !!! These will be configured to work with login.py and sign_up.py    

        