"""Contains the LoginFrame class"""

from tkinter import PhotoImage, messagebox, ttk


class LoginFrame(ttk.Frame):
    """Represents a LoginFrame UI object"""

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master

        self.frame_header = ttk.Frame(self)
        self.frame_header.pack()
        self.frame_content = ttk.Frame(self)
        self.frame_content.pack()

        self.lion_photo = PhotoImage(file='thriftanyLion.png')
        self.wordart_photo = PhotoImage(file='ct_wordart.png')

        ttk.Label(self.frame_header, image=self.wordart_photo).grid(
            row=0, column=0)
        ttk.Label(self.frame_content, image=self.lion_photo).grid(
            row=1, column=1, padx=5, columnspan=2, sticky='we')
        ttk.Label(self.frame_content, text='Username:').grid(
            row=3, column=1, padx=5, sticky='w')
        ttk.Label(self.frame_content, text='Password:').grid(
            row=3, column=2, padx=5, sticky='w')
        ttk.Button(self.frame_content, text='Sign up', command=self.sign_up).grid(
            row=3, column=0, padx=5, pady=5)
        ttk.Button(self.frame_content, text='Submit',
                   command=self.try_login).grid(row=4, column=0)
        # Entry widgets
        self.entry_username = ttk.Entry(
            self.frame_content, width=24, font=('Arial', 10))
        self.entry_password = ttk.Entry(
            self.frame_content, width=24, font=('Arial', 10))
        self.entry_username.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        self.entry_password.grid(row=4, column=2)

    def try_login(self):
        """Checks credentials of attempted login"""

        # if database contains a username/password match, initiate login_successful functionality. Else,
        # clear the Entry widgets and show an error message
        if (self.master.try_login(self.entry_username.get(), self.entry_password.get())):
            # this changes the current display to reflect successful login
            self.master.login_successful()
        else:
            self.clear()
            messagebox.showinfo(title="LoginFailure",
                                message="Login Unsuccessful")

    def clear(self):
        """Clears the current user entries representing username and password"""
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')

    def sign_up(self):
        """Launches a sign up window for user to create an account"""
        self.master.display_signuptk()
