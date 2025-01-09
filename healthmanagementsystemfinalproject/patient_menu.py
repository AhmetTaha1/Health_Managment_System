from tkinter import *
from patient_appointment import AppointmentForm
from patient_view_appointments import PatientViewAppointments
from view_medical_records import ViewMedicalRecords
from view_billing_info import ViewBillingInfo


class PatientMenu:
    def __init__(self, master, patient_id):
        self.master = master
        self.patient_id = patient_id  # Patient's ID
        self.master.title("Patient Menu")
        self.master.geometry("800x600")
        self.master.config(bg="lightblue")

        # Title
        Label(
            self.master,
            text="PATIENT MENU",
            font="Arial 28 bold",
            bg="lightblue",
            fg="darkblue",
        ).pack(pady=20)

        # Menu Buttons
        self.create_menu_button("TAKE APPOINTMENT", self.take_appointment)
        self.create_menu_button("VIEW APPOINTMENTS", self.view_appointments)
        self.create_menu_button("VIEW MEDICAL RECORDS", self.view_medical_records)
        self.create_menu_button("VIEW BILLING INFO", self.view_billing_info)
        self.create_menu_button("EXIT", self.master.destroy, bg_color="red", fg_color="white")

    def create_menu_button(self, text, command, bg_color="deepskyblue", fg_color="black"):
        Button(
            self.master,
            text=text,
            font="Arial 16 bold",
            width=25,
            bg=bg_color,
            fg=fg_color,
            command=command,
        ).pack(pady=10)

    def take_appointment(self):
        """Open the window to take an appointment."""
        self.newWindow = Toplevel(self.master)
        self.app = AppointmentForm(self.newWindow, self.patient_id)  # Use AppointmentForm for taking appointments

    def view_appointments(self):
        """Open the window to view existing appointments."""
        self.newWindow = Toplevel(self.master)
        self.app = PatientViewAppointments(self.newWindow, self.patient_id)  # Use PatientViewAppointments for viewing appointments

    def view_medical_records(self):
        """Open the window to view medical records."""
        self.newWindow = Toplevel(self.master)
        self.app = ViewMedicalRecords(self.newWindow, self.patient_id)

    def view_billing_info(self):
        """Open the window to view billing information."""
        self.newWindow = Toplevel(self.master)
        self.app = ViewBillingInfo(self.newWindow, self.patient_id)


# Example usage
if __name__ == "__main__":
    root = Tk()
    PatientMenu(root, patient_id="P001")  # Replace with an actual patient ID
    root.mainloop()
