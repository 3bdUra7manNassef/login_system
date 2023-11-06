#---- login system : برنامج تسجيل الدخول ----#
#todo i want to lb`s  btn`s  icon  entry  frame  window and check_btn#

from tkinter import*

#*---- window : النافذة ----*#
wind = Tk()
wind.title('LOGIN SYSTEM')
wind.config(background = '#BFC9CA')
wind.resizable(False,False)
wind.geometry('500x500+350+100')
wind.iconbitmap('C:\\Users\\amzn1\\Downloads\\icon.ico')

#*---- title : العنوان -----*#
title = Label(wind, text='LOGIN SYSTEM',bg='black',fg='white',font="Times 17 bold")
title.pack(side='top',fill=X)

#*---- frame ----*#
fr = Frame(wind, width=300, height=350 ,bg='whitesmoke')
fr.pack(pady=30)

#*---- image : الصورة ----*#
image = PhotoImage(file='C:\\Users\\amzn1\\Downloads\\295128 (1).png')
open_image = Label(fr,image= image)
open_image.place(x=100,y=0)

#*---- entry : مدخلات ----*#

usr_name = Entry(fr,justify='center')
usr_name.place(x=134,y=145)

password = Entry(fr,justify='center')
password.place(x=134,y=185)

#*---- label ----*#

lb1 = Label(fr,text='USERNAME', font=('Courier 15'))
lb1.place(x=10,y=140)

lb2 = Label(fr,text='PASSWORD', font=('Courier 15'))
lb2.place(x=10,y=180)

#*---- buttons : الازرار ----*#
login = Button(fr,text='LOGIN',font=("Times 15 bold"),width='11',bg='#1E8449')
login.place(x=15,y=260)

sign_in = Button(fr,text='SIGN IN',font=("Times 15 bold"),width='11',bg='#C0392B')
sign_in.place(x=145,y=260)

#*----check button----*#
checkbutton = Checkbutton(fr,text='forget password',font=('Courier 15'),bg='whitesmoke')
checkbutton.place(x=10,y=220)

wind.mainloop()