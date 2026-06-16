import streamlit as st
st.title("METRO+CAB BOOKING")
stations=[
    "JNTUH",
    "MYP",
    "AMEERPET",
    "LB NAGAR"
]
from_station=st.selectbox("From Stations",stations) 
to_station=st.selectbox("To station",stations) 
tickets=st.number_input("No of tickets",min_value=1,max_value=10)
need_cab=st.radio("Do YOu Need a cab ?",["Yes","No"],index=None)
st.write("From Station:",from_station)
st.write("To Station:",to_station)  
cab_destination=""
cab_fare=0
if need_cab=="Yes":
    cab_destination=st.text_input("Cab Destination")
    cab_fare=130
if st.button("Book Now"):
    if from_station==to_station:
        st.error("From and To stations are same") 
    else:
        metro_fare=20*tickets
        total_fare=metro_fare+cab_fare
        st.success("Booking Successful")
        st.subheader("***Bill Details***")
        st.write(f"From Station: {from_station}")
        st.write(f"To Station: {to_station}")
        st.write(f"Number of Tickets: {tickets}")
        st.write(f"Metro Fare: {metro_fare}")
        if need_cab=="Yes": 
             st.write(f"Cab From: {to_station}")
             st.write(f"Cab To: {cab_destination}")
             st.write(f"Cab bill: {cab_fare}")
             st.write(f"Total Fare: {total_fare}")