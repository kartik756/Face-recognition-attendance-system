import tkinter
from help import Help
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from train import train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self , root):
        self.root=root
        self.root.geometry("1300x650+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"college_images\topL.jpg")
        img=img.resize((450,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0, width=450,height=130)

        #second image
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((450,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0, width=450,height=130)

        #third image
        img2=Image.open(r"college_images\topR.jpg")
        img2=img2.resize((450,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0, width=450,height=130)

        #bg image
        img3=Image.open(r"college_images\Bg3.jpg")
        img3=img3.resize((1300,650),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130, width=1300,height=650)

        title_lbl=Label(bg_img,text="FACE RECOGNITION BASED ATTENDANCE SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        #student button
        img4=Image.open(r"college_images\Student.png")
        img4=img4.resize((220,210),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details ,cursor="hand2")
        b1.place(x=84,y=60,width=220,height=210)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=84,y=240,width=220,height=40)
        
        #Detect face
        img5=Image.open(r"college_images\Face_detector.jpg")
        img5=img5.resize((220,210),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=388,y=60,width=220,height=210)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=388,y=240,width=220,height=40)

        #Attendance face button
        img6=Image.open(r"college_images\Attendance.jpg")
        img6=img6.resize((220,210),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=672,y=60,width=220,height=210)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=672,y=240,width=220,height=40)

         #Help face button
        img7=Image.open(r"college_images\Help.jpg")
        img7=img7.resize((220,210),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=976,y=60,width=220,height=210)

        b1_1=Button(bg_img,text="Help",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=976,y=240,width=220,height=40)

         #Train face button
        img8=Image.open(r"college_images\Train_data.png")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=84,y=300,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=84,y=480,width=220,height=40)

         #Photos face button
        img9=Image.open(r"college_images\BestFacialRecognition.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=388,y=300,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=388,y=480,width=220,height=40)

         #Developer face button
        img10=Image.open(r"college_images\Developer.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=672,y=300,width=220,height=220)

        b1_1=Button(bg_img,text="Developers",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=672,y=480,width=220,height=40)

         #Exit face button
        img11=Image.open(r"college_images\Exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=976,y=300,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=976,y=480,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return



#========================function button==================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)  

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window) 


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
