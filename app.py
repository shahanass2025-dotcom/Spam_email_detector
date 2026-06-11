import streamlit as st

st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)
theme = st.sidebar.radio(
    "🎨 Select Theme",
    ["Dark", "Light"]
)

if theme == "Dark":
    st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: white;
        }

        .stTextInput > div > div > input,
        .stTextArea textarea {
            background-color: #262730;
            color: white;
        }

        .stButton > button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
        <style>
        .stApp {
            background-color: white;
            color: black;
        }

        .stTextInput > div > div > input,
        .stTextArea textarea {
            background-color: white;
            color: black;
        }

        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)
st.title("📧 Email Spam Detector")
st.write("Detect whether an email is Spam or Legitimate")

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
