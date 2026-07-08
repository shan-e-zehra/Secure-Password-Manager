import sqlite3

conn = sqlite3.connect("passwords.db")
c = conn.cursor()

print("\n--- USERS TABLE ---")
for row in c.execute("SELECT id, username, master_hash FROM users"):
    print(row)

print("\n--- PASSWORDS TABLE ---")
for row in c.execute("SELECT id, user_id, site, encrypted_password FROM passwords"):
    print(row)

conn.close()
