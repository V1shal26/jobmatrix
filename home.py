from tkinter import*
from PIL import ImageTk     #pil python image lib


def Logout():
    root.destroy()
    import userSignIn

root=Tk()
root.geometry('819x461+50+50')
root.title = "UserSignIn"

bg1 = ImageTk.PhotoImage(file="images/home5.png")
bglabel=Label(root,image=bg1)
bglabel.place(x=0,y=0)

logout=Button(root,text='Logout',font=('Segoe UI Symbol',13,'bold'),fg='red',cursor='hand2',bd=0,command=Logout)
logout.place(x=700,y=10,height=30,width=100)

logouticon=PhotoImage(file='icons/logout.png')
logoutbtn=Button(root,image=logouticon,bd=0,cursor='hand2')
logoutbtn.place(x=780,y=10)
root.mainloop()
