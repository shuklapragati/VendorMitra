import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

try:
    c.execute("ALTER TABLE vendors ADD COLUMN location_lat TEXT")
    c.execute("ALTER TABLE vendors ADD COLUMN location_lng TEXT")
    print("✅ Columns 'location_lat' and 'location_lng' added successfully.")
except Exception as e:
    print("⚠️ Error:", e)

conn.commit()
conn.close()
