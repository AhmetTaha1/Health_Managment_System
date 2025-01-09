from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class MedicalRecords:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="light blue")
        self.frame = Frame(self.master, bg="light blue")
        self.frame.pack()

        # Variables
        self.patient_id = StringVar()
        self.record_date = StringVar()
        self.diagnosis = StringVar()
        self.treatment = StringVar()
        self.prescription = StringVar()

        # Title
        self.lblTitle = Label(self.frame, text="MEDICAL RECORD FORM", font="Helvetica 20 bold", bg="light blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        # Frames for inputs and buttons
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="light blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="light blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # Labels and Entry Fields
        self.lblPatientID = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblPatientID.grid(row=0, column=0)
        self.entryPatientID = Entry(self.LoginFrame, textvariable=self.patient_id, font="Helvetica 14 bold", bd=2)
        self.entryPatientID.grid(row=0, column=1)

        self.lblRecordDate = Label(self.LoginFrame, text="RECORD DATE (YYYY-MM-DD)", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblRecordDate.grid(row=1, column=0)
        self.entryRecordDate = Entry(self.LoginFrame, textvariable=self.record_date, font="Helvetica 14 bold", bd=2)
        self.entryRecordDate.grid(row=1, column=1)

        self.lblDiagnosis = Label(self.LoginFrame, text="DIAGNOSIS", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblDiagnosis.grid(row=2, column=0)
        self.entryDiagnosis = Entry(self.LoginFrame, textvariable=self.diagnosis, font="Helvetica 14 bold", bd=2)
        self.entryDiagnosis.grid(row=2, column=1)

        self.lblTreatment = Label(self.LoginFrame, text="TREATMENT", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblTreatment.grid(row=3, column=0)
        self.entryTreatment = Entry(self.LoginFrame, textvariable=self.treatment, font="Helvetica 14 bold", bd=2)
        self.entryTreatment.grid(row=3, column=1)

        self.lblPrescription = Label(self.LoginFrame, text="PRESCRIPTION", font="Helvetica 14 bold", bg="light blue", bd=22)
        self.lblPrescription.grid(row=4, column=0)
        self.entryPrescription = Entry(self.LoginFrame, textvariable=self.prescription, font="Helvetica 14 bold", bd=2)
        self.entryPrescription.grid(row=4, column=1)

        # Buttons
        self.btnAdd = Button(self.LoginFrame2, text="ADD RECORD", width=15, font="Helvetica 14 bold", bg="light blue", command=self.add_record)
        self.btnAdd.grid(row=0, column=0, padx=10)

        self.btnClose = Button(self.LoginFrame2, text="CLOSE", width=15, font="Helvetica 14 bold", bg="light blue", command=self.master.destroy)
        self.btnClose.grid(row=0, column=1, padx=10)

    def add_record(self):
        try:
            conn = sqlite3.connect("HospitalDB.db")
            c = conn.cursor()
            c.execute(
                "INSERT INTO MEDICAL_RECORDS (PATIENT_ID, RECORD_DATE, DIAGNOSIS, TREATMENT, PRESCRIPTION) VALUES (?, ?, ?, ?, ?)",
                (
                    self.patient_id.get(),
                    self.record_date.get(),
                    self.diagnosis.get(),
                    self.treatment.get(),
                    self.prescription.get(),
                ),
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("HOSPITAL MANAGEMENT SYSTEM", "Record added successfully")
        except Exception as e:
            messagebox.showerror("HOSPITAL MANAGEMENT SYSTEM", f"Failed to add record: {e}")


# Main application
if __name__ == "__main__":
    root = Tk()
    app = MedicalRecords(root)
    root.mainloop()
