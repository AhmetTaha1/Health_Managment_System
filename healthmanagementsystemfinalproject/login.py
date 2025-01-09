from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from menu import Menu  # Admin menu
from doctor_menu import DoctorMenu  # Doctor-specific menu
from patient_menu import PatientMenu  # Patient-specific menu
import sqlite3


def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("HEALTH ADMINISTRATION MANAGEMENT SYSTEM")
        self.master.geometry("1000x600")  # Window size

        # Load and set the background image
        self.bg_image = Image.open("workers.png").resize((1000, 600), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = Label(self.master, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Login frame
        self.frame = Frame(self.master, bg="lightblue", relief="groove", bd=10)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=300)

        self.username = StringVar()
        self.password = StringVar()

        # Title label
        self.lbl_title = Label(
            self.frame,
            text="HEALTH ADMINISTRATION MANAGEMENT SYSTEM",
            font="Helvetica 16 bold",
            bg="lightblue",
            fg="black",
            wraplength=400,
            justify=CENTER,
        )
        self.lbl_title.pack(pady=10)

        # Login fields
        self.login_frame = Frame(self.frame, bg="lightblue")
        self.login_frame.pack(pady=20)

        Label(self.login_frame, text="Username:", font="Helvetica 12", bg="lightblue", fg="black").grid(row=0, column=0, pady=5, sticky=E)
        Entry(self.login_frame, font="Helvetica 12", textvariable=self.username, width=25).grid(row=0, column=1, pady=5, padx=10)

        Label(self.login_frame, text="Password:", font="Helvetica 12", bg="lightblue", fg="black").grid(row=1, column=0, pady=5, sticky=E)
        Entry(self.login_frame, font="Helvetica 12", show="*", textvariable=self.password, width=25).grid(row=1, column=1, pady=5, padx=10)

        # Buttons
        self.button_frame = Frame(self.frame, bg="lightblue")
        self.button_frame.pack(pady=10)

        Button(self.button_frame, text="Login", font="Helvetica 12 bold", width=12, bg="cadet blue", fg="white", command=self.login_system).grid(row=0, column=0, padx=10)
        Button(self.button_frame, text="Exit", font="Helvetica 12 bold", width=12, bg="cadet blue", fg="white", command=self.exit_app).grid(row=0, column=1, padx=10)

        # Bind Enter key to the login system
        self.master.bind('<Return>', self.trigger_login)

    def trigger_login(self, event=None):
        self.login_system()

    def login_system(self):
        username_input = self.username.get().strip()
        password_input = self.password.get().strip()

        # Check for hardcoded admin credentials
        if (username_input == "admin" and password_input == "1234") or (username_input == "root" and password_input == "4321"):
            new_window = Toplevel(self.master)
            Menu(new_window)  # Admin Menu
            return

        # Check credentials in the database
        conn = sqlite3.connect("HospitalDB.db")
        cursor = conn.cursor()

        try:
            cursor.execute("""
                SELECT ROLE, EMP_ID, PATIENT_ID
                FROM USERS
                WHERE USERNAME = ? AND PASSWORD = ?
            """, (username_input, password_input))
            result = cursor.fetchone()

            if result:
                role, emp_id, patient_id = result

                if role == "doctor" and emp_id:
                    new_window = Toplevel(self.master)
                    DoctorMenu(new_window, emp_id=emp_id)  # Pass EMP_ID to DoctorMenu

                elif role == "patient" and patient_id:
                    new_window = Toplevel(self.master)
                    PatientMenu(new_window, patient_id=patient_id)  # Pass PATIENT_ID to PatientMenu

                elif role == "admin":
                    new_window = Toplevel(self.master)
                    Menu(new_window)  # Admin Menu

                else:
                    tkinter.messagebox.showerror("Login Error", "Invalid role or missing credentials!")

            else:
                tkinter.messagebox.showerror("Login Error", "Invalid username or password.")

        except sqlite3.Error as e:
            tkinter.messagebox.showerror("Database Error", f"An error occurred: {e}")

        finally:
            conn.close()

    def exit_app(self):
        self.master.destroy()


if __name__ == "__main__":
    main()
