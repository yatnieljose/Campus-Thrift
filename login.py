#!/usr/bin/python3
# feedback_solution.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys
sys.path.append('..')
import listing

class Feedback:

    def __init__(self, master):
        
        master.title('Campus Thrift')
        master.resizable(False, False)
        master.configure(background = '#041E42')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#041E42')
        self.style.configure('TButton', background = '#041E42')
        self.style.configure('TLabel', background = '#041E42', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))      

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        lion_photo = PhotoImage(file = 'thriftanyLion.png')
        wordart_photo = PhotoImage(file = 'ct_wordart.png')
        

        #ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, image = wordart_photo).grid(row = 0, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Username:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Password:').grid(row = 0, column = 2, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, image = lion_photo).grid(row = 2, column = 1, padx = 5, sticky = 'sw')
        
        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        
        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 2, padx = 5)
        
        ttk.Button(self.frame_content, text = 'Submit',
                   command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear',
                   command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

        for i in range(5):
            listing.Listing(self.frame_content, "item name", "$99.99", 5 + i, 0)

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title = 'Explore California Feedback', message = 'Comments Submitted!')
    
    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')
         
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
