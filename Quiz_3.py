from tkinter import *
import sqlite3
'''Connecting to database for inserting data inside'''
def ex(w2,E1,E2,E3,E4):
        conn = sqlite3.connect("Quiz.db")
        conn.execute("create table if not exists quiz(Sl_no int,ques varchar(100),opt1 varchar(25),opt2 varchar(25),corr int);")
        s = E1.get()
        cd = conn.execute("select * from quiz;")
        c = len(cd.fetchall())
        c = c+1
        conn.execute("insert into quiz values(?,?,?,?,?);",(c,E1.get(),E2.get(),E3.get(),int(E4.get())))
        conn.commit()
        conn.close()
        w3 = Tk()
        def ex1():
            w3.destroy()
            E1.set("")
            E2.set("")
            E3.set("")
            E4.set("")
        def ex2():
            w3.destroy()
            w2.destroy()
        w3.geometry("250x125")
        L5 = Label(w3,text="Want to add more ?").place(x=10,y=10)
        b4 = Button(w3, text="Yes",command = ex1).place(x=50, y=50)
        b5 = Button(w3, text="No",command =ex2).place(x=100, y=50)
        w3.mainloop()
#The set window method 
def set():
    w2 = Tk()
    w2.geometry("500x250")
    E1 = StringVar()
    E2 = StringVar()
    E3 = StringVar()
    E4 = StringVar()
    L2 = Label(w2,text="Enter a Question ", ).place(x=0, y=10)
    e1 = Entry(w2,textvariable = E1,justify =LEFT,width = 50)
    e1.place(x=100,y=10)
    L3 = Label(w2,text="Option 1 :", ).place(x=0, y=50)
    e2 = Entry(w2,textvariable = E2).place(x=100,y=50)
    L4 = Label(w2,text="Option 2 :", ).place(x=0, y=100)
    e3 = Entry(w2,textvariable = E3).place(x=100,y=100)
    L5 = Label(w2,text="Correct Option :", ).place(x=0, y=150)
    e4 = Entry(w2,textvariable = E4).place(x=100,y=150)
    b3 = Button(w2, text="submit",command = lambda : ex(w2,E1,E2,E3,E4)).place(x=100, y=200)
    w2.mainloop()
#performs task for the next button
def nex(window,conn,i,n,ans):
    window.destroy()
    if i <n:
        i = i + 1
        star(ans,conn,i,n)
    else:
        return
#performs task for the previous button
def prev(window,conn,i,n,ans):
    window.destroy()
    if i > 1:
        i = i - 1
        star(ans,conn,i,n)
    else:
        star(ans,conn,1,n) 
'''Connecting to database to read data which is used in the Quiz.'''
def star(ans,conn,i,n):
    window = Tk()
    window.geometry("600x300")
    radio = IntVar()
    def exe():
        '''if radio.get() == rows[4]:
            print("correct") 
        else:
            print("Wrong")'''
        ans[i-1] = radio.get()    
    cursor = conn.execute("select * from quiz where Sl_no = " + str(i) + ";")
    for rows in cursor:
        L1 = Label(text = "Q " + rows[1] ).place(x=0,y=0)
        r1 = Radiobutton(window,text = "1 "+ rows[2],variable = radio, value = 1).place(x = 0,y = 25)
        r2 = Radiobutton(window,text = "2 "+ rows[3],variable = radio, value = 2).place(x = 0,y = 50)
        radio.set(ans[i-1])
    b1 = Button(window,text = "Submit",command = exe).place(x=300,y=150)
    b2 = Button(window,text = "  Next  ",command = lambda : nex(window,conn,i,n,ans)).place(x = 220,y=150)
    b3 = Button(window,text = "Previous",command = lambda : prev(window,conn,i,n,ans)).place(x=150,y=150)
    if(ans[i-1]>0):
        L2 = Label(text = "answer placed ").place(x =210,y = 200) 
    window.mainloop()
#Results of the Quiz
def result(ans,conn,n):
    window = Tk()
    c = 0
    t = n*10
    window.geometry("600x300")
    for i in range(1,n+1):
        cursor = conn.execute("select * from quiz where Sl_no = " + str(i) + ";")
        for rows in cursor:
            if ans[i-1] == rows[4]:
                c += 10
    L1 = Label(window,text = "YOUR SCORE:",font = ("TimesNewRoman",30)).place(x=150,y=0)
    L2 = Label(window,text = str(c) + "/" + str(t),font = ("TimesNewRoman",60)).place(x=200,y=100)    
    window.mainloop()
#Setting Questions in the quiz
def set1(w1):
    w1.destroy()
    set()
    start()
#Attemptig the Quiz    
def start1(w1):
    w1.destroy()
    conn = sqlite3.connect("Quiz.db")
    cd = conn.execute("select * from quiz;")
    n = len(cd.fetchall())
    ans = [0] * n
    #for i in range(1,n+1):
    star(ans,conn,1,n)
    result(ans,conn,n)
    conn.close()
    start()
def start():
    w1 = Tk()
    w1.geometry("500x250")
    L1 = Label(w1,text = "QUIZ-RELOADED",font = ("TimesNewRoman",30)).place(x=100,y=0)
    b1 = Button(w1,text = "START",font = ("TimesNewRoman",15),command = lambda :start1(w1)).place(x = 150,y=100)
    b2 = Button(w1,text = "SET",font = ("TimesNewRoman",15),command = lambda :set1(w1)).place(x = 300,y=100)
    w1.mainloop()    
#the frontside of the app
start()