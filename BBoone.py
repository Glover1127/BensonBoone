import streamlit as st
import random
import pandas as pd

# Trivia data structure
questions = [
    {"question": "Which show did Benson Boone audition for?", "options": ["America's Got Talent", "American Idol", "The Voice"], "answer": "American Idol", "difficulty": "Easy"},
    {"question": "Which platform made Benson Boone famous first?", "options": ["YouTube", "Instagram", "TikTok"], "answer": "TikTok", "difficulty": "Easy"},
    {"question": "What was Benson Boone's first major hit song?", "options": ["Sugar Sweet", "Ghost Town", "Beautiful Things"], "answer": "Ghost Town", "difficulty": "Easy"},
    {"question": "Benson Boone primarily plays what instrument?", "options": ["Violin", "Piano", "Drums"], "answer": "Piano", "difficulty": "Medium"},
    {"question": "In what month was Benson Boone born?", "options": ["June", "October", "December"], "answer": "June", "difficulty": "Medium"},
    {"question": "Which U.S. state is Benson Boone originally from?", "options": ["California", "Washington", "Texas"], "answer": "Washington", "difficulty": "Medium"},
    {"question": "Which major record label signed Benson Boone first?", "options": ["Warner Records", "Sony Music", "Capitol Records"], "answer": "Warner Records", "difficulty": "Hard"}
]

# Shuffle questions
random.shuffle(questions)

# Initialize or load leaderboard
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = pd.DataFrame(columns=['Name', 'Score'])

# App layout
st.title("🎤 Benson Boone Trivia Game 🎶")

user_name = st.text_input("Enter your name to start:")

if user_name:
    score = 0
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}: ({q['difficulty']})")
        answer = st.radio(q["question"], options=q["options"], key=f"q{i}")
        if answer == q["answer"]:
            score += 1

    if st.button("Submit Answers"):
        st.success(f"{user_name}, your score is {score}/{len(questions)}")
        # Update leaderboard
        new_entry = pd.DataFrame([[user_name, score]], columns=['Name', 'Score'])
        st.session_state.leaderboard = pd.concat([st.session_state.leaderboard, new_entry], ignore_index=True)
        st.session_state.leaderboard = st.session_state.leaderboard.sort_values(by='Score', ascending=False)

    st.header("🏆 Leaderboard")
    st.dataframe(st.session_state.leaderboard.reset_index(drop=True))