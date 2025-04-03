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

# Shuffle questions once
if 'shuffled_questions' not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.current_q = 0
    st.session_state.answers = {}
    st.session_state.score = 0
    st.session_state.next_q = False

# Initialize leaderboard
if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = pd.DataFrame(columns=['Name', 'Score'])

st.title("🎤 Benson Boone Trivia Game 🎶")

user_name = st.text_input("Enter your name to start:")

if user_name:
    q_index = st.session_state.current_q
    if q_index < len(st.session_state.shuffled_questions):
        q = st.session_state.shuffled_questions[q_index]
        st.subheader(f"Question {q_index+1}: ({q['difficulty']})")
        selected = st.radio(q['question'], q['options'], key=f"question_{q_index}")

        if st.button("Next Question"):
            st.session_state.answers[q_index] = selected
            if selected == q['answer']:
                st.session_state.score += 1
            st.session_state.next_q = True

        if st.session_state.next_q:
            st.session_state.current_q += 1
            st.session_state.next_q = False
            st.experimental_rerun()

    else:
        st.success(f"{user_name}, your final score is {st.session_state.score}/{len(st.session_state.shuffled_questions)}")
        new_entry = pd.DataFrame([[user_name, st.session_state.score]], columns=['Name', 'Score'])
        st.session_state.leaderboard = pd.concat([st.session_state.leaderboard, new_entry], ignore_index=True)
        st.session_state.leaderboard = st.session_state.leaderboard.sort_values(by='Score', ascending=False)

        if st.button("Play Again"):
            for key in ['shuffled_questions', 'current_q', 'answers', 'score', 'next_q']:
                if key in st.session_state:
                    del st.session_state[key]
            st.experimental_rerun()

    st.header("🏆 Leaderboard")
    st.dataframe(st.session_state.leaderboard.reset_index(drop=True))