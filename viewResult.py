from tkinter import *
from tkinter import messagebox
import sqlite3

class view_result_class:
    def __init__(self, r):
        self.root = r
        self.root.geometry("1180x600")
        self.root.title("View Result")
        self.root.config(bg="#d3d9e2")
        self.root.focus_force()  # to make focus forcefully from dashboard

        title = Label(self.root, text="View Result", font="arial 15 bold", bg="#26c6da", fg="white")
        title.place(x=10, y=10, relwidth=0.985, height=45)

        self.search_var = StringVar()
        search_label = Label(self.root, text="Search By Roll: ", font="arial 13 bold", bg="white", bd="1", relief=RIDGE)
        search_label.place(x=150, y=80, height=55, width=160)
        search_entry = Entry(self.root, textvariable=self.search_var, font="arial 13", bg="white")
        search_entry.place(x=310, y=80, width=440, height=55)
        btn_search = Button(self.root, text="Search", font="arial 13 bold", bg="dodgerblue", fg="white", cursor="hand2", command=self.search)
        btn_search.place(x=740, y=80, width=150, height=55)

        btn_clear = Button(self.root, text="Clear", font="arial 13 bold", bg="#FFBE00", fg="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=900, y=80, width=150, height=55)

        self.delete = Button(text="Delete", font="arial 13 bold", bg="tomato", fg="white", cursor="hand2", command=self.confirm_delete)
        self.delete.place(x=150, y=280, width=900, height=50)

        label_roll = Label(self.root, text="Roll No", font=("arial 15 "), bg="white", bd=2, relief=GROOVE)
        label_roll.place(x=150, y=170, width=150, height=50)
        label_name = Label(self.root, text="Name", font=("arial 15 "), bg="white", bd=2, relief=GROOVE)
        label_name.place(x=300, y=170, width=150, height=50)
        label_course = Label(self.root, text="Course", font=("arial 15 "), bg="white", bd=2, relief=GROOVE)
        label_course.place(x=450, y=170, width=150, height=50)
        label_marks = Label(self.root, text="Marks Obtained", font=("arial 15 "), bg="white", bd=2, relief=GROOVE)
        label_marks.place(x=600, y=170, width=150, height=50)
        label_full = Label(self.root, text="Total Marks", font=("arial 15 ",), bg="white", bd=2, relief=GROOVE)
        label_full.place(x=750, y=170, width=150, height=50)
        label_per = Label(self.root, text="Percentage", font=("arial 15 "), bg="white", bd=2, relief=GROOVE)
        label_per.place(x=900, y=170, width=150, height=50)

        self.roll = Label(self.root, font=("arial 15 "), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=220, width=150, height=50)
        self.name = Label(self.root, font=("arial 15 "), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=220, width=150, height=50)
        self.course = Label(self.root, font=("arial 15 "), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=220, width=150, height=50)
        self.mark_obtain = Label(self.root, font=("arial 15"), bg="white", bd=2, relief=GROOVE)
        self.mark_obtain.place(x=600, y=220, width=150, height=50)
        self.full_mark = Label(self.root, font=("arial 15 ",), bg="white", bd=2, relief=GROOVE)
        self.full_mark.place(x=750, y=220, width=150, height=50)
        self.percent = Label(self.root, font=("arial 15 "), bg="white", bd=2, relief=GROOVE)
        self.percent.place(x=900, y=220, width=150, height=50)

    def search(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()
        try:
            if self.search_var.get() == "":
                messagebox.showerror("Error", "Roll No. Required", parent=self.root)
            else:
                cursor.execute("SELECT * FROM result WHERE roll=?", (self.search_var.get(),))
                rows = cursor.fetchone()
                if rows is not None:
                    self.roll.config(text=rows[0])
                    self.name.config(text=rows[1])
                    self.course.config(text=rows[2])
                    self.mark_obtain.config(text=rows[3])
                    self.full_mark.config(text=rows[4])
                    self.percent.config(text=rows[5])
                else:
                    messagebox.showerror("Error", "No Record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}")

    def clear(self):
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.mark_obtain.config(text="")
        self.full_mark.config(text="")
        self.percent.config(text="")
        self.search_var.set("")

    def confirm_delete(self):
        if self.search_var.get() == "":
            messagebox.showerror("Error", "Roll No. Required", parent=self.root)
        else:
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
            if confirm:
                self.delete_record()

    def delete_record(self):
        try:
            connect = sqlite3.connect(database="rms.db")
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM result WHERE roll=?", (self.search_var.get(),))
            row = cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Record not found", parent=self.root)
            else:
                cursor.execute("DELETE FROM result WHERE roll=?", (self.search_var.get(),))
                connect.commit()
                messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}")


if __name__ == "__main__":
    r = Tk()
    obj = view_result_class(r)
    r.mainloop()