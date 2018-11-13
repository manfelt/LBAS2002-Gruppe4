import sys
import time
from tkinter import *

from datetime import date
today = date.today()

print ("test")
print (today)

def value1 ():
    num1.set(today)
    return
def value2():
    today = time.asctime(time.localtime(time.time()))
    num1.set(today)
    return

root = Tk()
root.title("Date and Time")
root.geometry('450x450+400+150')
frame = Frame(root)
frame.pack()

#root.title(today) ('Date and Time')

num1=StringVar()
radbtn = StringVar()
radbtn.set(None)

frame1 = Frame(root)
frame1.pack( side = TOP )

label1=Label(frame, text='se dagens dato', font=72, fg='Black', relief=RAISED)
label1.pack( side = TOP)
label1=Label(frame1,text='\n')
label1.pack( side = TOP)

txtDisplay=Entry(frame1,textvariable = num1 ,bd=30,insertwidth =1,font = 12 ,justify= 'center')
txtDisplay.pack( side = TOP)

radio1= Radiobutton(frame1, text="Local Time", variable = radbtn,value="Local Time", command=value2).pack(side =BOTTOM)

button1 = Button(frame1, padx=16, pady=16, bd=8, text="Todays Date is", bg='black', fg='white', activebackground='Gray')
button1.pack(side =BOTTOM)
radio1= Radiobutton(frame1, text="My Time", variable = radbtn, value="My Time").pack(side =BOTTOM)

root.mainloop()