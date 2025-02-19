import streamlit as st
import random
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(page_title="Personal Growth Dashboard", page_icon="🌱", layout="wide")

# Custom CSS with enhanced animations and styling
st.markdown("""
<style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideIn {
        from { transform: translateX(-100%); }
        to { transform: translateX(0); }
    }
    @keyframes scaleIn {
        from { transform: scale(0.95); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    .fade-in {
        animation: fadeIn 1.5s ease-in;
    }
    .slide-in {
        animation: slideIn 1s ease-out;
    }
    .scale-in {
        animation: scaleIn 0.5s ease-out;
    }
    .stButton>button {
        transition: all 0.3s ease;
        border-radius: 20px;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .quote-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        color: black;
        margin: 20px 0;
        animation: fadeIn 2s ease-in;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .skill-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .achievement-card {
        background-color: #f8f9fa;
        color:black;
        padding: 20px;
        border-radius: 15px;
        margin: 15px 0;
        border-left: 4px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session states
if "show_quote" not in st.session_state:
    st.session_state.show_quote = False
if "proceed" not in st.session_state:
    st.session_state.proceed = False
if "responses" not in st.session_state:
    st.session_state.responses = {}
if "skills" not in st.session_state:
    st.session_state.skills = []
if "achievements" not in st.session_state:
    st.session_state.achievements = []
if "learning_goals" not in st.session_state:
    st.session_state.learning_goals = []

def get_mindset_quote():
    quotes = [
        "The only limit to your growth is your mindset.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Your potential is unlimited. Your growth is in your control.",
        "The expert in anything was once a beginner.",
        "Growth and comfort do not coexist. Choose growth!"
    ]
    return random.choice(quotes)

# Header Section
st.markdown('<div class="fade-in">', unsafe_allow_html=True)
st.title("🌱 Personal Growth Dashboard")
st.markdown("</div>", unsafe_allow_html=True)

# Sidebar for Navigation
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Go to:", 
                    ["Profile", "Skills & Achievements", "Learning Analysis", "Growth Mindset Quiz"])

# Main Content
if page == "Profile":
    col1, col2 = st.columns([2,1])
    
    with col1:
        name = st.text_input("👋 What's your name?", "")
        if name:
            st.markdown(f'<div class="slide-in">', unsafe_allow_html=True)
            st.success(f"Welcome, {name}! Let's track your growth journey! 🚀")
            st.markdown('</div>', unsafe_allow_html=True)
            
            if not st.session_state.show_quote:
                time.sleep(0.5)
                st.session_state.show_quote = True
            
            if st.session_state.show_quote:
                st.markdown(f'<div class="quote-box">{get_mindset_quote()}</div>', 
                           unsafe_allow_html=True)

   

elif page == "Skills & Achievements":
    st.header("🎯 Skills & Achievements Tracker")
    
    # Skills Section
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Add New Skill")
        new_skill = st.text_input("Skill name")
        skill_level = st.slider("Proficiency Level", 1, 100, 50)
        if st.button("Add Skill"):
            if new_skill:
                st.session_state.skills.append({"name": new_skill, "level": skill_level})
                st.success(f"Added {new_skill} to your skills!")

    with col2:
        st.subheader("Your Skills")
        if st.session_state.skills:
            # Create radar chart
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=[skill["level"] for skill in st.session_state.skills],
                theta=[skill["name"] for skill in st.session_state.skills],
                fill='toself'
            ))
            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])))
            st.plotly_chart(fig)

    # Achievements Section
    st.subheader("🏆 Achievements")
    col3, col4 = st.columns(2)
    
    with col3:
        new_achievement = st.text_area("Add new achievement")
        achievement_date = st.date_input("Date achieved")
        if st.button("Add Achievement"):
            if new_achievement:
                st.session_state.achievements.append({
                    "achievement": new_achievement,
                    "date": achievement_date
                })
                st.success("Achievement recorded!")

    with col4:
        if st.session_state.achievements:
            for achievement in st.session_state.achievements:
                st.markdown(f"""
                <div class="achievement-card">
                    <h4>{achievement['date'].strftime('%B %d, %Y')}</h4>
                    <p>{achievement['achievement']}</p>
                </div>
                """, unsafe_allow_html=True)

elif page == "Learning Analysis":
    st.header("📊 Learning Analysis")
    
    # Learning Goals
    st.subheader("Learning Goals Tracker")
    col1, col2 = st.columns(2)
    
    with col1:
        new_goal = st.text_input("Add new learning goal")
        goal_deadline = st.date_input("Target completion date")
        if st.button("Add Goal"):
            if new_goal:
                st.session_state.learning_goals.append({
                    "goal": new_goal,
                    "deadline": goal_deadline,
                    "status": "In Progress"
                })
    
    with col2:
        if st.session_state.learning_goals:
            for idx, goal in enumerate(st.session_state.learning_goals):
                status = st.selectbox(
                    f"Status for: {goal['goal']}", 
                    ["In Progress", "Completed", "On Hold"],
                    key=f"goal_{idx}"
                )
                st.session_state.learning_goals[idx]["status"] = status

    # Progress Visualization
    if st.session_state.learning_goals:
        status_counts = pd.DataFrame([g["status"] for g in st.session_state.learning_goals]
                                   ).value_counts().reset_index()
        status_counts.columns = ["Status", "Count"]
        fig = px.pie(status_counts, values="Count", names="Status", 
                     title="Learning Goals Progress")
        st.plotly_chart(fig)

elif page == "Growth Mindset Quiz":
    st.header("📝 Growth Mindset Assessment")
    
    questions = [
        {
            "question": "How do you typically respond to challenges?",
            "options": [
                "I see them as opportunities to learn and grow",
                "I try to avoid them if possible",
                "I face them but prefer easier tasks"
            ]
        },
        {
            "question": "When you receive constructive criticism, you usually:",
            "options": [
                "Welcome it as a chance to improve",
                "Feel defensive but try to learn from it",
                "Take it personally"
            ]
        },
        {
            "question": "How do you view your intelligence and abilities?",
            "options": [
                "They can be developed through effort and learning",
                "They are mostly fixed but can improve slightly",
                "They are largely determined by natural talent"
            ]
        }
    ]
    
    responses = {}
    for idx, q in enumerate(questions):
        responses[idx] = st.radio(q["question"], q["options"], key=f"q_{idx}")
    
    if st.button("Analyze My Mindset"):
        score = sum([1 if resp.startswith("I see them") or 
                    resp.startswith("Welcome") or 
                    resp.startswith("They can be") else 0 
                    for resp in responses.values()])
        
        st.balloons()
        
        if score >= 2:
            message = "🌟 Strong Growth Mindset! Keep nurturing your development!"
        else:
            message = "💪 You're on your way! Focus on embracing challenges and learning opportunities."
            
        st.success(f"Your Growth Mindset Score: {score}/3\n{message}")

# Footer
st.write("---")
st.markdown("🌟 Built to empower continuous personal growth and development!")
