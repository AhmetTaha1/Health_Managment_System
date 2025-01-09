from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class ViewSchedule:
    def __init__(self, master, emp_id):
        self.master = master
        self.master.title("Doctor's Schedule")
        self.master.geometry("800x400")
        self.master.config(bg="lightblue")

        self.emp_id = emp_id  # Store the EMP_ID of the doctor

        # UI Components
        self.setup_ui()

        # Load the doctor's schedule
        self.load_schedule()

    def setup_ui(self):
        """Setup the UI for viewing the schedule."""
        # Title
        self.lblTitle = Label(
            self.master,
            text="DOCTOR'S SCHEDULE",
            font="Helvetica 20 bold",
            bg="lightblue",
            fg="darkblue"
        )
        self.lblTitle.pack(pady=10)

        # Table Frame
        self.table_frame = Frame(self.master, bg="lightblue")
        self.table_frame.pack(pady=20)

        # Treeview for displaying schedule
        self.schedule_table = ttk.Treeview(
            self.table_frame,
            columns=("Day", "Start Time", "End Time"),
            show="headings",
            height=10
        )
        self.schedule_table.heading("Day", text="Day")
        self.schedule_table.heading("Start Time", text="Start Time")
        self.schedule_table.heading("End Time", text="End Time")
        self.schedule_table.column("Day", width=200, anchor="center")
        self.schedule_table.column("Start Time", width=200, anchor="center")
        self.schedule_table.column("End Time", width=200, anchor="center")
        self.schedule_table.pack(side=LEFT, fill=BOTH, expand=True)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.table_frame, orient=VERTICAL, command=self.schedule_table.yview)
        self.schedule_table.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Close Button
        self.btnClose = Button(
            self.master,
            text="CLOSE",
            font="Helvetica 14 bold",
            bg="red",
            fg="white",
            command=self.master.destroy
        )
        self.btnClose.pack(pady=10)

    def load_schedule(self):
        """Fetch and display the schedule of the doctor."""
        try:
            conn = sqlite3.connect("HospitalDB.db")
            cursor = conn.cursor()

            # Query to fetch the doctor's schedule
            cursor.execute("""
                SELECT DAY_OF_WEEK, START_TIME, END_TIME
                FROM DOCTOR_SCHEDULE
                WHERE EMP_ID = ?
            """, (self.emp_id,))
            rows = cursor.fetchall()

            # Check if there are any records
            if rows:
                for row in rows:
                    self.schedule_table.insert("", "end", values=row)
            else:
                messagebox.showinfo("No Schedule", "No schedule found for the doctor.")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
