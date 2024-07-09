import tkinter
from tkinter import messagebox


root=tkinter.Tk()



def Onclick_submit():
    name=name_textbox.get()
    enrollment=enrollment_textbox.get()
    section=section_textbox.get()
    
    if name and enrollment and section:
        messagebox.showinfo("status","Data Submitted")
    else:
        messagebox.showwarning("Warning","Please Fill all the details")

root.geometry("300x400")
root.configure(bg="#808080")

root.title("Registration Form")

name_label=tkinter.Label(root,text="Enter Name")
name_label.pack(anchor=tkinter.W,padx=20)
name_textbox=tkinter.Entry(root)
name_textbox.pack(anchor=tkinter.W,padx=20)

enrollment_label=tkinter.Label(root,text="Enter Enrollment Number")
enrollment_label.pack(anchor=tkinter.W,padx=20)
enrollment_textbox=tkinter.Entry(root)
enrollment_textbox.pack(anchor=tkinter.W,padx=20)

section_label=tkinter.Label(root,text="Enter Section")
section_label.pack(anchor=tkinter.W,padx=20)
section_textbox=tkinter.Entry(root)
section_textbox.pack(anchor=tkinter.W,padx=20)

submit_button=tkinter.Button(root,text="Submit",command=Onclick_submit)
submit_button.pack(anchor=tkinter.W,padx=20)

root.mainloop()







