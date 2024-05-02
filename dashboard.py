from tkinter import *
from PIL import Image, ImageTk
from course import course_class
from student import student_class
from result import result_class
from viewResult import view_result_class

class RMS:
    def __init__(self, r):
        self.root = r
        self.root.geometry("1920x1280")
        self.root.title("Result Management System")
        self.root.config(bg="#d3d9e2")


        # Load the logo
        self.logo = ImageTk.PhotoImage(file="Images/logo.png")

        # Title Label
        title_label = Label(image=self.logo, text="Student Result Management System", padx=10, compound=LEFT, font="arial 20 bold", bg="#00849f", fg="white")
        title_label.place(x=0, y=0, relwidth=1, height=70)

        #logout button
        logout = Button(title_label, text="Log Out", font="arial 10 bold",bg="#00849f",fg="white", cursor="hand2") #padding not works in when we use width,height. it works in grid()
        logout.place(x=1330, y=15, width=100, height=40)




        dashboard = Label(text="Dashboard", font="arial 15", bg="#9DA0A4", fg="white")
        dashboard.place(x=0, y=85, relwidth=1, height=45)
        # Menu LabelFrame

        menu_frame = LabelFrame(self.root, text="Menu", font="arial 10 bold",  bg="white")
        menu_frame.place(x=10, y=140, relwidth=0.98, height=110)

        # Button inside Menu LabelFrame
        course = Button(menu_frame, text="Course", font="arial 13 bold",bg="#42a5f5",fg="white", cursor="hand2", command=self.add_course) #padding not works in place(). it works in grid()
        course.place(x=60, y=5, width=300, height=70)

        student = Button(menu_frame, text="Student", font="arial 13 bold",bg="#7e57c2",fg="white", cursor="hand2", command=self.add_student)
        student.place(x=410, y=5, width=300, height=70)

        result = Button(menu_frame, text="Result", font="arial 13 bold",bg="#ef5350",fg="white", cursor="hand2", command=self.add_result)
        result.place(x=770, y=5, width=300, height=70)

        view_result = Button(menu_frame, text="View Student Result", font="arial 13 bold",bg="#26c6da",fg="white", cursor="hand2", command=self.view_result)
        view_result.place(x=1130, y=5, width=300, height=70)


        frame1=Frame(self.root, bg="#eee9dc")
        frame1.place(x=1100, y=270, width=410, height=500)



        students = Label(frame1, text="Total Students\n[0]", font="arial 15 bold", bg="tomato", fg="white", bd="10",relief=RIDGE)
        students.place(x=50, y=50, width=300, height=100)


        courses=Label(frame1, text="Total Courses\n[0]", font="arial 15 bold", bg="dodgerblue",fg="white",bd="10", relief=RIDGE)
        courses.place(x=50,y=200, width=300, height=100)

        results = Label(frame1, text="Total Results\n[0]", font="arial 15 bold", bg="slateblue", fg="white", bd="10",relief=RIDGE)
        results.place(x=50, y=350, width=300, height=100)



        footer=Label(self.root,text="© All Right Reserved", font="arial 10",fg="white",bg="navy", pady=5).pack(side=BOTTOM,fill="x")


#call course class
    def add_course(self):
        self.new_window=Toplevel(self.root)
        self.new_object=course_class(self.new_window)

# call student class
    def add_student(self):
            self.new_window = Toplevel(self.root)
            self.new_object = student_class(self.new_window)

#call result class
    def add_result(self):
        self.new_window=Toplevel(self.root)
        self.new_object=result_class(self.new_window)

#call view result class
    def view_result(self):
        self.new_window=Toplevel(self.root)
        self.new_object=view_result_class(self.new_window)


if __name__ == "__main__":
    r = Tk()
    obj = RMS(r)
    r.mainloop()
