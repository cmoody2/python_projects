#   Author:         Christopher A. Moody
#
#   Purpose:        Creating a Student Tracking System. This will demonstrate
#                   OOP, Tkinter GUI module, and using Tkinter Parent
#                   and child relationships.
#
#   Tested OS:      Written and tested with Windows 10.


from tkinter import *
import tkinter as tk


import student_tracker_main
import student_tracker_func

def load_gui(self):

    self.lbl_fname = tk.Label(self.master, text='First Name: ', bg='#90ee90')
    self.lbl_fname.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_lname = tk.Label(self.master, text='Last Name: ', bg='#90ee90')
    self.lbl_lname.grid(row=2, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_phone = tk.Label(self.master, text='Phone Number: ', bg='#90ee90')
    self.lbl_phone.grid(row=4, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_email = tk.Label(self.master, text='Email: ', bg='#90ee90')
    self.lbl_email.grid(row=6, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
    self.lbl_course = tk.Label(self.master, text='Current Course: ', bg='#90ee90')
    self.lbl_course.grid(row=8, column=0, padx=(27,0), pady=(10,0), sticky=N+W)

    self.txt_fname = tk.Entry(self.master, text='')
    self.txt_fname.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master, text='')
    self.txt_lname.grid(row=3, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master, text='')
    self.txt_phone.grid(row=5, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_email = tk.Entry(self.master, text='')
    self.txt_email.grid(row=7, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    self.txt_course = tk.Entry(self.master, text='')
    self.txt_course.grid(row=9, column=0, rowspan=1, columnspan=2, padx=(30,40), pady=(0,0), sticky=N+E+W)
    
    self.scrollbar1 = Scrollbar(self.master, orient=VERTICAL)
    self.lstList1 = Listbox(self.master, exportselection=0, yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>', lambda event: student_tracker_func.onSelect(self, event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1, column=5, rowspan=7, columnspan=1, padx=(0,0), pady=(0,0), sticky=N+E+S)
    self.lstList1.grid(row=1, column=2, rowspan=7, columnspan=3, padx=(0,0), pady=(0,0), sticky=N+E+S+W)

    self.btn_add = tk.Button(self.master, width=12, height=2, text='Add', command=lambda: student_tracker_func.addToList(self))
    self.btn_add.grid(row=9, column=0, padx=(25,0), pady=(45,10),sticky=W)
    self.btn_delete = tk.Button(self.master, width=12, height=2, text='Delete', bg='#FF0000', fg='#FFFFFF', command=lambda: student_tracker_func.onDelete(self))
    self.btn_delete.grid(row=9, column=2, padx=(15,0), pady=(45,10), sticky=W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close', command=lambda: student_tracker_func.ask_quit(self))
    self.btn_close.grid(row=9, column=4, columnspan=1, padx=(15,0), pady=(45,10), sticky=E)

    student_tracker_func.create_db(self)
    student_tracker_func.onRefresh(self)



if __name__ == "__main__":
    pass
