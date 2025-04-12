import streamlit as st

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{};:,.<>?" for c in password):
        score += 1

    if score <= 1:
        return " Very Weak"
    elif score == 2:
        return " Weak"
    elif score == 3:
        return " Moderate"
    else:
        return " Strong"

st.title(" Simple Password Strength Checker")

pwd = st.text_input("Enter password", type="password")

if pwd:
    st.write("Strength:", check_strength(pwd))
