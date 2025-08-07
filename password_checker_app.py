import streamlit as st
from zxcvbn import zxcvbn
import math

# Sample list of most common leaked passwords (extendable)
leaked_passwords = [
    '123456', 'password', '123456789', '12345678', '12345',
    'qwerty', 'abc123', 'football', '123123', '111111',
    'welcome', 'monkey', 'dragon', 'letmein', 'admin'
]

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

# --- Streamlit UI ---
st.set_page_config(page_title="🔐 Smart Password Checker", layout="centered")

st.title("🔐 Smart Password Checker")
st.caption("Check if your password is strong, safe, and unguessable.")

password = st.text_input("Enter your password", type="password")

if password:
    st.divider()
    
    # Run analysis
    analysis = zxcvbn(password)
    score = analysis['score']
    entropy_val = entropy(password)
    crack_time = analysis['crack_times_display']['offline_fast_hashing_1e10_per_second']
    label, icon = strength_label(score)

    # Results
    st.subheader("🔍 Password Analysis")
    st.markdown(f"**Strength:** {label} {icon}")
    st.markdown(f"**Entropy:** {entropy_val} bits")
    st.markdown(f"**Estimated Crack Time:** `{crack_time}`")
    
    # Leaked password check
    if is_leaked(password):
        st.error("❌ This password is among the most commonly leaked ones!")
    else:
        st.success("✅ This password is not a commonly leaked one.")
    
    # Suggestions
    suggestions = get_suggestions(password)
    if suggestions:
        st.warning("🔧 Suggestions to improve your password:")
        for s in suggestions:
            st.markdown(f"- {s}")
    else:
        st.success("✅ Your password meets all best practices!")

    st.divider()

    st.caption("⚠️ Never reuse passwords across platforms. Use a password manager for safe storage.")

