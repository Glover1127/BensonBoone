import streamlit as st
import random
import pandas as pd

# Trivia data structure with 17 additional questions (total 54)
questions = [
    {"question": "Which show did Benson Boone audition for?", "options": ["America's Got Talent", "American Idol", "The Voice"], "answer": "American Idol", "difficulty": "Easy"},
    {"question": "Which platform made Benson Boone famous first?", "options": ["YouTube", "Instagram", "TikTok"], "answer": "TikTok", "difficulty": "Easy"},
    {"question": "What was Benson Boone's first major hit song?", "options": ["Sugar Sweet", "Ghost Town", "Beautiful Things"], "answer": "Ghost Town", "difficulty": "Easy"},
    {"question": "Benson Boone primarily plays what instrument?", "options": ["Violin", "Piano", "Drums"], "answer": "Piano", "difficulty": "Medium"},
    {"question": "In what month was Benson Boone born?", "options": ["June", "October", "December"], "answer": "June", "difficulty": "Medium"},
    {"question": "Which U.S. state is Benson Boone originally from?", "options": ["California", "Washington", "Texas"], "answer": "Washington", "difficulty": "Medium"},
    {"question": "Which major record label signed Benson Boone first?", "options": ["Warner Records", "Sony Music", "Capitol Records"], "answer": "Warner Records", "difficulty": "Hard"},
    {"question": "What year was Benson Boone born?", "options": ["2000", "2002", "2004"], "answer": "2002", "difficulty": "Easy"},
    {"question": "What was the title of Benson Boone’s debut album?", "options": ["Fireworks & Rollerblades", "Walk Me Home", "Pulse"], "answer": "Fireworks & Rollerblades", "difficulty": "Easy"},
    {"question": "Which song by Benson Boone topped charts in multiple countries in 2024?", "options": ["In the Stars", "Beautiful Things", "Slow It Down"], "answer": "Beautiful Things", "difficulty": "Easy"},
    {"question": "What sport did Benson Boone compete in during high school?", "options": ["Diving", "Basketball", "Football"], "answer": "Diving", "difficulty": "Medium"},
    {"question": "Which Imagine Dragons member signed Benson Boone to his label?", "options": ["Dan Reynolds", "Wayne Sermon", "Ben McKee"], "answer": "Dan Reynolds", "difficulty": "Medium"},
    {"question": "What was Benson Boone’s second single released in 2022?", "options": ["Room for 2", "Before You", "In the Stars"], "answer": "Room for 2", "difficulty": "Medium"},
    {"question": "Which city did Benson Boone perform in for Taylor Swift’s Eras Tour?", "options": ["London", "New York", "Los Angeles"], "answer": "London", "difficulty": "Medium"},
    {"question": "What is the name of Benson Boone’s first EP?", "options": ["Pulse", "Walk Me Home", "Fireworks"], "answer": "Walk Me Home", "difficulty": "Medium"},
    {"question": "Which instrument did Benson Boone NOT play on 'Ghost Town'?", "options": ["Guitar", "Drums", "Violin"], "answer": "Violin", "difficulty": "Hard"},
    {"question": "What inspired Benson Boone to take singing seriously?", "options": ["A Jon Bellion concert", "A school talent show", "American Idol"], "answer": "A Jon Bellion concert", "difficulty": "Hard"},
    {"question": "How many sisters does Benson Boone have?", "options": ["2", "3", "4"], "answer": "4", "difficulty": "Hard"},
    {"question": "Which song did Benson Boone release in April 2022?", "options": ["In the Stars", "Sugar Sweet", "Beautiful Things"], "answer": "In the Stars", "difficulty": "Medium"},
    {"question": "What is Benson Boone’s middle name?", "options": ["James", "Michael", "Thomas"], "answer": "James", "difficulty": "Hard"},
    {"question": "Which university did Benson Boone briefly attend?", "options": ["Brigham Young University–Idaho", "University of Washington", "UCLA"], "answer": "Brigham Young University–Idaho", "difficulty": "Hard"},
    {"question": "What activity does Benson Boone enjoy outside of music?", "options": ["Rollerblading", "Painting", "Cooking"], "answer": "Rollerblading", "difficulty": "Medium"},
    {"question": "Which TV show did Benson Boone perform 'Ghost Town' on?", "options": ["The Ellen DeGeneres Show", "Jimmy Kimmel Live", "The Tonight Show"], "answer": "The Ellen DeGeneres Show", "difficulty": "Medium"},
    {"question": "What was the name of Benson Boone’s high school?", "options": ["Monroe High School", "Skyline High School", "Lincoln High School"], "answer": "Monroe High School", "difficulty": "Hard"},
    {"question": "Which song from 'Fireworks & Rollerblades' features a piano intro?", "options": ["Slow It Down", "Cry", "Beautiful Things"], "answer": "Slow It Down", "difficulty": "Hard"},
    {"question": "In which year did Benson Boone release 'Ghost Town'?", "options": ["2020", "2021", "2022"], "answer": "2021", "difficulty": "Easy"},
    {"question": "What is the name of Benson Boone’s record label under Warner Records?", "options": ["Night Street Records", "Daylight Records", "Starlight Records"], "answer": "Night Street Records", "difficulty": "Medium"},
    {"question": "Which artist did Benson Boone open for in 2024?", "options": ["Taylor Swift", "Ed Sheeran", "Billie Eilish"], "answer": "Taylor Swift", "difficulty": "Easy"},
    {"question": "What was Benson Boone’s TikTok follower count before 'Ghost Town'?", "options": ["1.7 million", "2.5 million", "3 million"], "answer": "1.7 million", "difficulty": "Hard"},
    {"question": "Which song did Benson Boone release in May 2023?", "options": ["What Was", "Coffee Cake", "Little Runaway"], "answer": "What Was", "difficulty": "Medium"},
    {"question": "What is the title of Benson Boone’s 2023 EP?", "options": ["Pulse", "Walk Me Home", "Fireworks"], "answer": "Pulse", "difficulty": "Medium"},
    {"question": "Which country did 'Beautiful Things' top the charts in?", "options": ["United Kingdom", "Japan", "Brazil"], "answer": "United Kingdom", "difficulty": "Easy"},
    {"question": "What was Benson Boone’s age when he auditioned for American Idol?", "options": ["17", "18", "19"], "answer": "18", "difficulty": "Hard"},
    # New Questions Start Here (17 more)
    {"question": "What day in June was Benson Boone born?", "options": ["15", "25", "30"], "answer": "25", "difficulty": "Hard"},
    {"question": "Which song did Benson Boone perform on 'American Idol'?", "options": ["Punchline", "Simple", "Ghost Town"], "answer": "Punchline", "difficulty": "Medium"},
    {"question": "What is the name of Benson Boone’s hometown?", "options": ["Monroe", "Seattle", "Spokane"], "answer": "Monroe", "difficulty": "Medium"},
    {"question": "Which 'Fireworks & Rollerblades' track has a music video with a desert setting?", "options": ["Forever and a Day", "Beautiful Things", "Cry"], "answer": "Beautiful Things", "difficulty": "Medium"},
    {"question": "What color is prominently featured in Benson Boone’s 'Ghost Town' music video?", "options": ["Red", "Blue", "Green"], "answer": "Blue", "difficulty": "Hard"},
    {"question": "Which artist co-wrote 'In the Stars' with Benson Boone?", "options": ["Jason Evigan", "Dan Reynolds", "Jon Bellion"], "answer": "Jason Evigan", "difficulty": "Hard"},
    {"question": "What was Benson Boone’s first single of 2023?", "options": ["Sugar Sweet", "Before You", "Little Runaway"], "answer": "Sugar Sweet", "difficulty": "Medium"},
    {"question": "Which award nomination did Benson Boone receive in 2024?", "options": ["MTV Video Music Award", "Grammy Award", "Billboard Music Award"], "answer": "MTV Video Music Award", "difficulty": "Easy"},
    {"question": "What is the runtime of 'Beautiful Things'?", "options": ["2:52", "3:00", "3:15"], "answer": "3:00", "difficulty": "Hard"},
    {"question": "Which song did Benson Boone release as a piano version?", "options": ["Ghost Town", "In the Stars", "Slow It Down"], "answer": "In the Stars", "difficulty": "Medium"},
    {"question": "What is the name of Benson Boone’s childhood pet?", "options": ["Max", "Buddy", "Unknown"], "answer": "Unknown", "difficulty": "Hard"},
    {"question": "Which European country did Benson Boone first tour in?", "options": ["Germany", "France", "United Kingdom"], "answer": "United Kingdom", "difficulty": "Easy"},
    {"question": "What was the release month of 'Fireworks & Rollerblades'?", "options": ["April", "June", "August"], "answer": "April", "difficulty": "Easy"},
    {"question": "Which 'Pulse' track is the shortest?", "options": ["Coffee Cake", "Little Runaway", "Sugar Sweet"], "answer": "Coffee Cake", "difficulty": "Hard"},
    {"question": "What hairstyle is Benson Boone known for?", "options": ["Curly mullet", "Buzz cut", "Long ponytail"], "answer": "Curly mullet", "difficulty": "Easy"},
    {"question": "Which song did Benson Boone dedicate to his family?", "options": ["In the Stars", "Ghost Town", "Before You"], "answer": "In the Stars", "difficulty": "Medium"},
    {"question": "How many tracks are on 'Fireworks & Rollerblades'?", "options": ["12", "15", "18"], "answer": "15", "difficulty": "Medium"}
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
            st.rerun()

    else:
        st.success(f"{user_name}, your final score is {st.session_state.score}/{len(st.session_state.shuffled_questions)}")
        new_entry = pd.DataFrame([[user_name, st.session_state.score]], columns=['Name', 'Score'])
        st.session_state.leaderboard = pd.concat([st.session_state.leaderboard, new_entry], ignore_index=True)
        st.session_state.leaderboard = st.session_state.leaderboard.sort_values(by='Score', ascending=False)

        if st.button("Play Again"):
            for key in ['shuffled_questions', 'current_q', 'answers', 'score', 'next_q']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    st.header("🏆 Leaderboard")
    st.dataframe(st.session_state.leaderboard.reset_index(drop=True))