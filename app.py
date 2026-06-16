import streamlit as st
st.title("Loginpage")
username = st.text_input("Username")
password = st.text_input("Password", type="password")
if st.button("Login"):
    if username == "vamshi" and password == "123":
        st.success("Login successful")
    else:
        st.error("Invalid username or password")    