import streamlit as st
from PIL import Image
from utils.streamlit_utils import hide_icons, hide_sidebar, remove_whitespaces
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title = "Blockchain- Based Certificate Verification System", layout="centered", initial_sidebar_state="collapsed")
hide_icons()
hide_sidebar()
remove_whitespaces()

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html= True)

st.title("Certificate Verification System")
st.write("")
st.subheader("Select Your Role")

col1, col2 = st.columns(2)
institite_logo = Image.open("../assets/institute_logo.png")
with col1:
    st.image(institite_logo, output_format="jpg", width=230)
    clicked_institute = st.button("Institute")

company_logo = Image.open("../assets/company_logo.jpg")
with col2:
    st.image(company_logo, output_format="jpg", width=260)
    clicked_verifier = st.button("Verifier")

if clicked_institute:
    st.session_state.profile = "Institute"
    switch_page('login')
elif clicked_verifier:
    st.session_state.profile = "Verifier"
    switch_page('login')

