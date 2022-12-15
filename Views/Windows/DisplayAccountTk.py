from tkinter import Tk, ttk, PhotoImage
import Views.Styling.ct_tk as ct_tk
import Views.Styling.ct_style as ct_style


class DisplayAccountTk(Tk):
    """Displays account info relevant to a given account"""

    def __init__(self, account):
        Tk.__init__(self)
        ct_tk.CT_Tk(self, "Account Information")
        self.label_style = ct_style.CT_Style().CT_Label()

        self.account = account

        self.frame_header = ttk.Frame(self)
        self.frame_header.pack()
        self.frame_content = ttk.Frame(self)
        self.frame_content.pack(pady=30)

        # Create header frame
        self.logo_photo = PhotoImage(
            master=self.frame_header, file='psu_logo.png')

        ttk.Label(self.frame_header, image=self.logo_photo).grid(
            row=0, column=0)
        ttk.Label(self.frame_header, text="Account Information").grid(
            row=0, column=1)
        ttk.Label(self.frame_header, image=self.logo_photo).grid(
            row=0, column=2)

        # Create content frame

        ttk.Label(self.frame_content, text="Seller Name: ",
                  font=("Times", 16)).pack(pady=20)
        ttk.Label(self.frame_content, text=self.account.get_name).pack()

        ttk.Label(self.frame_content, text="Email: ",
                  font=("Times", 16)).pack(pady=20)
        ttk.Label(self.frame_content,
                  text=self.account.get_email).pack()

        ttk.Label(self.frame_content, text="Bio: ",
                  font=("Times", 16)).pack(pady=20)
        ttk.Label(self.frame_content, text=self.account.get_bio).pack()
