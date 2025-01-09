from tkinter import *
from tkinter.ttk import Treeview
import sqlite3

class ViewAppointments:
    def __init__(self, master, patient_id):
        self.master = master
        self.master.title("View Appointments")
        self.master.geometry("600x400")
        self.master.config(bg="lightblue")

        # Title
        Label(
            self.master,
            text="Your Appointments",
            font="Arial 20 bold",
            bg="lightblue",
            fg="darkblue",
        ).pack(pady=10)

        # Table Setup
        columns = ("Appointment Date", "Time", "Doctor")
        self.tree = Treeview(self.master, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor=CENTER)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.populate_table(patient_id)

    def populate_table(self, patient_id):
        try:
            conn = sqlite3.connect("HospitalDB.db")
            cursor = conn.cursor()
            query = """
            SELECT AP_DATE, AP_TIME, EMP_NAME
            FROM APPOINTMENT
            JOIN EMPLOYEE ON APPOINTMENT.EMP_ID = EMPLOYEE.EMP_ID
            WHERE PATIENT_ID = ?
            """
            rows = cursor.execute(query, (patient_id,)).fetchall()

            for row in rows:
                self.tree.insert("", "end", values=row)

            if not rows:
                Label(
                    self.master, text="No appointments found.", fg="red", bg="lightblue"
                ).pack(pady=10)

        except sqlite3.Error as e:
            Label(
                self.master, text=f"Database Error: {e}", fg="red", bg="lightblue"
            ).pack(pady=10)

        finally:
            if conn:
                conn.close()
