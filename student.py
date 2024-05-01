from tkinter import *
from PIL import Image, ImageTk

class student_class:
    def __init__(self, r):
        self.root = r
        self.root.geometry("1280x600")
        self.root.title("Student")
        self.root.config(bg="#d3d9e2")
        self.root.focus_force() # to make focus forcefully from dashboard

        title = Label(self.root,text="Manage Student", font="arial 15 bold", bg="#7e57c2", fg="white")
        title.place(x=10, y=10, relwidth=0.985, height=45)

if __name__ == "__main__":
    r = Tk()
    obj = student_class(r)
    r.mainloop()