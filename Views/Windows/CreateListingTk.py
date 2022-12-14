from tkinter import Tk, ttk, PhotoImage, messagebox, StringVar
import Views.Styling.ct_tk as ct_tk
import Views.Styling.ct_style as ct_style
import Models.TypeOptions as TypeOptions


class CreateListingTk(Tk):
    """Gathers validated information about an item that is to be created in the database"""

    def __init__(self, controller, traceback):
        Tk.__init__(self)
        ct_tk.CT_Tk(self, "Create Listing")
        self.label_style = ct_style.CT_Style().CT_Label()

        self.controller = controller
        self.traceback = traceback

        self.frame_header = ttk.Frame(self)
        self.frame_header.pack()
        self.frame_content = ttk.Frame(self)
        self.frame_content.pack(pady=30)

        # Create header frame
        self.logo_photo = PhotoImage(
            master=self.frame_header, file='psu_logo.png')

        ttk.Label(self.frame_header, image=self.logo_photo).grid(
            row=0, column=0)
        ttk.Label(self.frame_header, text="Create Listing").grid(
            row=0, column=1)
        ttk.Label(self.frame_header, image=self.logo_photo).grid(
            row=0, column=2)

        # Create content frame

        # Name row
        ttk.Label(self.frame_content, text="Name : ").grid(row=0, column=0)
        self.entry_name = ttk.Entry(self.frame_content)
        self.entry_name.grid(row=0, column=1)

        # Type row
        self.clicked = StringVar(self.frame_content)
        self.clicked.set(TypeOptions.type_options[0])

        ttk.Label(self.frame_content, text="Type : ").grid(row=1, column=0)
        self.drop_type = ttk.OptionMenu(
            self.frame_content, self.clicked, TypeOptions.type_options[0], *TypeOptions.type_options)
        self.drop_type.grid(row=1, column=1)

        # Minimum Bid row
        ttk.Label(self.frame_content, text="Minimum Bid : ").grid(
            row=2, column=0)
        self.entry_min_bid = ttk.Entry(self.frame_content)
        self.entry_min_bid.grid(row=2, column=1)

        # Submit Button
        ttk.Button(self.frame_content, text="Submit", command=self.try_create_item).grid(
            row=3, column=0, columnspan=2)

    def try_create_item(self):
        """Attempts to create new item based on given user input"""

        # returns None if validated, else returns error code
        # else returns widget that is "wrong"
        validation_flag = self.validate_input()

        if validation_flag is None:
            item_info = {'name': self.entry_name.get(),
                         'type': self.clicked.get(),
                         'min_bid': int(self.entry_min_bid.get())}

            self.controller.create_item(item_info)
            self.traceback.refresh_sell_listings()
            self.destroy()

        else:
            validation_flag.delete(0, len(validation_flag.get()))

    def validate_input(self):
        """Validates user input ---  0 < length of name < 50 --- 0 < type < 16 --- 0 < 1,000,000"""

        name = self.entry_name
        min_bid = self.entry_min_bid

        if len(name.get()) < 1 or len(name.get()) > 50:
            messagebox.showinfo(title='InvalidName',
                                message="Name must be between 1 and 50 characters")

            return name

        if int(min_bid.get()) <= 0 or int(min_bid.get()) > 1000000:
            messagebox.showinfo(title='InvalidMinBid',
                                message="The minimum bid must be between $1 and $1,000,000")

            return min_bid
