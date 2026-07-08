# Secure-Password-Manager


A secure desktop-based Password Manager developed in Python that enables users to safely store, retrieve, and generate passwords using modern cryptographic techniques. The application follows cybersecurity best practices by combining **AES-256 encryption**, **bcrypt hashing**, **SHA-256 key derivation**, and **SQLite** for secure credential management.

## ✨ Features

- 🔐 Secure user registration and login
- 🔑 Master password hashing using bcrypt with automatic salting
- 🛡️ AES-256 encryption for stored website passwords
- 🔒 SHA-256 based key derivation
- 💾 Secure local SQLite database storage
- 🎲 Strong password generator
- 🖥️ User-friendly graphical interface
- 🔍 Database inspection utility for debugging and verification

---

## 🛠️ Technologies Used

- Python
- Tkinter
- SQLite
- bcrypt
- hashlib (SHA-256)
- Cryptography (AES-256)
- secrets module

---

## 📂 Project Structure

```
SecurePasswordManager/
│── app.py
│── auth.py
│── encryption.py
│── database.py
│── password_generator.py
│── inspect_db.py
│── passwords.db
│── assets/
│── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Secure-Password-Manager.git
```

### Navigate to the project

```bash
cd Secure-Password-Manager
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

---

## 🔐 Security Features

### Master Password Protection
- Passwords are hashed using **bcrypt**
- Unique salt generated automatically
- Passwords are never stored in plaintext

### Password Encryption
- Website passwords are encrypted using **AES-256**
- Encryption key is derived using **SHA-256**
- Only authenticated users can decrypt stored passwords

### Secure Storage
- SQLite database stores encrypted credentials
- Master passwords remain hashed
- Sensitive information is protected from unauthorized access

### Password Generator
- Generates cryptographically secure passwords
- Includes:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters

---

## 📖 How It Works

1. Register using a username and master password.
2. The master password is hashed using bcrypt.
3. Log in securely using your credentials.
4. Save website credentials.
5. Passwords are encrypted before storage.
6. Retrieve and decrypt passwords only after successful authentication.
7. Generate strong random passwords whenever needed.

---

## 🎯 Learning Outcomes

- Password Hashing (bcrypt)
- Password Salting
- AES-256 Encryption
- SHA-256 Key Derivation
- Secure Authentication
- SQLite Database Security
- Python GUI Development
- Secure Password Generation
- Applied Cryptography

---

## 📸 Screenshots

Add screenshots here.

```md
![Login](screenshots/login.png)

![Dashboard](screenshots/dashboard.png)

![Password Generator](screenshots/password_generator.png)
```

---

## ⚠️ Disclaimer

This project was developed solely for educational and learning purposes to demonstrate secure password management techniques and modern cryptographic practices. It is not intended for production use without additional security enhancements and testing.


---

## 📚 References

- OWASP Password Storage Cheat Sheet
- NIST Digital Identity Guidelines (SP 800-63B)
- Python Cryptography Documentation
- SQLite Documentation

---

⭐ If you found this project useful, consider giving it a star!
