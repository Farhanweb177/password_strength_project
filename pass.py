import streamlit as st
import re

st.set_page_config(page_title="Password strength checker",page_icon="g")

st.title("password strength checker")
st.markdown("""
## welcome! to the ultimate password strenth checker!
use this simple tool to check the strenth of your password and get suggestion on how to make it stronger
            we will give you helpfull tip to create a strong password""")

password = st.text_input("enter your password",type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("password should be at least 8 characters long")

    if re.search(r'[A-Z]',password) and re.search(r'[a-z]',password):
        score += 1
    else:
        feedback.append("password should contain both uppercase and lowercase letters")

    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("password should contain at least one number")

    if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\]",password):
        score += 1
    else:
        feedback.append("password should contain at least one special character")
    if score == 4:
        feedback.append("your password is strong!")
    elif score == 3:
        feedback.append("your password is good, but consider adding more complexity")
    else:
        feedback.append("your password is weak, consider making it stronger")

    if feedback:
        st.markdown("## improve suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("please enter a password to check its strength")
        
