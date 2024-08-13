import streamlit as st
st.header("Please upload an image of a shoe")
file = st.file_uploader("", type=["jpeg", "jpg", "png"])