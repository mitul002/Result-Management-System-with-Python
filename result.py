from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class result_class:
    def __init__(self, r):
        self.root = r
        self.root.geometry("1180x600")
        self.root.title("Result")
        self.root.config(bg="#d3d9e2")
        self.root.focus_force() # to make focus forcefully from dashboard

        title = Label(self.root,text="Manage Result", font="arial 15 bold", bg="#ef5350", fg="white")
        title.place(x=10, y=10, relwidth=0.985, height=45)



        # =========Select Student============
        self.student_list = []
        self.fetch_student()

        select_student = Label(self.root, text="Select Student :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        select_student.place(x=10, y=80, width=200, height=55)

        self.select_student_var = StringVar()
        self.select_student_entry = ttk.Combobox(self.root, textvariable=self.select_student_var, font="arial 13 ",
                                              state='readonly',
                                              values=self.student_list)  # Entry() is used for making input box
        self.select_student_entry.place(x=210, y=80, width=200, height=55)
        self.select_student_entry.set("           Select")


        # =========Student Name============
        name = Label(self.root, text="Name :", font="arial 13 ", bg="#fffcf2", bd="1",relief=RIDGE)
        name.place(x=10, y=145, width=200, height=55)

        self.name_var = StringVar()
        self.name_entry = Entry(self.root, textvariable=self.name_var, font="arial 13 ", bg="#eee9dc",state='readonly')  # Entry() is used for making input box
        self.name_entry.place(x=210, y=145, width=330, height=55)

        # =========COURSE NAME============


        course_name = Label(self.root, text="Course Name :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        course_name.place(x=10, y=210, width=200, height=55)

        self.course_name_var = StringVar()
        self.course_name_entry = Entry(self.root, textvariable=self.course_name_var, font="arial 13 ",state='readonly')  # Entry() is used for making input box
        self.course_name_entry.place(x=210, y=210, width=330, height=55)


########


        mark_obtain = Label(self.root, text="Mark Obtained :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        mark_obtain.place(x=10, y=275, width=200, height=55)

        self.mark_obtain_var = StringVar()
        self.mark_obtain_entity = Entry(self.root, textvariable=self.mark_obtain_var, font="arial 13 ",
                                       bg="#eee9dc")
        self.mark_obtain_entity.place(x=210, y=275, width=330, height=55)

##########

        full_mark = Label(self.root, text="Full Mark :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        full_mark.place(x=10, y=340, width=200, height=55)

        self.full_mark_var = StringVar()
        self.full_mark_entry = Entry(self.root, textvariable=self.full_mark_var, font="arial 13 ",
                                       bg="#eee9dc")  # Entry() is used for making input box
        self.full_mark_entry.place(x=210, y=340, width=330, height=55)


        self.add=Button(self.root,text="Add ",font="arial 13 bold",bg="#FFBE00",fg="white",cursor="hand2", command=self.add)
        self.add.place(x=10,y=410,width=530,height=55)

###
        # Search Panel
        self.search_var = StringVar()
        btn_search = Button(self.root, text="Search", font="arial 13 bold", bg="dodgerblue", fg="white", cursor="hand2", command=self.search).place(x=415, y=80, width=125, height=55)


####Image

        # ==========Image=========
        self.img = Image.open("Images/result.jpg")
        self.img = self.img.resize((600, 380), )
        self.img = ImageTk.PhotoImage(self.img)

        self.img_label = Label(self.root, image=self.img).place(x=560, y=80)

    def fetch_student(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()

        try:
            cursor.execute("SELECT roll FROM student")
            rows = cursor.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.student_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}")

    def add(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()

        try:
            # Message box for no course entry
            if self.name_var.get() == "":
                messagebox.showerror("Error", "Search student record", parent=self.root)
            # Message box for entering an existing course
            else:
                cursor.execute("SELECT * FROM result WHERE roll=? AND course=?",
                               (self.select_student_var.get(), self.course_name_var.get()))
                row = cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Result already present", parent=self.root)
                else:
                    percent = (int(self.mark_obtain_var.get()) * 100 / int(self.full_mark_var.get()))
                    cursor.execute(
                        "INSERT INTO result (name, course, marks, full_marks, percent) VALUES (?, ?, ?, ?, ?)",
                        (
                            self.name_var.get(),
                            self.course_name_var.get(),
                            self.mark_obtain_var.get(),
                            self.full_mark_var.get(),
                            str(percent)
                        )
                        )

                    connect.commit()
                    messagebox.showinfo("Success", "Result Added Successfully", parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



    def search(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()

        try:
            cursor.execute("SELECT name, course FROM student WHERE roll=?", (self.select_student_var.get(),))
            rows = cursor.fetchone()
            if rows != None:
                self.name_var.set(rows[0])
                self.course_name_var.set(rows[1])
            else:
                messagebox.showerror("Error", "No Record found", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}")







if __name__ == "__main__":
    r = Tk()
    obj = result_class(r)
    r.mainloop()