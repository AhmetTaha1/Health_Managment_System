from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class ViewPatientRecords:
    def __init__(self, master, emp_id):
        self.master = master
        self.master.title("VIEW PATIENT RECORDS")
        self.master.geometry("800x600")
        self.master.config(bg="lightblue")

        self.emp_id = emp_id  # Store the EMP_ID of the doctor

        # UI Components
        self.setup_ui()

        # Load Patient Records
        self.load_patient_records()

    def setup_ui(self):
        """Setup the UI for viewing patient records."""
        # Title
        self.lblTitle = Label(
            self.master,
            text="PATIENT RECORDS",
            font="Helvetica 20 bold",
            bg="lightblue",
            fg="darkblue"
        )
        self.lblTitle.pack(pady=20)

        # Table Frame
        self.table_frame = Frame(self.master, bg="lightblue")
        self.table_frame.pack(pady=20)

        # Treeview for displaying patient records
        self.patient_table = ttk.Treeview(
            self.table_frame,
            columns=("ID", "Name", "Blood Group", "DOB", "Consult Team"),
            show="headings",
            height=15
        )
        self.patient_table.heading("ID", text="ID")
        self.patient_table.heading("Name", text="Name")
        self.patient_table.heading("Blood Group", text="Blood Group")
        self.patient_table.heading("DOB", text="DOB")
        self.patient_table.heading("Consult Team", text="Consult Team")
        self.patient_table.column("ID", width=100, anchor="center")
        self.patient_table.column("Name", width=200, anchor="center")
        self.patient_table.column("Blood Group", width=150, anchor="center")
        self.patient_table.column("DOB", width=150, anchor="center")
        self.patient_table.column("Consult Team", width=200, anchor="center")
        self.patient_table.pack(side=LEFT, fill=BOTH, expand=True)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.table_frame, orient=VERTICAL, command=self.patient_table.yview)
        self.patient_table.configure(yscroll=self.scrollbar.set)
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

    def load_patient_records(self):
        """Fetch and display patient records assigned to the doctor based on appointments."""
        try:
            # Connect to the database
            conn = sqlite3.connect("HospitalDB.db")
            cursor = conn.cursor()

            # Fetch patient records where the doctor (EMP_ID) has appointments with the patients
            query = """
                SELECT 
                    p.PATIENT_ID, p.NAME, p.BLOOD_GROUP, p.DOB, p.CONSULT_TEAM
                FROM 
                    PATIENT p
                INNER JOIN 
                    APPOINTMENT a ON p.PATIENT_ID = a.PATIENT_ID
                WHERE 
                    a.EMP_ID = ?
            """
            cursor.execute(query, (self.emp_id,))
            rows = cursor.fetchall()

            # Insert data into the table
            if rows:
                for row in rows:
                    self.patient_table.insert("", "end", values=row)
            else:
                messagebox.showinfo("No Records", "No patient records found for your appointments.")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            conn.close()


# Testing standalone (example usage)
if __name__ == "__main__":
    root = Tk()
    ViewPatientRecords(root, emp_id="EMP001")  # Replace "EMP001" with the actual doctor EMP_ID for testing
    root.mainloop()
