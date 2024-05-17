from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class student_class:
    def __init__(self, r):
        self.root = r
        self.root.geometry("1380x600")
        self.root.title("Student")
        self.root.config(bg="#d3d9e2")
        self.root.focus_force() # to make focus forcefully from dashboard

        title = Label(self.root,text="Manage Student", font="arial 15 bold", bg="#7e57c2", fg="white")
        title.place(x=10, y=10, relwidth=0.985, height=45)

#=========ROLL============
        roll = Label(self.root, text="Roll :", font="arial 13 ", bg="#fffcf2", bd="1",relief=RIDGE)
        roll.place(x=10, y=80, width=150, height=55)

        self.roll_var = IntVar()
        self.roll_entry = Entry(self.root, textvariable=self.roll_var, font="arial 13 ", bg="#eee9dc")  # Entry() is used for making input box
        self.roll_entry.place(x=160, y=80,  width=170, height=55)

# =========NAME============

        name = Label(self.root, text="Name :", font="arial 13 ", bg="#fffcf2", bd="1",relief=RIDGE)
        name.place(x=10, y=145, width=150, height=55)

        self.name_var = StringVar()
        self.name_entry = Entry(self.root, textvariable=self.name_var, font="arial 13 ", bg="#eee9dc")  # Entry() is used for making input box
        self.name_entry.place(x=160, y=145,  width=170, height=55)
#=========EMAIL============

        email = Label(self.root, text="Email :", font="arial 13 ", bg="#fffcf2", bd="1",relief=RIDGE)
        email.place(x=10, y=210, width=150, height=55)

        self.email_var = StringVar()
        self.email_entry = Entry(self.root, textvariable=self.email_var, font="arial 13 ", bg="#eee9dc")  # Entry() is used for making input box
        self.email_entry.place(x=160, y=210,  width=170, height=55)

# =========GENDER============

        gender = Label(self.root, text="Gender :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        gender.place(x=10, y=275, width=150, height=55)

        self.gender_var = StringVar()
        self.gender_entry = ttk.Combobox(self.root, textvariable=self.gender_var, font="arial 13 ",state='readonly',
                                 values=("Male","Female"))  # Entry() is used for making input box
        self.gender_entry.place(x=160, y=275, width=170, height=55)
 #=========BIRTHDAY============

        birthday = Label(self.root, text="Birthday :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        birthday.place(x=350, y=80, width=150, height=55)

        self.birthday_var = StringVar()
        self.birthday_entry = Entry(self.root, textvariable=self.birthday_var, font="arial 13 ",
                                 bg="#eee9dc")  # Entry() is used for making input box
        self.birthday_entry.place(x=500, y=80, width=170, height=55)
#=========CONTACT============

        contact = Label(self.root, text="Contact :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        contact.place(x=350, y=145, width=150, height=55)

        self.contact_var = IntVar()
        self.contact_entry = Entry(self.root, textvariable=self.contact_var, font="arial 13 ",
                                 bg="#eee9dc")  # Entry() is used for making input box
        self.contact_entry.place(x=500, y=145, width=170, height=55)
#=========COURSE NAME============

        course_name = Label(self.root, text="Course Name :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        course_name.place(x=350, y=210, width=150, height=55)

        self.course_name_var = StringVar()
        self.course_name_entry = Entry(self.root, textvariable=self.course_name_var, font="arial 13 ",
                                       bg="#eee9dc")  # Entry() is used for making input box
        self.course_name_entry.place(x=500, y=210, width=170, height=55)
#=========CITY============
        city = Label(self.root, text="City :", font="arial 13 ", bg="#fffcf2", bd="1", relief=RIDGE)
        city.place(x=350, y=275, width=150, height=55)

        self.city_var = StringVar()
        self.city_entry = Entry(self.root, textvariable=self.city_var, font="arial 13 ",
                                 bg="#eee9dc")  # Entry() is used for making input box
        self.city_entry.place(x=500, y=275, width=170, height=55)

#=========ADDRESS============

        address = Label(self.root, text="Address :", font="arial 13 ", bg="#fffcf2", bd="1",relief=RIDGE)
        address.place(x=10, y=340, width=150, height=100)

        self.address_entry = Text(self.root, font="arial 13 ", bg="#eee9dc")  # Entry() is used for making input box
        self.address_entry.place(x=160, y=340,  width=510, height=100)


# All buttons
        ButtonFrame=Frame(self.root, bg="white")
        ButtonFrame.place(x=10, y=445, width=660, height=70)


        self.add=Button(ButtonFrame,text="Save",font="arial 13 bold",bg="dodgerblue",fg="white",cursor="hand2",command=self.add)
        self.add.place(x=15,y=10,width=200,height=50)

        self.update=Button(ButtonFrame,text="Update",font="arial 13 bold",bg="slateblue",fg="white",cursor="hand2", command=self.update)
        self.update.place(x=230,y=10,width=200,height=50)

        self.delete=Button(ButtonFrame,text="Delete",font="arial 13 bold",bg="tomato",fg="white",cursor="hand2", command=self.delete)
        self.delete.place(x=445,y=10,width=200,height=50)




        # Search Panel
        self.search_var = StringVar()
        search_label = Label(self.root, text="Course Name: ", font="arial 13", bg="white", bd="1", relief=RIDGE).place(x=700, y=80, height=55, width=160)
        search_entry = Entry(self.root, textvariable=self.search_var, font="arial 13", bg="white").place(x=870, y=80, width=360, height=55)
        btn_search = Button(self.root, text="Search", font="arial 13 bold", bg="dodgerblue", fg="white", cursor="hand2",command=self.search).place(x=1220, y=80, width=150, height=55)


        #Course frame
        self.courseFrame=Frame(self.root, bd=2, relief=RIDGE)
        self.courseFrame.place(x=700,y=140,width=670 ,height=310)


        # Headings and Coloumns for the tables

        self.CourseTable=ttk.Treeview(self.courseFrame,columns=("cid","name","duration","charges","address"))
        self.CourseTable.pack(fill=BOTH, expand=1)

        self.CourseTable.heading("cid", text="Course ID")
        self.CourseTable.heading("name", text="Name")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("address", text="address")

        self.CourseTable["show"] = "headings"
        self.CourseTable.column("cid", width=100)
        self.CourseTable.column("name", width=100)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("address", width=150)
        self.show_courses()  #all previous stored data will show


##################
#add course
    def add(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()

        try:
            # Message box for no course entry
            if self.roll_var.get() == "":
                messagebox.showerror("Error", "Course name required", parent=self.root)
            # Message box for entering an existing course
            else:
                cursor.execute("SELECT * FROM course WHERE name=?", (self.roll_var.get(),))
                row = cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Course name already exists", parent=self.root)
                else:
                    cursor.execute("INSERT INTO course (name, duration, charges, address) VALUES (?, ?, ?, ?)",
                                   (
                                    self.roll_var.get(),
                                    self.name_var.get(),
                                    self.email_var.get(),
                                    self.address_entry.get("1.0", END)
                                                )
                                   )

                    connect.commit()
                    messagebox.showinfo("Success", "Course Added Successfully", parent=self.root)
                    self.show_courses()  #when we add data it will show in the table instantly


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



#update course
    def update(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()

        try:
            # Message box for no course entry
            if self.roll_var.get() == "":
                messagebox.showerror("Error", "Course name required", parent=self.root)
            # Message box for entering an existing course
            else:
                cursor.execute("SELECT * FROM course WHERE name=?", (self.roll_var.get(),))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select course from list", parent=self.root)
                else:
                    cursor.execute("UPDATE course SET duration =? , charges =? , address =? where name =? ",
                                   (

                                    self.name_var.get(),
                                    self.email_var.get(),
                                    self.address_entry.get("1.0", END),
                                    self.roll_var.get()
                                                )
                                   )

                    connect.commit()
                    messagebox.showinfo("Success", "Course Update Successfully", parent=self.root)
                    self.show_courses()  #when we add data it will show in the table instantly


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




    # delete course
    def delete(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()

        try:
            # Message box for no course entry
            if self.roll_var.get() == "":
                messagebox.showerror("Error", "Course name required", parent=self.root)
            # Message box for entering an existing course
            else:
                cursor.execute("SELECT * FROM course WHERE name=?", (self.roll_var.get(),))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Select course from list", parent=self.root)
                else:
                    cursor.execute("DELETE FROM course WHERE name=?",
                                      (self.roll_var.get(),)
                                   )

                    connect.commit()
                    messagebox.showinfo("Success", "Course Delete Successfully", parent=self.root)
                    self.show_courses()  # when we add data it will show in the table instantly


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")




    def show_courses(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()

        try:
            cursor.execute("SELECT * FROM course")
            rows = cursor.fetchall()

            self.CourseTable.delete(*self.CourseTable.get_children())

            for row in rows:
                self.CourseTable.insert('', 'end', values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}")

    def search(self):
        connect = sqlite3.connect(database="rms.db")
        cursor = connect.cursor()

        try:
            # Fetch courses matching the search criteria
            cursor.execute("SELECT * FROM course WHERE name LIKE ?", ('%' + self.search_var.get() + '%',))
            rows = cursor.fetchall()

            # Clear the existing data in the table widget
            self.CourseTable.delete(*self.CourseTable.get_children())

            # Insert fetched courses into the table widget
            for row in rows:
                self.CourseTable.insert('', 'end', values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error occurred: {str(ex)}")


if __name__ == "__main__":
    r = Tk()
    obj = student_class(r)
    r.mainloop()