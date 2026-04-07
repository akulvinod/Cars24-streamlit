import streamlit as st

st.title("My First Streamlit App")
st.header("Deploying using :blue[Streamlit Cloud]")
st.write("Learning streamlit for ML model deployment!")

agree = st.checkbox("I agree with akul!!")

if agree:
    st.write("You're Great!")