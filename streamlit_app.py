import streamlit as st

st.set_page_config(page_title="Staff Login", page_icon="🔐", layout="centered")

st.title("Staff Login")
st.write("Please enter your staff ID number and password to sign in.")

with st.form(key="login_form"):
    staff_id = st.text_input("Staff ID number", max_chars=20)
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Log in")

# Fake account for testing
VALID_STAFF_ID = "12345"
VALID_PASSWORD = "hellotech"

if submitted:
    if not staff_id or not password:
        st.error("Please enter both your staff ID and password.")
    elif staff_id == VALID_STAFF_ID and password == VALID_PASSWORD:
        st.success("Login successful")
        st.write("You have signed in using the test account.")
    else:
        st.error("Invalid staff ID or password. Please try again.")
        st.info("Forgot Password? Click here for a reset link.")
        st.markdown("[Forgot Password](#)")

st.caption("This is a simple login UI with a test account. Use staff ID 12345 and password hellotech.")
