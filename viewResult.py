from tkinter import *
from PIL import Image, ImageTk

class view_result_class:
    def __init__(self, r):
        self.root = r
        self.root.geometry("1280x600")
        self.root.title("View Result")
        self.root.config(bg="#d3d9e2")
        self.root.focus_force() # to make focus forcefully from dashboard

        title = Label(self.root,text="View Result", font="arial 15 bold", bg="#26c6da", fg="white")
        title.place(x=10, y=10, relwidth=0.985, height=45)

if __name__ == "__main__":
    r = Tk()
    obj = view_result_class(r)
    r.mainloop()