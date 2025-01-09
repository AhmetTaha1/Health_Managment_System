from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
import time

class AppointmentForm:
    def __init__(self, master, patient_id):
        self.master = master
        self.patient_id = patient_id
        self.master.title("Book Appointment")
        self.master.geometry("800x600")
        self.master.config(bg="lightblue")

        self.conn = sqlite3.connect("HospitalDB.db")
        print("DATABASE CONNECTION SUCCESSFUL")

        # Variables
        self.emp_id = StringVar()
        self.ap_date = StringVar()
        self.ap_time = StringVar()
        self.description = StringVar()
        self.ap_no = StringVar()

        # Title
        Label(
            self.master,
            text="BOOK APPOINTMENT",
            font="Arial 20 bold",
            bg="lightblue",
            fg="darkblue",
        ).pack(pady=20)

        # Form Frame
        form_frame = Frame(self.master, bg="lightblue")
        form_frame.pack(pady=10)

        # Patient ID
        Label(
            form_frame, text="Patient ID:", font="Arial 14", bg="lightblue"
        ).grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Entry(
            form_frame, font="Arial 14", textvariable=StringVar(value=self.patient_id), state="readonly"
        ).grid(row=0, column=1, padx=10, pady=5)

        # Appointment Number (Auto-generated)
        Label(
            form_frame, text="Appointment Number:", font="Arial 14", bg="lightblue"
        ).grid(row=1, column=0, padx=10, pady=5, sticky=W)
        Entry(
            form_frame, font="Arial 14", textvariable=self.ap_no, state="readonly"
        ).grid(row=1, column=1, padx=10, pady=5)

        # Doctor Selection
        Label(
            form_frame, text="Select Doctor:", font="Arial 14", bg="lightblue"
        ).grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.doctor_combo = ttk.Combobox(form_frame, font="Arial 14", textvariable=self.emp_id)
        self.load_doctors()
        self.doctor_combo.grid(row=2, column=1, padx=10, pady=5)

        # Appointment Date
        Label(
            form_frame, text="Date (YYYY-MM-DD):", font="Arial 14", bg="lightblue"
        ).grid(row=3, column=0, padx=10, pady=5, sticky=W)
        Entry(form_frame, font="Arial 14", textvariable=self.ap_date).grid(
            row=3, column=1, padx=10, pady=5
        )

        # Appointment Time
        Label(
            form_frame, text="Time (HH:MM:SS):", font="Arial 14", bg="lightblue"
        ).grid(row=4, column=0, padx=10, pady=5, sticky=W)
        Entry(form_frame, font="Arial 14", textvariable=self.ap_time).grid(
            row=4, column=1, padx=10, pady=5
        )

        # Description
        Label(
            form_frame, text="Description:", font="Arial 14", bg="lightblue"
        ).grid(row=5, column=0, padx=10, pady=5, sticky=W)
        Entry(form_frame, font="Arial 14", textvariable=self.description).grid(
            row=5, column=1, padx=10, pady=5
        )

        # Buttons
        button_frame = Frame(self.master, bg="lightblue")
        button_frame.pack(pady=20)
        Button(
            button_frame,
            text="BOOK APPOINTMENT",
            font="Arial 14 bold",
            bg="deepskyblue",
            fg="white",
            command=self.book_appointment,
        ).grid(row=0, column=0, padx=10, pady=10)
        Button(
            button_frame,
            text="CANCEL",
            font="Arial 14 bold",
            bg="red",
            fg="white",
            command=self.master.destroy,
        ).grid(row=0, column=1, padx=10, pady=10)

        self.generate_appointment_number()

    def load_doctors(self):
        """Load doctors from the database into the combobox."""
        try:
            doctors = self.conn.execute("SELECT EMP_ID, EMP_NAME FROM EMPLOYEE WHERE DESIG = 'Doctor'").fetchall()
            self.doctor_combo["values"] = [f"{doc[0]} - {doc[1]}" for doc in doctors]
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

    def generate_appointment_number(self):
        """Generate the next unique appointment number."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT COALESCE(MAX(AP_NO), 0) + 1 FROM APPOINTMENT")
            self.ap_no.set(cursor.fetchone()[0])
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error generating appointment number: {e}")
            self.master.destroy()


   

    def book_appointment(self):
        """Book an appointment for the patient."""
        emp_id = self.emp_id.get().split(" - ")[0]  # Extract doctor ID
        ap_date = self.ap_date.get()
        ap_time = self.ap_time.get()
        description = self.description.get()

        if not (emp_id and ap_date and ap_time and description):
            messagebox.showerror("Input Error", "All fields are required!")
            return

        try:
            # Generate unique appointment number
            timestamp = time.strftime("%Y%m%d%H%M%S")  # Current time as a unique ID component
            ap_no = f"{self.patient_id}_{timestamp}"

            # Insert appointment into the database
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO APPOINTMENT (PATIENT_ID, EMP_ID, AP_NO, AP_TIME, AP_DATE, DESCRIPTION) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (self.patient_id, emp_id, ap_no, ap_time, ap_date, description),
            )
            self.conn.commit()
            messagebox.showinfo("Success", f"Appointment booked successfully!\nAppointment No: {ap_no}")
            self.master.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Database Error", "Appointment number conflict. Please try again.")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))




# Example usage
if __name__ == "__main__":
    root = Tk()
    AppointmentForm(root, patient_id="P001")  # Replace with actual patient ID
    root.mainloop()
