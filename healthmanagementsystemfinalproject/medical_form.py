import sqlite3
from tkinter import *
from tkinter import messagebox

class MedicalRecords:
    def __init__(self, master):
        self.master = master
        self.master.title("Medical Records, Treatments, and Prescriptions")
        self.master.geometry("600x400")
        
        # Connect to the database
        self.conn = sqlite3.connect("HospitalDB.db")
        self.cursor = self.conn.cursor()
        
        # Set up the GUI
        self.create_widgets()
    
    def create_widgets(self):
        self.lblTitle = Label(self.master, text="Medical Records, Treatments, and Prescriptions", font="Helvetica 16 bold")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=20)

        # Patient ID input
        self.lblPatientID = Label(self.master, text="Patient ID:")
        self.lblPatientID.grid(row=1, column=0, padx=10, pady=10)
        self.entPatientID = Entry(self.master)
        self.entPatientID.grid(row=1, column=1, padx=10, pady=10)

        # Medical Records
        self.lblDiagnosis = Label(self.master, text="Diagnosis:")
        self.lblDiagnosis.grid(row=2, column=0, padx=10, pady=10)
        self.entDiagnosis = Entry(self.master)
        self.entDiagnosis.grid(row=2, column=1, padx=10, pady=10)

        self.lblMedicalHistory = Label(self.master, text="Medical History:")
        self.lblMedicalHistory.grid(row=3, column=0, padx=10, pady=10)
        self.entMedicalHistory = Entry(self.master)
        self.entMedicalHistory.grid(row=3, column=1, padx=10, pady=10)

        # Treatments
        self.lblTreatment = Label(self.master, text="Treatment Name:")
        self.lblTreatment.grid(row=4, column=0, padx=10, pady=10)
        self.entTreatment = Entry(self.master)
        self.entTreatment.grid(row=4, column=1, padx=10, pady=10)

        self.lblTreatmentCode = Label(self.master, text="Treatment Code:")
        self.lblTreatmentCode.grid(row=5, column=0, padx=10, pady=10)
        self.entTreatmentCode = Entry(self.master)
        self.entTreatmentCode.grid(row=5, column=1, padx=10, pady=10)

        self.lblTreatmentCost = Label(self.master, text="Treatment Cost:")
        self.lblTreatmentCost.grid(row=6, column=0, padx=10, pady=10)
        self.entTreatmentCost = Entry(self.master)
        self.entTreatmentCost.grid(row=6, column=1, padx=10, pady=10)

        # Prescriptions
        self.lblMedicineName = Label(self.master, text="Medicine Name:")
        self.lblMedicineName.grid(row=7, column=0, padx=10, pady=10)
        self.entMedicineName = Entry(self.master)
        self.entMedicineName.grid(row=7, column=1, padx=10, pady=10)

        self.lblMedicineQuantity = Label(self.master, text="Quantity:")
        self.lblMedicineQuantity.grid(row=8, column=0, padx=10, pady=10)
        self.entMedicineQuantity = Entry(self.master)
        self.entMedicineQuantity.grid(row=8, column=1, padx=10, pady=10)

        self.lblMedicineCost = Label(self.master, text="Medicine Cost:")
        self.lblMedicineCost.grid(row=9, column=0, padx=10, pady=10)
        self.entMedicineCost = Entry(self.master)
        self.entMedicineCost.grid(row=9, column=1, padx=10, pady=10)

        # Buttons
        self.btnAddRecord = Button(self.master, text="Add Medical Record", command=self.add_medical_record)
        self.btnAddRecord.grid(row=10, column=0, pady=20)

        self.btnAddTreatment = Button(self.master, text="Add Treatment", command=self.add_treatment)
        self.btnAddTreatment.grid(row=10, column=1, pady=20)

        self.btnAddPrescription = Button(self.master, text="Add Prescription", command=self.add_prescription)
        self.btnAddPrescription.grid(row=11, column=0, pady=20)

    def add_medical_record(self):
        patient_id = self.entPatientID.get()
        diagnosis = self.entDiagnosis.get()
        medical_history = self.entMedicalHistory.get()

        if not patient_id or not diagnosis:
            messagebox.showerror("Input Error", "Patient ID and Diagnosis are required!")
            return

        try:
            self.cursor.execute("INSERT INTO MEDICAL_RECORDS (PATIENT_ID, DIAGNOSIS, MEDICAL_HISTORY, DATE_OF_DIAGNOSIS) VALUES (?, ?, ?, ?)", 
                                (patient_id, diagnosis, medical_history, "2024-12-18"))
            self.conn.commit()
            messagebox.showinfo("Success", "Medical record added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_treatment(self):
        patient_id = self.entPatientID.get()
        treatment = self.entTreatment.get()
        treatment_code = self.entTreatmentCode.get()
        treatment_cost = self.entTreatmentCost.get()

        if not patient_id or not treatment or not treatment_code:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        try:
            self.cursor.execute("INSERT INTO TREATMENTS (PATIENT_ID, TREATMENT_NAME, TREATMENT_CODE, COST, DATE_TREATED) VALUES (?, ?, ?, ?, ?)", 
                                (patient_id, treatment, treatment_code, treatment_cost, "2024-12-18"))
            self.conn.commit()
            messagebox.showinfo("Success", "Treatment added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def add_prescription(self):
        patient_id = self.entPatientID.get()
        medicine_name = self.entMedicineName.get()
        quantity = self.entMedicineQuantity.get()
        medicine_cost = self.entMedicineCost.get()

        if not patient_id or not medicine_name or not quantity:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        try:
            self.cursor.execute("INSERT INTO PRESCRIPTIONS (PATIENT_ID, MEDICINE_NAME, QUANTITY, COST, DATE_PRESCRIBED) VALUES (?, ?, ?, ?, ?)", 
                                (patient_id, medicine_name, quantity, medicine_cost, "2024-12-18"))
            self.conn.commit()
            messagebox.showinfo("Success", "Prescription added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def __del__(self):
        # Close database connection when the window is closed
        self.conn.close()

# Main application to run the Medical Records window
if __name__ == "__main__":
    root = Tk()
    app = MedicalRecords(root)
    root.mainloop()
