import streamlit as st
import random
import datetime

# List of daily challenges
challenges = [
    "Write down three things you learned today.",
    "Embrace a mistake you made recently and reflect on what it taught you.",
    "Try a task outside your comfort zone and note your experience.",
    "Give constructive feedback to someone in a positive way.",
    "Reframe a past failure as a learning opportunity."
]

# Function to get today's challenge
def get_today_challenge():
    today = datetime.date.today()
    index = today.day % len(challenges)  # Rotate challenges daily
    return challenges[index]

# Streamlit UI
st.title("🌱 Growth Mindset Challenge")

# Justified Motivational Paragraph
st.markdown(
    """
    <div style="text-align: justify;">
        <b>Growth isn’t about instant success—it’s about the small, consistent steps we take every day.</b>  
        Every challenge you face is an opportunity to learn, adapt, and improve. Mistakes are not failures;  
        they are lessons in disguise, guiding you toward a better version of yourself. With each challenge  
        you complete, you’re not just checking off a task—you’re building resilience, strengthening your mindset,  
        and unlocking your true potential. Keep pushing forward, stay curious, and embrace every challenge  
        as a stepping stone to success. The journey of growth starts with a single step.  
        <b>Are you ready to take it?</b> 🚀
    </div>
    """, 
    unsafe_allow_html=True
)

st.header("Today's Challenge")
st.write(get_today_challenge())

# Reflection Section
st.subheader("Your Reflection")
reflection = st.text_area("How did you approach today's challenge?", "")

if st.button("Save Reflection"):
    st.success("Your reflection has been saved!")

# Progress Tracking
st.subheader("Challenge Completion")
completed = st.checkbox("I have completed today's challenge")

if completed:
    st.balloons()
    st.write("🎉 Great job! Keep going!")

st.write("---")
st.write("Come back tomorrow for a new challenge!")
