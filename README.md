# 🔐 Ultimate Password Security Tool

A powerful and interactive **Streamlit web app** to check, improve, and generate strong, secure passwords. This tool analyzes password strength, entropy, crack time, detects common leaked passwords, and offers suggestions for creating more secure passwords.

## 🚀 Features

- 🔍 Analyze password strength using `zxcvbn`
- ⚠️ Detect if a password is commonly leaked
- 🧠 Get real-time suggestions to improve weak passwords
- 🔁 Auto-generate improved version of a weak password
- 🔐 Generate brand new strong passwords with one click
- 📊 View password entropy and estimated crack time
- 💬 Friendly UI with Streamlit

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [zxcvbn-python](https://github.com/dwolfhub/zxcvbn-python)

## 📦 Installation

1. Clone this repository or download the script.

2. Install required packages:

```bash
pip install streamlit zxcvbn
```

3. Run the app:

```bash
streamlit run password_checker_app.py
```

## 📸 Screenshots

<img width="992" height="600" alt="image" src="https://github.com/user-attachments/assets/835bacf4-151d-4e7b-813b-37e538373e9a" />

<img width="852" height="516" alt="image" src="https://github.com/user-attachments/assets/85bcd664-476a-44b2-8585-5eb483e19f64" />

<img width="1060" height="333" alt="image" src="https://github.com/user-attachments/assets/e9d1f967-2d9d-4d44-8ea9-5382c5b2bb92" />

## 🧩 Example Use

- Enter password: `123456`
- Result: Very Weak, Leaked, Suggestions provided
- Click "✨ Improve This Password" to get something like: `A1@6c5#3gFd!Z`
- Use "🔁 Generate Strong Password" to get a random secure one

## ✅ Best Practices

- Use 12+ characters, mix upper/lowercase, digits & symbols
- Never reuse passwords across sites
- Use a password manager

## 🔒 Disclaimer

This app is for educational and demo purposes only. Passwords are never stored or sent anywhere.

## 👨‍💻 Author

Made with ❤️ by [Your Name]

---

> Feel free to contribute, report bugs, or request features!
