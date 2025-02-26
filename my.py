import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🚀", layout="wide", initial_sidebar_state="expanded")

# Custom Header Styling
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #2E86C1;
        }
        .sub-header {
            text-align: center;
            font-size: 20px;
            color: #5D6D7E;
        }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<div class='main-title'>🌱 Growth Mindset Challenge 🚀</div>", unsafe_allow_html=True)

# Introduction
st.markdown("<div class='sub-header'>Unlock Your Potential: Learn, Grow & Succeed!</div>", unsafe_allow_html=True)

st.write("---")

# Quotes Section
st.header("🌟 Inspirational Quote of the Day")
st.success("""“Success is not final, failure is not fatal: It is the courage to continue that counts.” - Winston Churchill""")

st.write("---")

# User Input: Challenge
st.header("🔥 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.info(f"You're facing: **{user_input}**. Keep pushing forward – You’ve got this! 💪")
else:
    st.warning("Tell us about your challenge today to get started!")

st.write("---")

# Reflection Section
st.header("📝 Daily Reflections")
reflection = st.text_area("How did you overcome your challenge today?")

if reflection:
    st.success(f"Great insight! You've learned: **{reflection}** ✨")
else:
    st.info("Reflect on your day and write down your thoughts here.")

st.write("---")

# Achievement Section
st.header("🏆 Celebrate Your Achievements")
achievement = st.text_input("Share something you've accomplished today:")

if achievement:
    st.balloons()
    st.success(f"🎉 Congratulations! You've achieved: **{achievement}**")
else:
    st.info("Big or small, every achievement counts! Share it here.")

st.write("---")

# Inspiration Section
st.header("🌈 Share Your Inspiration")
inspiration = st.text_area("What inspired you today?")

if inspiration:
    st.success(f"Great Inspiration! You’ve shared: **{inspiration}** 💡")
else:
    st.info("Share something that inspired you today.")

st.write("---")

# Footer
st.markdown("""
    <div style="text-align: center; color: #7D3C98; font-size: 16px;">
        ✨ This Growth Mindset Web App is created by <b>Hina</b> 🚀
    </div>
""", unsafe_allow_html=True)
