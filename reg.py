import streamlit as st
st.title("Registration Form")
name=st.text_input("Enter your name")
email=st.text_input("Enter your email") 
age=st.number_input("Enter your age",min_value=1,max_value=100) 
gender=st.radio("Select your gender",["Male","Female","others"])
course=st.selectbox("Select your course",["Python","Java","C++","Data Science"])
if st.button("Registration"):
    if name and email:
        st.success(f"Registration successful! Welcome {name} to the {course} course.")
        st.write(f"Name: {name}")
        st.write(f"Email: {email}") 
        st.write(f"Age: {age}") 
        st.write(f"Gender: {gender}")  
        st.write(f"Course: {course}")

    else:
        st.error("Please fill in all the required fields.")
        