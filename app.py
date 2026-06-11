import streamlit as st

st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)

# Dark Theme Styling
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3, p, label {
    color: white !important;
}

.stTextInput > div > div > input {
    background-color: #262730;
    color: white;
}

.stTextArea textarea {
    background-color: #262730;
    color: white;
}

.stButton > button {
    background-color: #FF4B4B;
    color: white;
    border-radius: 10px;
    width: 100%;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("📧 Email Spam Detector")
st.write("Detect whether an email is Spam or Legitimate")

# Subject Input
subject = st.text_input(
    "📨 Email Subject",
    placeholder="Enter email subject"
)

# Email Body Input
email_body = st.text_area(
    "📝 Email Content",
    placeholder="Paste email content here...",
    height=250
)

# File Upload
uploaded_file = st.file_uploader(
    "📂 Upload Email File",
    type=["txt"]
)

# Read uploaded file if provided
if uploaded_file is not None:
    email_body = uploaded_file.read().decode("utf-8")
    st.text_area(
        "📄 Uploaded Content",
        value=email_body,
        height=200
    )

# Detect Button
if st.button("🔍 Detect Spam"):

    if subject.strip() == "" and email_body.strip() == "":
        st.warning("⚠️ Please enter email content.")
    else:

        spam_words = [
            "free",
            "winner",
            "offer",
            "money",
            "urgent",
            "click",
            "prize",
            "claim",
            "cash",
            "congratulations"
        ]

        text = (subject + " " + email_body).lower()

        is_spam = any(
            word in text
            for word in spam_words
        )

        st.subheader("📋 Result")

        if is_spam:
            st.error("🚨 SPAM EMAIL")
        else:
            st.success("✅ NOT SPAM")

st.markdown("---")
st.caption("📧 Email Spam Detector | Built with Streamlit")
