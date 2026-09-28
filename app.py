import streamlit as st
st.title("Student Marks Calculator")

name = st.text_input("Enter your name")

col1, col2 = st.columns(2)

with col1:
    maths = st.number_input("Maths Marks", min_value=0, max_value=100)
    java = st.number_input("Java Marks", min_value=0, max_value=100)

with col2:
    dbms = st.number_input("DBMS Marks", min_value=0, max_value=100)
    cn = st.number_input("CN Marks", min_value=0, max_value=100)

if st.button("Calculate Result"):
    total = maths + java + dbms + cn
    percentage = total/4

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >=70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    st.success("Result Calculated!")

    st.subheader("Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Marks", f"{total}/400")

    with col2:
        st.metric("Percentage",f"{percentage}%")

    with col3:
        st.metric("Grade", grade)

    st.progress(percentage/100)

    if percentage >=50:
        st.success("PASS")
    else:
        st.error("FAIL")

    if st.button("Reset"):
        st.rerun()
