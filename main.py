# import os
# import sqlite3
# from crypto_utils import hash_password, verify_password, encrypt_password, decrypt_password, derive_key
# from database import init_db
# import secrets
# import string

# init_db()

# def generate_password(length=16):
#     chars = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(secrets.choice(chars) for _ in range(length))

# def register(username, master_password):
#     conn = sqlite3.connect("passwords.db")
#     c = conn.cursor()
#     c.execute("SELECT * FROM users WHERE username = ?", (username,))
#     if c.fetchone():
#         print(" Username already exists.")
#         return
#     hashed = hash_password(master_password)
#     c.execute("INSERT INTO users (username, master_hash) VALUES (?, ?)", (username, hashed))
#     conn.commit()
#     print(" User registered.")
#     conn.close()

# def login(username, master_password):
#     conn = sqlite3.connect("passwords.db")
#     c = conn.cursor()
#     c.execute("SELECT id, master_hash FROM users WHERE username = ?", (username,))
#     user = c.fetchone()
#     if not user:
#         print(" User not found.")
#         return None, None
#     user_id, master_hash = user
#     if verify_password(master_password, master_hash):
#         print(" Login successful.")
#         return user_id, derive_key(master_password)
#     else:
#         print(" Invalid credentials.")
#         return None, None

# def store_password(user_id, key, site, password):
#     conn = sqlite3.connect("passwords.db")
#     c = conn.cursor()
#     encrypted = encrypt_password(key, password)
#     c.execute("INSERT INTO passwords (user_id, site, encrypted_password) VALUES (?, ?, ?)", (user_id, site, encrypted))
#     conn.commit()
#     print(f" Password stored for {site}")
#     conn.close()

# def retrieve_password(user_id, key, site):
#     conn = sqlite3.connect("passwords.db")
#     c = conn.cursor()
#     c.execute("SELECT encrypted_password FROM passwords WHERE user_id = ? AND site = ?", (user_id, site))
#     row = c.fetchone()
#     if row:
#         encrypted = row[0]
#         decrypted = decrypt_password(key, encrypted)
#         print(f" Password for {site}: {decrypted}")
#     else:
#         print(" No password found.")
#     conn.close()

# def main():
#     print("Secure Password Manager")
#     print("1. Register")
#     print("2. Login")
#     choice = input("Choose option: ")

#     if choice == "1":
#         username = input("Username: ")
#         password = input("Master Password: ")
#         register(username, password)
#     elif choice == "2":
#         username = input("Username: ")
#         password = input("Master Password: ")
#         user_id, key = login(username, password)
#         if user_id:
#             while True:
#                 print("\nOptions: 1) Store 2) Retrieve 3) Generate 4) Exit")
#                 opt = input("Select: ")
#                 if opt == "1":
#                     site = input("Site name: ")
#                     pwd = input("Password: ")
#                     store_password(user_id, key, site, pwd)
#                 elif opt == "2":
#                     site = input("Site name: ")
#                     retrieve_password(user_id, key, site)
#                 elif opt == "3":
#                     print("Generated Password:", generate_password())
#                 elif opt == "4":
#                     break

# if __name__ == "__main__":
#     main()
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import sqlite3
from crypto_utils import hash_password, verify_password, encrypt_password, decrypt_password, derive_key
from database import init_db
import secrets
import string

# Initialize database
init_db()

class HackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("💀 Secure Hacker Password Manager")
        self.root.geometry("800x600")

        # Load background
        self.bg_image = Image.open("background.jpg").resize((800, 600))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas_bg = self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.user_id = None
        self.key = None
        self.setup_login_screen()

    def style_label(self, text, y):
        return self.canvas.create_text(400, y, text=text, fill='lime',
                                       font=("Consolas", 16, "bold"))

    def style_entry(self, y, show=None):
        entry = tk.Entry(self.root, show=show, font=("Consolas", 14),
                         fg='lime', bg='black', insertbackground='lime', width=30)
        self.canvas.create_window(400, y, window=entry)
        return entry

    def style_button(self, text, y, command):
        button = tk.Button(self.root, text=text, command=command,
                           bg='black', fg='lime', font=("Consolas", 12),
                           activebackground='green', activeforeground='black')
        self.canvas.create_window(400, y, window=button)
        return button

    def clear_canvas(self):
        self.canvas.delete("all")
        self.canvas_bg = self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

    def setup_login_screen(self):
        self.clear_canvas()
        self.style_label("🛡️LOGIN", 60)
        self.style_label("Username", 120)
        self.username_entry = self.style_entry(150)

        self.style_label("Master Password", 200)
        self.password_entry = self.style_entry(230, show="*")

        self.style_button("📝 Register", 300, self.register)
        self.style_button("🔓 Login", 340, self.login)

    def register(self):
        username = self.username_entry.get()
        master = self.password_entry.get()
        conn = sqlite3.connect("passwords.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        if c.fetchone():
            messagebox.showerror("Error", "Username already exists.")
            return
        hashed = hash_password(master)
        c.execute("INSERT INTO users (username, master_hash) VALUES (?, ?)", (username, hashed))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User registered!")

    def login(self):
        username = self.username_entry.get()
        master = self.password_entry.get()
        conn = sqlite3.connect("passwords.db")
        c = conn.cursor()
        c.execute("SELECT id, master_hash FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        if result and verify_password(master, result[1]):
            self.user_id = result[0]
            self.key = derive_key(master)
            self.setup_main_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials.")

    def setup_main_screen(self):
        self.clear_canvas()
        self.style_label("☠️ DarkLock", 60)
        self.style_button("💾 Store Password", 140, self.store_password)
        self.style_button("🔎 Retrieve Password", 180, self.retrieve_password)
        self.style_button("⚙️ Generate Password", 220, self.generate_password)
        self.style_button("🔐 Logout", 300, self.setup_login_screen)

    def store_password(self):
        site = simpledialog.askstring("Site", "Enter site name:")
        password = simpledialog.askstring("Password", "Enter password:")
        if not site or not password:
            messagebox.showerror("Error", "Site and password required.")
            return
        encrypted = encrypt_password(self.key, password)
        conn = sqlite3.connect("passwords.db")
        c = conn.cursor()
        c.execute("INSERT INTO passwords (user_id, site, encrypted_password) VALUES (?, ?, ?)",
                  (self.user_id, site, encrypted))
        conn.commit()
        conn.close()
        messagebox.showinfo("Saved", f"Password saved for {site}")

    def retrieve_password(self):
        site = simpledialog.askstring("Retrieve", "Enter site name:")
        conn = sqlite3.connect("passwords.db")
        c = conn.cursor()
        c.execute("SELECT encrypted_password FROM passwords WHERE user_id = ? AND site = ?", (self.user_id, site))
        row = c.fetchone()
        if row:
            decrypted = decrypt_password(self.key, row[0])
            messagebox.showinfo("Password", f"{site}: {decrypted}")
        else:
            messagebox.showerror("Not Found", "No password stored for this site.")

    def generate_password(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        generated = ''.join(secrets.choice(chars) for _ in range(16))
        messagebox.showinfo("Generated Password", generated)

if __name__ == "__main__":
    root = tk.Tk()
    app = HackerGUI(root)
    root.mainloop()
