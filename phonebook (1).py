import sqlite3
import front
from Tkinter import *
from tkMessageBox import *
root=Tk()
con=sqlite3.Connection('phonebook_11')
cur=con.cursor()
cur.execute('PRAGMA foreign_keys=ON')
cur.execute("create table if not exists detail_1(contact_id integer PRIMARY KEY AUTOINCREMENT, first_name varchar (50), last_name varchar(20), company varchar (100), address varchar(100), city varchar(50), website varchar (50), pin integer (10), birthdate varchar(20))")
cur.execute("create table if not exists phone(contact_id integer, contact_type varchar (50), phone integer (10) PRIMARY KEY, constraint f1 foreign key(contact_id) references detail_1(contact_id))")
cur.execute("create table if not exists email(contact_id integer, email_type varchar(50), email_id varchar (50) PRIMARY KEY, constraint f2 foreign key(contact_id) references detail_1(contact_id))")

img=PhotoImage(file=r'\\192.168.4.11\181b171\PhoneBook\book.gif')
Label(root, image=img).grid(row=0, column=1)
##Functions

##def add_phone():
##    bp.grid_forget()
##    o=v1.get()
##    if(o==1):
##        inn='Home'
##    elif(o==2):
##        inn='Office'
##    elif(o==3):
##        inn='Mobile'
##    p=Entry(root)
##    p.grid(row=11, column=3)
##    p1=p.get()
##    cur.execute("insert into phone (contact_type, phone) values(?,?)", (inn, p1))
##    bp2=Button(root, text="+", command=add_phone_1).grid(row=11, column=4)
##
##def add_email():
##    be.grid_forget()
##    o2=v2.get()
##    if(o2==4):
##        inn2='Personal'
##    elif(o2==5):
##        inn2='Office'
##    e=Entry(root)
##    e.grid(row=13, column=3)
##    e1=e.get()
##    cur.execute("insert into email (email_type, email_id) values(?,?)", (inn2,e1))

def save():
    try:
        cop=[str(fn.get()),str(ln.get()),str(co.get()),str(add.get()),str(cit.get()),str(web.get()),int(pin.get()),str(bd.get())]
        f=fn.get()
        l=ln.get()
        c=co.get()
        a=add.get()
        ci=cit.get()
        p=pin.get()
        w=web.get()
        b=bd.get()
        p1=root1.get()
        em1=em.get()
        cur.execute("insert into detail_1 (first_name, last_name, company, address, city, website, pin, birthdate) values(?,?,?,?,?,?,?,?)",cop)
        
        o=v1.get()
        if(o==1):
            inn='Home'
            cur.execute("insert into phone (contact_type, phone) values(?,?)", (inn, p1))
        elif(o==2):  
            inn='Office'
            cur.execute("insert into phone (contact_type, phone) values(?,?)", (inn, p1))
        elif(o==3):
            inn='Mobile'
            cur.execute("insert into phone (contact_type, phone) values(?,?)", (inn, p1))

        o2=v2.get()
        if(o2==4):
            inn1='Personal'
            cur.execute("insert into email (email_type, email_id) values(?,?)", (inn1, em1))
        elif(o2==5):
            inn1='Office'
            cur.execute("insert into email (email_type, email_id) values(?,?)", (inn1, em1))
        del cop[:]
        cur.execute('select * from detail_1,phone,email')
        n=cur.fetchall()
        fn.delete(0, END)
        ln.delete(0, END)
        co.delete(0, END)
        add.delete(0, END)
        cit.delete(0, END)
        pin.delete(0, END)
        web.delete(0, END)
        bd.delete(0, END)
        root1.delete(0, END)
        em.delete(0, END)
        v1.set(None)
        v2.set(None)    
        con.commit()
        saved()
    except:
        showerror('Try Again!', 'Looks like something went wrong')
    
def search():
    root2 = Tk()
    root2.propagate(0)
    root2.geometry('750x700')
    Label(root2,text = "Search Contact", font = 'Times 30 bold').grid(row =0, column = 2)
    Label(root2,text = "Enter Name:  ", font = 'Times 15 bold ').grid(row = 6, column = 0)
    search = Entry(root2)
    search.grid(row = 6 , column = 2)
    lab = Listbox(root2,width=60,height=30)
    lab.grid(row = 10,column = 2)
    def cclose():
            root2.destroy()
    Button(root2, text="Close", command=cclose).grid(row= 11, column=2)
    def key_press(e = 0):
        s = search.get()
        lab.delete(0,END)
        key = "select contact_id,first_name,last_name from detail_1 where first_name LIKE '%{}%' OR last_name".format(s,s)
        cur.execute(key)
        global a
        a = cur.fetchall()
        for z in range (len(a)):
            fn = a[z][1]+' '+a[z][2]
            lab.insert(0,fn)
        
    def retrieve(e = 0):
        global a
        hv = lab.curselection()
        index = hv[0]
        lab.delete(0,END)
        index = len(a) - index - 1
        cid = a[index][0]
        qq = 'select * from  detail_1 where contact_id = ?'
        cur.execute(qq,[(cid)])
        z = cur.fetchall()
        sep = 'select * from phone where contact_id = ?'
        cur.execute(sep,[(cid)])
        d = cur.fetchall()
        print d,
        sec = 'select * from email where contact_id =?'
        cur.execute(sec,[(cid)])
        c = cur.fetchall()
        print c,
        root1 = Tk()
        root1.geometry("500x500")
        Label(root1,text="Name: ",font = 20).grid(row = 2, column = 1)
        Label(root1,text = z[0][1] +' '+z[0][2],font = 20).grid(row = 2,column = 2)
        Label(root1,text = "Company Name: ",font = 20).grid(row = 3,column = 1)
        Label(root1,text = z[0][3],font = 20).grid(row = 3,column = 2)
        Label(root1,text = "City:",font = 20).grid(row = 4,column = 1)
        Label(root1,text = z[0][4],font = 20).grid(row = 4,column = 2)
        Label(root1,text = "Address: ",font = 20).grid(row = 5,column = 1)
        Label(root1,text = z[0][5],font = 20).grid(row = 5,column = 2)
        Label(root1,text = "WEBSITE URL",font = 20).grid(row = 6,column = 1)
        Label(root1,text = z[0][6],font = 20).grid(row = 6,column = 2)
        Label(root1,text = "Pin Code: ",font = 20).grid(row = 7,column = 1)
        Label(root1,text = z[0][7],font = 20).grid(row = 7,column = 2)
        Label(root1,text = "Date of Birth: ",font = 20).grid(row = 8,column = 1)
        Label(root1,text = z[0][8],font = 20).grid(row = 8,column = 2)
        Label(root1,text = "Phone Type: ",font = 20).grid(row = 9,column = 1)
        Label(root1,text = "Phone Number: ",font =20).grid(row = 10, column = 1)
        if len(d)!=0:
            Label(root1,text = d[0][1], font = 20).grid(row = 9,column = 2)
            Label(root1,text = d[0][2],font = 20).grid(row = 10, column =2)
        Label(root1,text = "Email Type: ", font = 20).grid(row = 11, column =1)
        Label(root1,text = "Email Id: ", font= 20).grid(row = 12, column = 1)
        if len(c)!=0:
            Label(root1,text = c[0][1],font = 20).grid(row = 11, column = 2)
            Label(root1,text = c[0][2],font = 20).grid(row = 12, column = 2)
        def close():
            root1.destroy()

        Button(root1, text="Close", command=close).grid(row= 13, column=2)
        
        def Delete():
            dd = "delete from detail_1 where contact_id = ?"
            cur.execute(dd,[(cid)])
            root1.destroy()
            showinfo("Deleted","Contact Deleted")
            con.commit()
        Button(root1, text="Delete", command=Delete).grid(row= 13, column=3)
        def Close():
            root1.destroy()
##        def Confirmation():
##            if True == askyesno("ASK", "Do you want to delete this contact?"):
##                Delete()
        def Deletee():
            dd = "delete from user_info where contact_id = ?"
            cur.execute(dd,[(cid)])
            con.commit()
    lab.bind('<Double-Button-1>',retrieve)
    lab.bind('<Button-1>',key_press)
    root2.bind('<Key>',key_press)

Label(root, text="First Name").grid(row=2, column=0)
Label(root, text="Last Name").grid(row=3, column=0)
Label(root, text="Company").grid(row=4, column=0)
Label(root, text="Address").grid(row=5, column=0)
Label(root, text="City").grid(row=6, column=0)
Label(root, text="PIN").grid(row=7, column=0)
Label(root, text="Website URL").grid(row=8, column=0)
Label(root, text="Birth Date").grid(row=9, column=0)
Label(root, text="Phone Number").grid(row=11, column=0)

Label(root, text=" Select Phone Type").grid(row=10, column=0)
v1=IntVar()
r1=Radiobutton(root, text="Home", variable=v1, value=1).grid(row=10, column=1)
r2=Radiobutton(root, text="Office", variable=v1, value=2).grid(row=10, column=2)
r3=Radiobutton(root, text="Mobile", variable=v1, value=3).grid(row=10, column=3)

Label(root, text=" Select Email Type").grid(row=12, column=0)
v2=IntVar()
r4=Radiobutton(root, text="Personal", variable=v2, value=4).grid(row=12, column=1)
r5=Radiobutton(root, text="Office", variable=v2, value=5).grid(row=12, column=2)
Label(root, text="Email-Id").grid(row=13, column=0)
def close1():
            root.destroy()
##Button
##bp=Button(root, text="+", command=add_phone).grid(row=11, column=2)
##be=Button(root, text="+", command=add_email).grid(row=13, column=2)
Button(root, text="Save", command=save).grid(row=14, column=0)
Button(root, text="Search", command=search).grid(row=14, column=1)
Button(root, text="Close", command=close1).grid(row=14, column=2)
#Button(root, text="Edit", command=edit).grid(row=14, column=3)

##Entry

fn=Entry(root)
fn.grid(row=2, column=1)
ln=Entry(root)
ln.grid(row=3, column=1)
co=Entry(root)
co.grid(row=4, column=1)
add=Entry(root)
add.grid(row=5, column=1)
cit=Entry(root)
cit.grid(row=6, column=1)
pin=Entry(root)
pin.grid(row=7, column=1)
web=Entry(root)
web.grid(row=8, column=1)
bd=Entry(root)
bd.grid(row=9, column=1)
root1=Entry(root)
root1.grid(row=11, column=1)
em=Entry(root)
em.grid(row=13, column=1)
##

##Popups
def saved():
    showinfo('Saved', 'Your Details are saved')
root.mainloop()
