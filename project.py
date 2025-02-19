
import streamlit as st
import random
import time

# Page Configuration (MUST be the first Streamlit command)
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

# Custom css 
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
    .fade-in {
        animation: fadeIn 1.5s ease-in;
    }
    .slide-in {
        animation: slideIn 1s ease-out;
    }
    .stButton>button {
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
    }
    .quote-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        color:black;
        margin: 20px 0;
        animation: fadeIn 2s ease-in;
    }
</style>
""", unsafe_allow_html=True)

# Function to get a random Growth Mindset quote
def get_mindset_quote():
    quotes = [
        "Challenges make life interesting. Overcoming them makes life meaningful.",
        "Failure is an opportunity to begin again, this time more intelligently.",
        "Your mindset determines your growth. Stay positive, stay hungry!",
        "Every expert was once a beginner. Keep pushing forward!",
        "Hardships prepare ordinary people for extraordinary destinies."
    ]
    return random.choice(quotes)

# Initialize session states
if "show_quote" not in st.session_state:
    st.session_state.show_quote = False
if "proceed" not in st.session_state:
    st.session_state.proceed = False
if "responses" not in st.session_state:
    st.session_state.responses = {}

# Animated Welcome Section
st.markdown('<div class="fade-in">', unsafe_allow_html=True)
st.title("🌱 Growth Mindset Challenge")
st.markdown('</div>', unsafe_allow_html=True)

# User Name Input
name = st.text_input("👋 What's your name?", "")

if name:
    st.markdown('<div class="slide-in">', unsafe_allow_html=True)
    st.success(f"Welcome, {name}! Let's explore your Growth Mindset together! 🚀")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if not st.session_state.show_quote:
        time.sleep(0.5)
        st.session_state.show_quote = True
    
    if st.session_state.show_quote:
        st.markdown(f'<div class="quote-box">{get_mindset_quote()}</div>', unsafe_allow_html=True)

    # Asking about Education and Future Goals
    st.header("🎯 Your Educational Background & Future Plans")
    education = st.text_input("📚 What is your highest level of education?")
    future_plans = st.text_area("🚀 What are your future goals and aspirations?")
    
    if st.button("Submit"):
        if not education.strip() or not future_plans.strip():
            st.warning("⚠️ Please fill in both your education level and future plans before proceeding.")
        else:
            with st.spinner("Processing your information..."):
                time.sleep(1)
                st.success(f"✅ Your education level: {education}")
                st.success(f"✅ Your future plans: {future_plans}")
                st.session_state.proceed = True

# Show Quiz Only If User Has Submitted Details
if st.session_state.proceed:
    # Growth Mindset Key Points
    st.header("Why Should You Adopt a Growth Mindset?")
    col1, col2 = st.columns(2)
    with col1:
        for point in [
            "**Embrace Challenges:** Learn from every obstacle.",
            "**Learn from Mistakes:** Failures are stepping stones to success.",
            "**Persist Through Difficulties:** Consistency is key."
        ]:
            st.markdown(f"✅ {point}")
    
    with col2:
        for point in [
            "**Celebrate Effort:** Focus on progress, not just results.",
            "**Stay Curious:** Keep exploring new possibilities."
        ]:
            st.markdown(f"✅ {point}")

    # Interactive Self-Assessment Quiz
    st.header("📝 Growth Mindset Self-Check")
    st.write("Answer these questions to see how strong your growth mindset is!")

    questions = [
        "Do you see challenges as opportunities to grow?",
        "Do you believe that intelligence can be developed?",
        "Are you open to learning from criticism?",
        "Do you put in effort even when things are difficult?",
        "Do you feel motivated to improve your skills every day?"
    ]

    score = 0
    for q in questions:
        response = st.radio(q, ("Yes", "No"), key=q, index=None)
        st.session_state.responses[q] = response
        if response == "Yes":
            score += 1

    if st.button("Check My Mindset Score"):
        with st.spinner("Calculating your mindset score..."):
            time.sleep(1)
            st.balloons()
            st.success(f"🎯 Your Growth Mindset Score: {score}/5")

            if score >= 4:
                st.markdown("🚀 **Amazing! You have a strong growth mindset. Keep it up!**")
            elif score >= 2:
                st.markdown("🔄 **You're on the right track! Keep working on developing your mindset.**")
            else:
                st.markdown("💡 **Time to focus on personal growth. Believe in yourself!**")

# Footer
st.write("---")
st.write("🌟 Developed with 💙 to inspire a Growth Mindset!")
