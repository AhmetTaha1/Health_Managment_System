from tkinter import *
import sqlite3
from patient_form import Patient
from room_form import Room
from employee_form import Employee
from appointment_form import Appointment
from billing_form import Billing
from doctor_schedule import DoctorSchedule
from medical_records import MedicalRecords
from generate_reports import GenerateReports  # Import Generate Reports functionality

# Establish database connection
conn = sqlite3.connect("HospitalDB.db")
print("DATABASE CONNECTION SUCCESSFUL")

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("HEALTH ADMINISTRATION MANAGEMENT SYSTEM")
        self.master.geometry("1000x700+0+0")
        self.master.config(bg="lightblue")  # Light blue background for the main window

        # Title Label
        self.lblTitle = Label(
            self.master,
            text="MAIN MENU",
            font="Arial 28 bold",
            bg="lightblue",
            fg="darkblue"
        )
        self.lblTitle.pack(pady=20)  # Add padding above and below the title

        # Button frame to hold menu buttons
        self.button_frame = Frame(self.master, bg="lightblue")
        self.button_frame.pack(pady=20)  # Padding around the button frame

        # Buttons for different functionalities
        self.create_button("1. PATIENT REGISTRATION", self.Patient_Reg)
        self.create_button("2. ROOM ALLOCATION", self.Room_Allocation)
        self.create_button("3. EMPLOYEE REGISTRATION", self.Employee_Reg)
        self.create_button("4. BOOK APPOINTMENT", self.Appointment_Form)
        self.create_button("5. PATIENT BILL", self.Billing_Form)
        self.create_button("6. DOCTOR SCHEDULE", self.Doctor_Schedule)
        self.create_button("7. MEDICAL RECORDS", self.Medical_Records)
        self.create_button("8. GENERATE REPORTS", self.Generate_Reports)  # New Generate Reports button
        self.create_button("9. EXIT", self.Exit, bg_color="red", fg_color="white")  # Highlight Exit in red

    def create_button(self, text, command, bg_color="deepskyblue", fg_color="black"):
        """Helper method to create buttons with consistent styling."""
        button = Button(
            self.button_frame,
            text=text,
            font="Arial 16 bold",
            width=30,
            bg=bg_color,
            fg=fg_color,
            command=command
        )
        button.pack(pady=10)  # Space between buttons

    def Patient_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow)

    def Room_Allocation(self):
        self.newWindow = Toplevel(self.master)
        self.app = Room(self.newWindow)

    def Employee_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Employee(self.newWindow)

    def Appointment_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Appointment(self.newWindow)

    def Billing_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Billing(self.newWindow)

    def Doctor_Schedule(self):
        self.newWindow = Toplevel(self.master)
        self.app = DoctorSchedule(self.newWindow)

    def Medical_Records(self):
        self.newWindow = Toplevel(self.master)
        self.app = MedicalRecords(self.newWindow)

    def Generate_Reports(self):
        self.newWindow = Toplevel(self.master)
        self.app = GenerateReports(self.newWindow)

    def Exit(self):
        self.master.destroy()


# Main application
if __name__ == "__main__":
    root = Tk()
    app = Menu(root)
    root.mainloop()
