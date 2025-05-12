import streamlit as st
import random


st.set_page_config(page_title="Growth Mindset 💡", layout="centered")


st.markdown("""
    <style>
        .main {
            background-color: #f0f4f8;
        }
        .title {
            font-size: 40px;
            font-weight: 700;
            text-align: center;
            color: #2c3e50;
        }
        .quote-box {
            background-color: #e0f7fa;
            padding: 25px;
            border-radius: 15px;
            margin-top: 20px;
            font-size: 24px;
            color: #006064;
            font-style: italic;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            margin-top: 50px;
            color: #95a5a6;
        }
    </style>
""", unsafe_allow_html=True)


quotes = [
    "Failure is a stepping stone to success. 🌱",
    "I can learn anything I want to. 💪",
    "Challenges help me grow. 🚀",
    "My effort and attitude determine my abilities. 🎯",
    "I embrace the process of learning. 📚",
    "Every mistake is a chance to improve. 🔁",
    "Success comes from effort, not talent alone. 🔥",
    "I am not afraid of failure. 🌟",
    "Feedback is a gift. 🎁",
    "The power of 'yet' turns 'I can't' into 'I can't yet'. 🧠"
]

st.markdown('<div class="title">🚀 Growth Mindset Generator</div>', unsafe_allow_html=True)


if st.button("✨ Inspire Me"):
    st.markdown(f'<div class="quote-box">{random.choice(quotes)}</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="quote-box">{quotes[0]}</div>', unsafe_allow_html=True)


mood = st.selectbox("How are you feeling today?", ["😊 Happy", "😐 Neutral", "😞 Low"])
if mood == "😞 Low":
    st.info("You're not alone. Every expert was once a beginner. Keep going! 💖")
elif mood == "😐 Neutral":
    st.success("Let today be a step forward. You got this! 💼")
else:
    st.balloons()
    st.success("Awesome! Keep sharing that energy! 🌈")


st.markdown('<div class="footer">Made with 💙 using Streamlit | #GrowthMindset</div>', unsafe_allow_html=True)
