import sqlite3

try:
    conn = sqlite3.connect("ВВЕДИТЕИМЯБД.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO'users")
except sqlite3.Error as error:
    print("Error", error)
finally:
    if(conn):
        conn.close()