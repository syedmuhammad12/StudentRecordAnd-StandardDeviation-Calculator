from csv import *
from tkinter import *
from tkinter.messagebox import showinfo
def filemake():
     with open("record.csv","w",newline="") as f:
          write = writer(f)
          write.writerow(["Student Name","Roll No","Marks"])

def entry():
     try:
          with open("record.csv","r+") as f:
               pass
          with open("record.csv","a+",newline="") as f:
               write = writer(f)
               write.writerow([f"{name.get()}",f"{roll.get()}",f"{marks.get()}"])
     except:
          showinfo(message="Please create a file first")

def avg():
     try:
          with open("record.csv","r+") as f:
               content = reader(f)
               c = []
               for i in content:
                    c.append(i)
          
          count = 0
          sum = 0
          for i in range(len(c)):
             if i>=1:
                 sum+=float(c[i][2])
                 count+=1
          avg = sum/count
          showinfo(message=f"The average marks of the class is {avg}")
     except:
          showinfo(message="No file found")

def sd():
     try:
          with open("record.csv","r+") as f:
               content = reader(f)
               c = []
               for i in content:
                    c.append(i)
          
          count = 0
          sum = 0
          for i in range(len(c)):
             if i>=1:
                 sum+=float(c[i][2])
                 count+=1
          avg = sum/count
          counter = 0
          for i in range(len(c)):
             if i>=1:
                 counter+=(float(c[i][2])-avg)**2
          sd = round((counter/(len(c)-2))**0.5,2)
          showinfo(message=f"Student deviation is {sd}")
     except:
          showinfo(message="No file found")

a = Tk()
a.title("Database")
a.geometry("820x620+300+60")
a.maxsize("820","620")
a.minsize("820","620")
a.configure(bg="#9BCFD0")
a.iconbitmap("icon.ico")
name = StringVar()
roll = StringVar()
marks = StringVar()
l = Label(a,text= "Students Record",font=("Times New Roman","35","bold"),background="#9BCFD0")
l.pack()
f = Frame(a,background="#9BCFD0")
l = Label(f,text="Want to make a new file?",font="lucids 11 bold",background="#9BCFD0")
l.pack(side=LEFT,anchor="w",padx=30,pady=10)
b = Button(a,text="Create File First",font="lucida 11 bold",borderwidth=5,relief="groove",command=filemake) 
b.pack(side=RIGHT,anchor="n",pady=20,padx=50)
f.pack(pady= 20,anchor="w",padx=20)
f = Frame(a,background="#9BCFD0")
l = Label(f,text="Enter name of the student:",font="lucids 11 bold",background="#9BCFD0")
l.pack(side=LEFT,anchor="w",padx=30)
e = Entry(f,font="lucida 11 bold",textvar=name)
e.pack(ipadx=20,fill=X,padx=20)
f.pack(pady= 20,anchor="w",padx=20)
f = Frame(a,background="#9BCFD0")
l = Label(f,text="Enter Roll no of the student:",font="lucids 11 bold",background="#9BCFD0")
l.pack(side=LEFT,anchor="w",padx=30)
e = Entry(f,font="lucida 11 bold",textvar=roll)
e.pack(ipadx=20,fill=X,padx=6)
f.pack(pady= 20,anchor="w",padx=20)
f = Frame(a,background="#9BCFD0")
l = Label(f,text="Enter marks of the student:",font="lucids 11 bold",background="#9BCFD0")
l.pack(side=LEFT,anchor="w",padx=30)
e = Entry(f,font="lucida 11 bold",textvar=marks)
e.pack(ipadx=20,fill=X,padx=12)
f.pack(pady= 20,anchor="w",padx=20)
b = Button(a,text="Submit Entry",font="lucida 11 bold",borderwidth=5,relief="groove",command=entry) 
b.pack(pady=10)
l = Label(a,text="Other options",font=("Times New Roman","25","bold"),background="#9BCFD0")
l.pack(anchor="w",padx=40,pady=10)
f = Frame(a,background="#9BCFD0")
l = Label(f,text="Calculate average marks",font="lucids 11 bold",background="#9BCFD0")
l.pack(side=LEFT,anchor="w",padx=40)
b = Button(a,text="Average",font="lucida 11 bold",borderwidth=5,relief="groove",command=avg) 
b.pack(anchor="n",side=RIGHT,pady=10)
f.pack(anchor="w",pady= 10,padx=10)
f = Frame(a,background="#9BCFD0")
l = Label(f,text="Calculate Standard Deviation",font="lucids 11 bold",background="#9BCFD0")
l.pack(side=LEFT,anchor="w",padx=40,pady=30)
b = Button(a,text="Standard Deviation",font="lucida 11 bold",borderwidth=5,relief="groove",command=sd) 
b.pack(side = RIGHT,pady=20)
f.pack(anchor="w",pady= 20,padx=10)
a.mainloop()
