import sqlite3
conn = sqlite3.connect("HospitalDB.db")

# Add trigger to notify doctors when their schedules are full
conn.execute("""
CREATE TRIGGER NotifyDoctorWhenFull
AFTER INSERT ON APPOINTMENT
BEGIN
    INSERT INTO NOTIFICATIONS (EMP_ID, MESSAGE)
    SELECT NEW.EMP_ID, 'Your schedule is full for ' || NEW.AP_DATE
    WHERE (
        SELECT COUNT(*) 
        FROM APPOINTMENT 
        WHERE EMP_ID = NEW.EMP_ID AND AP_DATE = NEW.AP_DATE
    ) > 10;
END;
""")
print("TRIGGER TO NOTIFY DOCTORS CREATED SUCCESSFULLY")