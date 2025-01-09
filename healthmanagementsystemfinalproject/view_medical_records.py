from tkinter import *
from tkinter.ttk import Treeview
import sqlite3

class ViewMedicalRecords:
    def __init__(self, master, patient_id):
        self.master = master
        self.master.title("View Medical Records")
        self.master.geometry("600x400")
        self.master.config(bg="lightblue")

        # Title
        Label(
            self.master,
            text="Your Medical Records",
            font="Arial 20 bold",
            bg="lightblue",
            fg="darkblue",
        ).pack(pady=10)

        # Table Setup
        columns = ("Record Date", "Diagnosis", "Treatment", "Prescription")
        self.tree = Treeview(self.master, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor=CENTER)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.populate_table(patient_id)

    def populate_table(self, patient_id):
        try:
            conn = sqlite3.connect("HospitalDB.db")
            cursor = conn.cursor()
            query = """
            SELECT RECORD_DATE, DIAGNOSIS, TREATMENT, PRESCRIPTION
            FROM MEDICAL_RECORDS
            WHERE PATIENT_ID = ?
            """
            rows = cursor.execute(query, (patient_id,)).fetchall()

            for row in rows:
                self.tree.insert("", "end", values=row)

            if not rows:
                Label(
                    self.master, text="No medical records found.", fg="red", bg="lightblue"
                ).pack(pady=10)

        except sqlite3.Error as e:
            Label(
                self.master, text=f"Database Error: {e}", fg="red", bg="lightblue"
            ).pack(pady=10)

        finally:
            if conn:
                conn.close()
