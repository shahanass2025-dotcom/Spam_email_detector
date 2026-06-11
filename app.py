import streamlit as st

st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)
[theme]
base="dark"
primaryColor="#FF4B4B"
backgroundColor="#0E1117"
secondaryBackgroundColor="#262730"
textColor="#FAFAFA"

email_body = st.text_area(
    "📝 Email Content",
    placeholder="Paste email content here...",
    height=250
)

uploaded_file = st.file_uploader(
    "📂 Upload Email File",
    type=["txt"]
)

if st.button("🔍 Detect Spam"):

    if subject == "" and email_body == "":
        st.warning("⚠️ Please enter email content.")
    else:

        spam_words = [
            "free",
            "winner",
            "offer",
            "money",
            "urgent",
            "click"
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
st.caption("Email Spam Detector")
