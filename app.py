import streamlit as st

# App Title with Your Name
st.title("🌱 Growth Mindset Challenge by Anum Munir")

# Subtitle
st.subheader("Develop Your Potential with the Right Mindset")

# Introduction
st.write("""
### Welcome to the Growth Mindset Challenge!  
I'm **Anum Munir**, and this app is designed to help you develop a **growth mindset**.  
A **growth mindset** means believing that intelligence and abilities can improve through effort and learning.  
Use this app to track your challenges, set goals, and stay motivated!
""")

# User Input Section
name = st.text_input("Enter your name:")
goal = st.text_area("What is one challenge you're working on right now?")

if st.button("Submit"):
    if name and goal:
        st.success(f"Great job, {name}! Keep pushing through your challenge: {goal}")
    else:
        st.warning("Please enter both your name and your challenge.")

# Growth Mindset Tips
st.subheader("💡 Growth Mindset Tips by Anum Munir")
tips = [
    "🔹 Embrace challenges as learning opportunities.",
    "🔹 Learn from mistakes instead of fearing them.",
    "🔹 Stay persistent when things get tough.",
    "🔹 Celebrate effort, not just results.",
    "🔹 Seek feedback and use it to grow."
]

for tip in tips:
    st.write(tip)

st.write("🚀 Keep growing and never stop learning!")
