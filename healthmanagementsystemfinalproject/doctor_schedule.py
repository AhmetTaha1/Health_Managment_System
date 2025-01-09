from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class DoctorSchedule:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="light blue")

        # Use a frame with colored background
        self.frame = Frame(self.master, bg="light blue")
        self.frame.pack()

        # Set up the database connection
        self.conn = sqlite3.connect("HospitalDB.db")
        self.cursor = self.conn.cursor()

        # Set up the UI components
        self.setup_ui()

    def setup_ui(self):
        # Title label
        self.lblTitle = Label(self.frame, text="DOCTOR SCHEDULE FORM", font="Helvetica 20 bold", bg="light blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        # Frames for the form inputs
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # Labels and entry fields for doctor's schedule
        self.lblDoctorID = Label(self.LoginFrame, text="DOCTOR ID (EMP_ID)", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblDoctorID.grid(row=0, column=0)
        self.entDoctorID = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2)
        self.entDoctorID.grid(row=0, column=1)

        self.lblDay = Label(self.LoginFrame, text="DAY OF WEEK", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblDay.grid(row=1, column=0)
        self.entDay = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2)
        self.entDay.grid(row=1, column=1)

        self.lblStartTime = Label(self.LoginFrame, text="START TIME", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblStartTime.grid(row=2, column=0)
        self.entStartTime = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2)
        self.entStartTime.grid(row=2, column=1)

        self.lblEndTime = Label(self.LoginFrame, text="END TIME", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblEndTime.grid(row=3, column=0)
        self.entEndTime = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2)
        self.entEndTime.grid(row=3, column=1)

        # Buttons for actions
        self.btnAddSchedule = Button(self.LoginFrame2, text="ADD SCHEDULE", width=15, font="Helvetica 14 bold", bg="light blue", command=self.add_schedule)
        self.btnAddSchedule.grid(row=0, column=0, padx=10)

        self.btnUpdateSchedule = Button(self.LoginFrame2, text="UPDATE SCHEDULE", width=15, font="Helvetica 14 bold", bg="light blue", command=self.update_schedule)
        self.btnUpdateSchedule.grid(row=0, column=1, padx=10)

        self.btnViewSchedule = Button(self.LoginFrame2, text="VIEW SCHEDULE", width=15, font="Helvetica 14 bold", bg="light blue", command=self.view_schedule)
        self.btnViewSchedule.grid(row=0, column=2, padx=10)

        self.btnExit = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="light blue", command=self.exit_form)
        self.btnExit.grid(row=0, column=3, padx=10)

    def add_schedule(self):
        emp_id = self.entDoctorID.get()
        day_of_week = self.entDay.get()
        start_time = self.entStartTime.get()
        end_time = self.entEndTime.get()

        if not emp_id or not day_of_week or not start_time or not end_time:
            messagebox.showerror("HOSPITAL MANAGEMENT SYSTEM", "All fields are required!")
            return

        try:
            self.cursor.execute("INSERT INTO DOCTOR_SCHEDULE (EMP_ID, DAY_OF_WEEK, START_TIME, END_TIME) VALUES (?, ?, ?, ?)",
                                (emp_id, day_of_week, start_time, end_time))
            self.conn.commit()
            messagebox.showinfo("HOSPITAL MANAGEMENT SYSTEM", "Schedule added successfully!")
        except Exception as e:
            messagebox.showerror("HOSPITAL MANAGEMENT SYSTEM", str(e))

    def update_schedule(self):
        emp_id = self.entDoctorID.get()
        day_of_week = self.entDay.get()
        start_time = self.entStartTime.get()
        end_time = self.entEndTime.get()

        if not emp_id or not day_of_week or not start_time or not end_time:
            messagebox.showerror("HOSPITAL MANAGEMENT SYSTEM", "All fields are required!")
            return

        try:
            self.cursor.execute("UPDATE DOCTOR_SCHEDULE SET START_TIME = ?, END_TIME = ? WHERE EMP_ID = ? AND DAY_OF_WEEK = ?",
                                (start_time, end_time, emp_id, day_of_week))
            self.conn.commit()
            messagebox.showinfo("HOSPITAL MANAGEMENT SYSTEM", "Schedule updated successfully!")
        except Exception as e:
            messagebox.showerror("HOSPITAL MANAGEMENT SYSTEM", str(e))

    def view_schedule(self):
        emp_id = self.entDoctorID.get()

        if not emp_id:
            messagebox.showerror("HOSPITAL MANAGEMENT SYSTEM", "Doctor ID is required!")
            return

        self.cursor.execute("SELECT DAY_OF_WEEK, START_TIME, END_TIME FROM DOCTOR_SCHEDULE WHERE EMP_ID = ?", (emp_id,))
        rows = self.cursor.fetchall()

        if rows:
            view_window = Toplevel(self.master)
            view_window.title("Doctor Schedule")
            view_window.geometry("600x400")
            tree = ttk.Treeview(view_window, columns=("Day", "Start Time", "End Time"), show="headings")
            tree.heading("Day", text="Day")
            tree.heading("Start Time", text="Start Time")
            tree.heading("End Time", text="End Time")
            tree.grid(row=0, column=0, padx=10, pady=10)

            for row in rows:
                tree.insert("", "end", values=row)
        else:
            messagebox.showinfo("HOSPITAL MANAGEMENT SYSTEM", "No schedule found for this doctor.")

    def exit_form(self):
        self.master.destroy()

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = Tk()
    app = DoctorSchedule(root)
    root.mainloop()
