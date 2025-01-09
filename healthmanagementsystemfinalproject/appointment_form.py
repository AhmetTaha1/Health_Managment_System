from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
    
conn = sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")


# Class for BOOKING APPOINTMENT   
class Appointment:
    def __init__(self, master):
        self.master = master
        self.master.title("HEALTH ADMINISTRATION MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="lightblue")
        self.frame = Frame(self.master, bg="lightblue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        self.pat_ID = IntVar()
        self.emp_ID = StringVar()
        self.ap_no = StringVar()
        self.ap_time = StringVar()
        self.ap_date = StringVar()
        self.des = StringVar()

        #===============TITLE==========
        self.lblTitle = Label(self.frame, text="APPOINTMENT FORM", font="Helvetica 20 bold", bg="lightblue", fg="black")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        
        #===========LABELS=============          
        self.lblpid = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblpid.grid(row=0, column=0)
        self.lblpid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_ID)
        self.lblpid.grid(row=0, column=1)
        
        self.lbldid = Label(self.LoginFrame, text="DOCTOR ID", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lbldid.grid(row=1, column=0)
        self.lbldid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_ID)
        self.lbldid.grid(row=1, column=1)

        self.lblap = Label(self.LoginFrame, text="APPOINTMENT NO", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblap.grid(row=2, column=0)
        self.lblap = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_no)
        self.lblap.grid(row=2, column=1)
            
        self.lblapt = Label(self.LoginFrame, text="APPOINTMENT TIME(HH:MM:SS)", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblapt.grid(row=0, column=2)
        self.lblapt = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_time)
        self.lblapt.grid(row=0, column=3)

        self.lblapd = Label(self.LoginFrame, text="APPOINTMENT DATE(YYYY-MM-DD)", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblapd.grid(row=1, column=2)
        self.lblapd = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_date)
        self.lblapd.grid(row=1, column=3)
        
        self.lbldes = Label(self.LoginFrame, text="DESCRIPTION", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lbldes.grid(row=2, column=2)
        self.lbldes = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.des)
        self.lbldes.grid(row=2, column=3)
        
        #===========BUTTONS============= 
        self.button2 = Button(self.LoginFrame2, text="SAVE", width=10, font="Helvetica 14 bold", bg="light blue", command=self.INSERT_AP)
        self.button2.grid(row=3, column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="light blue", command=self.DE_AP_DISPLAY)
        self.button3.grid(row=3, column=2)
        
        self.button3 = Button(self.LoginFrame2, text="SEARCH APPOINTMENTS", width=20, font="Helvetica 14 bold", bg="light blue", command=self.S_AP_DISPLAY)
        self.button3.grid(row=3, column=3)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="light blue", command=self.Exit)
        self.button6.grid(row=3, column=4)
        
    # FUNCTION TO EXIT APPOINTMENT WINDOW
    def Exit(self):            
        self.master.destroy()
        
    # FUNCTION TO INSERT DATA IN APPOINTMENT FORM   
    def INSERT_AP(self):
        global e1, e2, e3, e4, e5, e6, var
        e1 = (self.pat_ID.get())
        e2 = (self.emp_ID.get())
        e3 = (self.ap_no.get())
        e4 = (self.ap_time.get())
        e5 = (self.ap_date.get())
        e6 = (self.des.get())
        conn = sqlite3.connect("HospitalDB.db")
        p = list(conn.execute("SELECT * FROM appointment WHERE AP_NO =?", (e3,)))
        x = len(p)
        if x != 0:
            tkinter.messagebox.showerror("HOSPITAL DATABSE SYSTEM", "APPOINTMENT ALREADY EXISTS")     
        else:
            conn.execute("Insert into appointment values(?,?,?,?,?,?)", (e1, e2, e3, e4, e5, e6,))
            tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "APPOINTMENT SET SUCCESSFULLY")
        conn.commit()

    # FUNCTION TO OPEN DELETE APPOINTMENT DISPLAY WINDOW
    def DE_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DEL_AP(self.newWindow)
        
    # FUNCTION TO OPEN SEARCH APPOINTMENT DISPLAY WINDOW
    def S_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = SEA_AP(self.newWindow)
           

# CLASS FOR DISPLAY MENU FOR DELETE APPOINTMENT   
class DEL_AP:
    def __init__(self, master):    
        global de1_ap, de
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="lightblue")
        self.frame = Frame(self.master, bg="lightblue")
        self.frame.pack()
        self.de1_ap = StringVar()
        self.lblTitle = Label(self.frame, text="DELETE APPOINTMENT WINDOW", font="Helvetica 20 bold", bg="lightblue", fg="black")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame, text="ENTER APPOINTMENT NO TO DELETE", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.de1_ap)
        self.lblpatid.grid(row=0, column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="light blue", command=self.DELETE_AP)
        self.DeleteB.grid(row=3, column=1)

    # FUNCTION TO DELETE DATA IN APPOINTMENT FORM      
    def DELETE_AP(self):        
        global inp_d
        inp_d = str(self.de1_ap.get())
        conn = sqlite3.connect("HospitalDB.db")
        v = list(conn.execute("select * from appointment where AP_NO=?", (inp_d,)))
        if len(v) == 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "PATIENT APPOINTMENT NOT FIXED")     
        else:
            conn.execute('DELETE FROM APPOINTMENT where AP_NO=?', (inp_d,))
            tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "PATIENT APPOINTMENT DELETED")
        conn.commit()
        
# CLASS FOR DISPLAY MENU FOR SEARCH APPOINTMENT          
class SEA_AP:
    def __init__(self, master):    
        global inp_s, entry, SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="lightblue")
        self.frame = Frame(self.master, bg="lightblue")
        self.frame.pack()
        self.entry = StringVar()
        self.lblTitle = Label(self.frame, text="SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold", bg="lightblue", fg="black")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=25)
        
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame, text="ENTER APPOINTMENT NO TO SEARCH", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.entry)
        self.lblpatid.grid(row=0, column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH", width=10, font="Helvetica 14 bold", bg="light blue", command=self.SEARCH_AP)
        self.SearchB.grid(row=3, column=1)

    # FUNCTION TO SEARCH DATA IN APPOINTMENT FORM      
    def SEARCH_AP(self):        
        global inp_s
        inp_s = str(self.entry.get())
        conn = sqlite3.connect("HospitalDB.db")
        v = list(conn.execute("select * from appointment where AP_NO=?", (inp_s,)))
        if len(v) == 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "NO APPOINTMENT FOUND")     
        else:
            for row in v:
                tkinter.messagebox.showinfo("Appointment Found", f"Appointment details: {row}")
                
# MAIN FUNCTION TO RUN GUI
def main():
    root = Tk()
    app = Appointment(root)
    root.mainloop()
