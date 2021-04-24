from Tkinter import *
root=Tk()
Label(root, text="Project Title: PhoneBook", font="Helvetica 20 bold", bg="pink").grid(row=0, column=0)
Label(root, text="Project of Python and Database", font="times 20 bold").grid(row=2,column=3)
Label(root, text="Developed by: ROHINI VERMA, 181B171", font="Helvetica 15 bold").grid(row=3,column=3)
Label(root, text="make mouse movement over this screen to close", font="times 10").grid(row=5,column=3)
def close(e=1):
    root.destroy()
root.bind('<Motion>', close)
root.mainloop()
