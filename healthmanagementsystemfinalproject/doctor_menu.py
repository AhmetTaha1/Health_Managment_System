from tkinter import *
import tkinter.messagebox
from view_schedule import ViewSchedule
from view_patient_records import ViewPatientRecords  # Ensure this is correctly imported

class DoctorMenu:
    def __init__(self, master, emp_id):
        self.master = master
        self.master.title("DOCTOR MENU")
        self.master.geometry("800x600")
        self.master.config(bg="lightblue")

        self.emp_id = emp_id  # Store doctor/employee ID for personalized actions

        # Title
        self.lblTitle = Label(
            self.master,
            text="DOCTOR MENU",
            font="Arial 28 bold",
            bg="lightblue",
            fg="darkblue"
        )
        self.lblTitle.pack(pady=20)

        # Button Frame
        self.button_frame = Frame(self.master, bg="lightblue")
        self.button_frame.pack(pady=20)

        # Buttons for doctor functionalities
        self.create_button("1. VIEW SCHEDULE", self.open_view_schedule)
        self.create_button("2. VIEW PATIENT RECORDS", self.open_view_patient_records)
        self.create_button("3. EXIT", self.exit, bg_color="red", fg_color="white")

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
        button.pack(pady=10)

    def open_view_schedule(self):
        """Open the ViewSchedule window, passing the doctor's EMP_ID."""
        self.newWindow = Toplevel(self.master)
        ViewSchedule(self.newWindow, emp_id=self.emp_id)

    def open_view_patient_records(self):
        """Open the ViewPatientRecords window, passing the doctor's EMP_ID."""
        self.newWindow = Toplevel(self.master)
        ViewPatientRecords(self.newWindow, emp_id=self.emp_id)  # Pass EMP_ID to filter patient records

    def exit(self):
        """Close the Doctor Menu window."""
        self.master.destroy()


# Main application
if __name__ == "__main__":
    root = Tk()
    app = DoctorMenu(root, emp_id="EMP001")  # Replace "EMP001" with the actual doctor's EMP_ID
    root.mainloop()
