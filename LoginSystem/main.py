from PIL import Image as PILImage, ImageTk
from tkinter import *
from tkinter import messagebox
class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        # Load the image using PILImage
        img = PILImage.open("my_image.jpeg")
        self.bg = ImageTk.PhotoImage(img)

        # Create a label to display the image and pack it to fill the entire window
        self.bg_image = Label(self.root, image=self.bg)
        self.bg_image.pack(fill="both", expand=True)

        #login frame
        Frame_login=Frame(self.root ,bg='white')
        Frame_login.place(x=330 ,y=150 ,width=500,height=400)

        #tilte
        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg='#6162FF',bg="white").place(x=90,y=30)

        subtitle= Label(Frame_login, text="Members Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white").place(x=90,y=100)
        #username
        lbl_user=Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90,y=140)
        self.username= Entry (Frame_login,font=("Goudy old style", 15), bg="#E7E6E6")

        self.username.place(x=90, y=170, width=320 ,height=35)
        # username
        lbl_password = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")

        self.password.place(x=90, y=240, width=320, height=35)
        #Button
        forget=Button(Frame_login, text="Forget Password",bd=0, font=("Goudy old style", 12), fg="#6162FF",bg="white").place(x=90, y=280)
        submit = Button(Frame_login,command=self.check_function, text="Login?", bd=0, font=("Goudy old style", 12), bg="#6162FF",fg="white",width=180 ,height=40).place(x=90,y=320,width=180,height=40)
    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.username.get()!="M.Ibrahim" or self.password.get()!="ibrahimnasir":
            messagebox.showerror("Error","Invalid Username",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"welcome{self.username.get()}")
root = Tk()
obj = login(root)
root.mainloop()
