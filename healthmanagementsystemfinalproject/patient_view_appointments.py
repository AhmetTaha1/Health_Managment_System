from tkinter import *
from tkinter import ttk
import sqlite3


class PatientViewAppointments:
    def __init__(self, master, patient_id):
        self.master = master
        self.patient_id = patient_id  # Patient's ID
        self.master.title("View Your Appointments")
        self.master.geometry("700x400")
        self.master.config(bg="lightblue")

        # Title
        Label(
            self.master,
            text="Your Appointments",
            font="Arial 20 bold",
            bg="lightblue",
            fg="darkblue",
        ).pack(pady=20)

        # Treeview to display appointments
        self.tree = ttk.Treeview(self.master, columns=("Appointment No", "Doctor ID", "Date", "Time", "Description"), show="headings")
        self.tree.pack(pady=20, fill=BOTH, expand=True)

        # Define column headings
        self.tree.heading("Appointment No", text="Appointment No")
        self.tree.heading("Doctor ID", text="Doctor ID")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Time", text="Time")
        self.tree.heading("Description", text="Description")

        self.tree.column("Appointment No", anchor=CENTER, width=100)
        self.tree.column("Doctor ID", anchor=CENTER, width=100)
        self.tree.column("Date", anchor=CENTER, width=150)
        self.tree.column("Time", anchor=CENTER, width=100)
        self.tree.column("Description", anchor=W, width=200)

        # Load appointments
        self.load_appointments()

    def load_appointments(self):
        try:
            conn = sqlite3.connect("HospitalDB.db")
            cursor = conn.cursor()

            # Query to fetch patient-specific appointments
            query = """
                SELECT AP_NO, EMP_ID, AP_DATE, AP_TIME, DESCRIPTION
                FROM APPOINTMENT
                WHERE PATIENT_ID = ?
                ORDER BY AP_DATE, AP_TIME
            """
            cursor.execute(query, (self.patient_id,))
            appointments = cursor.fetchall()

            # Populate treeview with appointments
            for appointment in appointments:
                self.tree.insert("", "end", values=appointment)

            conn.close()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            Label(self.master, text="Failed to load appointments", bg="lightblue", fg="red", font="Arial 12").pack(pady=10)


# Example usage
if __name__ == "__main__":
    root = Tk()
    PatientViewAppointments(root, patient_id="P001")  # Replace with an actual patient ID
    root.mainloop()
