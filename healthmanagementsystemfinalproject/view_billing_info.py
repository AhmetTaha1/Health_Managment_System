from tkinter import *
from tkinter.ttk import Treeview
import sqlite3

class ViewBillingInfo:
    def __init__(self, master, patient_id):
        self.master = master
        self.master.title("View Billing Information")
        self.master.geometry("600x400")
        self.master.config(bg="lightblue")

        # Title
        Label(
            self.master,
            text="Billing Information",
            font="Arial 20 bold",
            bg="lightblue",
            fg="darkblue",
        ).pack(pady=10)

        # Table Setup
        columns = ("Bill Date", "Amount", "Paid Status")
        self.tree = Treeview(self.master, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor=CENTER)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.populate_table(patient_id)

    def populate_table(self, patient_id):
        query = """
        SELECT 
            ROOM.DATE_ADMITTED AS BILL_DATE,
            (TREATMENT.T_COST + MEDICINE.M_COST + ROOM.RATE) AS Amount,
            CASE WHEN NOTIFICATIONS.MESSAGE LIKE '%paid%' THEN 'Paid' ELSE 'Unpaid' END AS Paid_Status
        FROM 
            PATIENT
        LEFT JOIN 
            TREATMENT ON PATIENT.PATIENT_ID = TREATMENT.PATIENT_ID
        LEFT JOIN 
            MEDICINE ON PATIENT.PATIENT_ID = MEDICINE.PATIENT_ID
        LEFT JOIN 
            ROOM ON PATIENT.PATIENT_ID = ROOM.PATIENT_ID
        LEFT JOIN 
            NOTIFICATIONS ON PATIENT.PATIENT_ID = NOTIFICATIONS.PATIENT_ID
        WHERE 
            PATIENT.PATIENT_ID = ?
        """
        try:
            conn = sqlite3.connect("HospitalDB.db")
            cursor = conn.cursor()
            rows = cursor.execute(query, (patient_id,)).fetchall()

            for row in rows:
                self.tree.insert("", "end", values=row)

            if not rows:
                Label(
                    self.master, text="No billing information found.", fg="red", bg="lightblue"
                ).pack(pady=10)

        except sqlite3.Error as e:
            Label(
                self.master, text=f"Database Error: {e}", fg="red", bg="lightblue"
            ).pack(pady=10)

        finally:
            if conn:
                conn.close()
