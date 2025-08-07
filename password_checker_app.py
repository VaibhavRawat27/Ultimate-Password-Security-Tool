import streamlit as st
from zxcvbn import zxcvbn
import random
import string
import math

# Leaked password examples
leaked_passwords = [
    '123456', 'password', '123456789', '12345678', '12345',
    'qwerty', 'abc123', 'football', '123123', '111111',
    'welcome', 'monkey', 'dragon', 'letmein', 'admin'
]

# Functions
def is_leaked(password):
    return password.lower() in leaked_passwords

def entropy(password):
    pool = 0
    if any(c.islower() for c in password): pool += 26
    if any(c.isupper() for c in password): pool += 26
    if any(c.isdigit() for c in password): pool += 10
    if any(c in "!@#$%^&*()-_+=<>?/|{}[]" for c in password): pool += 32
    return round(len(password) * math.log2(pool)) if pool else 0

def get_suggestions(password):
    suggestions = []
    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letters.")
    if not any(c.islower() for c in password):
        suggestions.append("Include lowercase letters.")
    if not any(c.isdigit() for c in password):
        suggestions.append("Include numbers.")
    if not any(c in "!@#$%^&*()-_+=<>?/|{}[]" for c in password):
        suggestions.append("Include special characters.")
    return suggestions

def strength_label(score):
    return {
        0: ("Very Weak", "🔴"),
        1: ("Weak", "🟠"),
        2: ("Fair", "🟡"),
        3: ("Strong", "🟢"),
        4: ("Very Strong", "🟢")
    }.get(score, ("Unknown", "⚪"))

def generate_strong_password(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+=<>?/|{}[]"
    return ''.join(random.choice(chars) for _ in range(length))

def improve_existing_password(password):
    # Add complexity to the user-entered password
    base = ''.join(random.sample(password, len(password)))
    extras = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()-_+=<>?/|{}[]")
    ]
    while len(base) + len(extras) < 14:
        extras.append(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()-_+=<>?/|{}[]"))
    improved = base + ''.join(extras)
    return ''.join(random.sample(improved, len(improved)))

# --- Streamlit UI ---
st.set_page_config(page_title="🔐 Ultimate Password Tool", layout="centered")
st.title("🔐 Ultimate Password Security Tool")
st.caption("Analyze, improve, and generate secure passwords instantly.")

# Section: Analyze & Improve Password
st.header("🔍 Analyze & Improve Your Password")
user_password = st.text_input("Enter a password to analyze/improve", type="password")

if user_password:
    st.subheader("Password Analysis Results")
    analysis = zxcvbn(user_password)
    score = analysis['score']
    crack_time = analysis['crack_times_display']['offline_fast_hashing_1e10_per_second']
    entropy_val = entropy(user_password)
    label, icon = strength_label(score)

    st.markdown(f"**Strength:** {label} {icon}")
    st.markdown(f"**Entropy:** `{entropy_val} bits`")
    st.markdown(f"**Estimated Crack Time:** `{crack_time}`")

    if is_leaked(user_password):
        st.error("🚨 This password is commonly leaked! Avoid using it.")
    else:
        st.success("✅ This password is not among commonly leaked ones.")

    suggestions = get_suggestions(user_password)
    if suggestions:
        st.warning("🔧 Suggestions:")
        for s in suggestions:
            st.markdown(f"- {s}")
    else:
        st.success("✅ Your password follows best practices!")

    if st.button("✨ Improve This Password"):
        improved = improve_existing_password(user_password)
        st.info("🔒 Improved Password:")
        st.code(improved, language="text")

st.divider()

# Section: Generate Strong Password
st.header("⚙️ Generate a Strong New Password")
if st.button("🔁 Generate Strong Password"):
    generated = generate_strong_password()
    st.success("Here’s a strong password you can use:")
    st.code(generated, language="text")

st.caption("✅ Tip: Use a password manager to store strong passwords securely.")
