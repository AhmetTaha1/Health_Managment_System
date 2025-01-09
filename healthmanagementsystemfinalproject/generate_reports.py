import sqlite3
from tkinter import *
from tkinter.ttk import Treeview

class GenerateReports:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1000x700")
        self.master.config(bg="light blue")

        # Variables
        self.conn = sqlite3.connect("HospitalDB.db")
        self.report_type = StringVar()
        self.report_type.set("Monthly Patient Visits")

        # Title
        self.lblTitle = Label(self.master, text="GENERATE REPORTS", font="Helvetica 20 bold", bg="light blue")
        self.lblTitle.pack(pady=20)

        # Frame for Report Selection
        self.ReportFrame = Frame(self.master, bg="light blue")
        self.ReportFrame.pack(pady=20)

        self.lblReportType = Label(self.ReportFrame, text="Select Report Type:", font="Helvetica 14 bold", bg="light blue")
        self.lblReportType.grid(row=0, column=0, padx=10, pady=10)

        self.reportMenu = OptionMenu(
            self.ReportFrame,
            self.report_type,
            "Monthly Patient Visits",
            "Treatment Statistics",
            "Doctor Workload",
            "Revenue Report"
        )
        self.reportMenu.config(font="Helvetica 12", width=25)
        self.reportMenu.grid(row=0, column=1, padx=10, pady=10)

        self.btnGenerate = Button(self.ReportFrame, text="Generate Report", font="Helvetica 14 bold", bg="light blue", command=self.generate_report)
        self.btnGenerate.grid(row=0, column=2, padx=10, pady=10)

        # Frame for Results
        self.ResultFrame = Frame(self.master, bg="light blue")
        self.ResultFrame.pack(fill=BOTH, expand=True, pady=20)

        # Treeview for displaying results
        self.tree = Treeview(self.ResultFrame, show="headings")
        self.tree.pack(fill=BOTH, expand=True, padx=20, pady=20)

    def generate_report(self):
        """Fetch and display data for the selected report."""
        report = self.report_type.get()
        cursor = self.conn.cursor()

        # Clear previous results
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = ()  # Reset columns

        if report == "Monthly Patient Visits":
            cursor.execute("""
                SELECT strftime('%Y-%m', AP_DATE) AS Month, 
                       COUNT(DISTINCT PATIENT_ID) AS TotalPatients
                FROM APPOINTMENT
                GROUP BY Month
                ORDER BY Month;
            """)
            self.display_results(cursor, ["Month", "Total Patients"])

        elif report == "Treatment Statistics":
            cursor.execute("""
                SELECT TREATMENT, 
                       COUNT(*) AS TotalOccurrences, 
                       SUM(T_COST) AS TotalCost
                FROM TREATMENT
                GROUP BY TREATMENT
                ORDER BY TotalOccurrences DESC;
            """)
            self.display_results(cursor, ["Treatment", "Total Occurrences", "Total Cost"])

        elif report == "Doctor Workload":
            cursor.execute("""
                SELECT EMPLOYEE.EMP_NAME AS DoctorName, 
                    COUNT(APPOINTMENT.AP_NO) AS TotalAppointments
                FROM EMPLOYEE
                JOIN APPOINTMENT ON EMPLOYEE.EMP_ID = APPOINTMENT.EMP_ID
                GROUP BY EMPLOYEE.EMP_NAME
                ORDER BY TotalAppointments DESC;
            """)
            self.display_results(cursor, ["Doctor Name", "Total Appointments"])

        elif report == "Revenue Report":
            cursor.execute("""
                SELECT strftime('%Y-%m', DATE_ADMITTED) AS Month, 
                       SUM(RATE) AS RoomRevenue, 
                       SUM(M_COST) AS MedicineRevenue, 
                       SUM(T_COST) AS TreatmentRevenue, 
                       SUM(RATE + M_COST + T_COST) AS TotalRevenue
                FROM ROOM
                LEFT JOIN MEDICINE USING(PATIENT_ID)
                LEFT JOIN TREATMENT USING(PATIENT_ID)
                GROUP BY Month
                ORDER BY Month;
            """)
            self.display_results(cursor, ["Month", "Room Revenue", "Medicine Revenue", "Treatment Revenue", "Total Revenue"])

    def display_results(self, cursor, columns):
        """Display query results in the Treeview."""
        self.tree["columns"] = columns
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        for row in cursor.fetchall():
            self.tree.insert("", "end", values=row)


# Main Application
if __name__ == "__main__":
    root = Tk()
    app = GenerateReports(root)
    root.mainloop()
