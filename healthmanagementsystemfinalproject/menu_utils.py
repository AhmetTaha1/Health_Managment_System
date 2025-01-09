import sqlite3
from tkinter import messagebox
from tkinter import Toplevel
from tkinter.ttk import Treeview

def open_table_window(master, title, columns, query, params=()):
    window = Toplevel(master)
    window.title(title)
    window.geometry("600x400")

    # Table setup
    tree = Treeview(window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    try:
        # Connect to the database
        conn = sqlite3.connect("HospitalDB.db")
        cursor = conn.cursor()
        rows = cursor.execute(query, params).fetchall()
        for row in rows:
            tree.insert("", "end", values=row)
        if not rows:
            messagebox.showinfo("No Data", f"No records found for {title.lower()}.")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        if conn:
            conn.close()

def save_to_database(query, params, success_message, error_message):
    try:
        # Connect to the database
        conn = sqlite3.connect("HospitalDB.db")
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        messagebox.showinfo("Success", success_message)
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"{error_message}: {e}")
    finally:
        if conn:
            conn.close()
