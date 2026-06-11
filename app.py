import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="wide"
)

# Header
st.title("📧 Email Spam Detector")
st.markdown("### Detect whether an email is Spam or Legitimate")

# Sidebar
with st.sidebar:
    st.header("📌 Project Information")
    st.write("Email Spam Detector using Machine Learning")
    st.write("Frontend: Streamlit")
    st.write("Backend: Python")
    st.write("Database: MongoDB")
    
    st.header("👨‍💻 Team")
    st.write("Add Team Members Here")

# Main Layout
col1, col2 = st.columns([2, 1])

with col1:
    subject = st.text_input(
        "📨 Email Subject",
        placeholder="Enter email subject"
    )

    email_body = st.text_area(
        "📝 Email Content",
        placeholder="Paste email content here...",
        height=250
    )

    uploaded_file = st.file_uploader(
        "📂 Upload Email File",
        type=["txt"]
    )

    detect = st.button("🔍 Detect Spam")

with col2:
    st.subheader("📊 Statistics")

    st.metric("Emails Checked", "150")
    st.metric("Spam Detected", "42")
    st.metric("Accuracy", "98%")

# Prediction Section
if detect:

    if subject == "" and email_body == "":
        st.warning("⚠️ Please enter email content.")
    else:

        # Dummy Prediction Logic
        spam_words = [
            "free",
            "winner",
            "prize",
            "money",
            "offer",
            "click",
            "urgent"
        ]

        text = (subject + " " + email_body).lower()

        is_spam = any(word in text for word in spam_words)

        st.divider()
        st.subheader("📋 Detection Result")

        if is_spam:
            st.error("🚨 This Email is SPAM")
            st.progress(90)
            st.write("Spam Probability: 90%")
        else:
            st.success("✅ This Email is NOT SPAM")
            st.progress(20)
            st.write("Spam Probability: 20%")

# Footer
st.divider()
st.caption("© 2026 Email Spam Detector Project")
