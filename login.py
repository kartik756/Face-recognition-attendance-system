from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1300x650+0+0")

        self.bg=ImageTk.PhotoImage(file=r"college_images\di.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        

        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=130,width=340,height=450 )

        img1=Image.open(r"college_images\logo.jpg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=630,y=130,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=70,y=145)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black")
        password.place(x=70,y=215)
        
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)

        #=====icon image=======
        img2=Image.open(r"college_images\username.png")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=550,y=280,width=25,height=25)

        img3=Image.open(r"college_images\password.jpg")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=550,y=350,width=25,height=25)

        #login button
        loginbtn=Button(frame,text="Login ",borderwidth=3,relief=RAISED,command=self.login,font=("times new roman",20,"bold"),fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register button
        registerbtn=Button(frame,text="New User Register ",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        registerbtn.place(x=15,y=350,width=160)

        #forget pass btn
        registerbtn=Button(frame,text="Forget Password",command=self.forgot__password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        registerbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All feild required")

        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","welcome to Face recognition system")
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()

                                                                                      ))
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

            #========reset password====
    def reset_pass(self):
                if self.combo_security_Q.get()=="Select":
                    messagebox.showerror("Error","Select the security question",parent=self.root2)
                elif self.txt_security.get()=="":
                    messagebox.showerror("Error","Please enter the answer",parent=self.root2)
                elif self.txt_newpass.get()=="":
                    messagebox.showerror("Error","Please enter the new password",parent=self.root2)
                else:
                    try:
                        conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
                        my_cursor=conn.cursor()
                        query=("Select * from register where email=%s and securityQ=%s and securityA=%s")
                        value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        if row==None:
                            messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
                        else:
                            query=("update register set password=%s where email=%s")
                            value=(self.txt_newpass.get(),self.txtuser.get())
                            my_cursor.execute(query,value)

                            conn.commit()
                            conn.close()
                            
                            messagebox.showinfo("Info","your pasword has been reset,please login new password",parent=self.root2)
                            self.root2.destroy()
                            self.txtuser.focus()
                    except Exception as es:
                        messagebox.showerror("Error",f"Error Due To:{str(es)}",parent=self.root2)        
                    


            #=====forgot password window==============
    def forgot__password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
           # print(row)


            if row==None:
               messagebox.showerror("My Error","Please enter valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","your birth place","your girlfriend name","your pet name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)


                

        

                
            

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1300x650+0+0")

    #=============Variable=========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self._var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()   



    #==========bg image==================
        self.bg=ImageTk.PhotoImage(file=r"college_images\di.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

    #===========left image=================
        self.bg1=ImageTk.PhotoImage(file=r"college_images\img1.jpeg")
        left_lbl=Label(self.root,image=self.bg)
        left_lbl.place(x=50,y=100,width=470,height=550)

    #====== main frame===================
        frame=Frame(self.root,bg="white")
        frame.place(x=240,y=60,width=800,height=550)
        registre_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        registre_lbl.place(x=20,y=20)

    #===========label and entry===========
    #====================row1=====
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")  
        fname.place(x=50,y=100)  

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last name",font=("times new roman",15,"bold"),bg="white")  
        l_name.place(x=370,y=100)  

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

    #=====row2=
        contact=Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

    #=========row3=========
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self._var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","your birth place","your girlfriend name","your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

    #=====row4======
        pswd=Label(frame,text="password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.confim_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.confim_pswd.place(x=370,y=340,width=250)

    #==== check button==========
        self.var_check=IntVar()
        Checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        Checkbtn.place(x=50,y=380)

    #====button==============
        img=Image.open(r"college_images\register_now.jpg")
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"college_images\login_now.jpg")
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)

        #=====function declaration====
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self._var_securityQ.get()=="Select":
            messagebox.showerror("Error","All field are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree your terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Test@123",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another Email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self._var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()


            




















if __name__=="__main__":
    main()
    
