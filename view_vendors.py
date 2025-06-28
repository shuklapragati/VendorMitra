import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("PRAGMA table_info(vendors)")
columns = c.fetchall()
print("🧾 Table Structure (Columns):")
for col in columns:
    print(f"- {col[1]}")

print("\n📦 Vendor Data:")
c.execute("SELECT * FROM vendors")
rows = c.fetchall()

for row in rows:
    print(row)

conn.close()
