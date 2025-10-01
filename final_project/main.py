import streamlit as st
import time

# Function to simulate multi-page navigation using JavaScript injection
def navigate_to(page_name):
    path = f"/{page_name.lower().replace(' ', '_')}"
    st.components.v1.html(
        f"""
        <script>
            window.parent.location.pathname = "{path}";
        </script>
        """,
        height=0,
        width=0
    )

# --- PAGE CONFIG & CUSTOM CSS ---

st.set_page_config(
    page_title="Finance Learning Hub",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed" 
)

# Custom CSS for header and clickable cards
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    /* Hide default button look to make the card clickable */
    div.stButton > button {
        visibility: hidden; 
        height: 100%; 
        position: absolute; 
        top: 0;
        left: 0;
        width: 100%;
        cursor: pointer;
    }
    .clickable-card {
        position: relative; 
        border-radius: 15px; 
        overflow: hidden; 
        margin-bottom: 2rem; 
    }
</style>
""", unsafe_allow_html=True)


# --- HEADER & INTRO ---

st.markdown('<h1 class="main-header">💰 Finance Learning Hub</h1>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <h2>Welcome to Your Financial Education Platform! 🚀</h2>
    <p style="font-size: 1.2rem; color: #666;">
        Choose from our interactive learning tools below:
    </p>
</div>
""", unsafe_allow_html=True)


# --- CLICKABLE FEATURE CARDS ---

col1, col2, col3, col4 = st.columns(4)

# Card 1: Finance Trivia
with col1:
    st.markdown('<div class="clickable-card">', unsafe_allow_html=True)
    st.markdown("""
    <div style="padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);  
                 border-radius: 15px; color: white; text-align: center; height: 100%;">
        <h3>🎯 Finance Trivia</h3>
        <p>Test your financial knowledge with interactive quizzes</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Trivia", key="go_trivia", use_container_width=True):
        navigate_to("finance_trivia") # Maps to pages/finance_trivia.py
    st.markdown('</div>', unsafe_allow_html=True)

# Card 2: Finance AI
with col2:
    st.markdown('<div class="clickable-card">', unsafe_allow_html=True)
    st.markdown("""
    <div style="padding: 2rem; background: linear-gradient(135deg, #28a745 0%, #20c997 100%);  
                 border-radius: 15px; color: white; text-align: center; height: 100%;">
        <h3>📊 Finance AI</h3>
        <p>Ask your questions here</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to AI Chat", key="go_ai", use_container_width=True):
        navigate_to("finance_ai") # Maps to pages/finance_ai.py
    st.markdown('</div>', unsafe_allow_html=True)

# Card 3: Resources
with col3:
    st.markdown('<div class="clickable-card">', unsafe_allow_html=True)
    st.markdown("""
    <div style="padding: 2rem; background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);  
                 border-radius: 15px; color: white; text-align: center; height: 100%;">
        <h3>📚 Resources</h3>
        <p>Explore financial learning materials</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Resources", key="go_resources", use_container_width=True):
        navigate_to("learning_materials") # Maps to pages/learning_materials.py
    st.markdown('</div>', unsafe_allow_html=True)

# Card 4: Financial Calculators (Deep Teal)
with col4:
    st.markdown('<div class="clickable-card">', unsafe_allow_html=True)
    st.markdown("""
    <div style="padding: 2rem; background: linear-gradient(135deg, #0081A7 0%, #00B1CC 100%); 
                border-radius: 15px; color: white; text-align: center; height: 100%;">
        <h3>🧮 Financial Calculators</h3>
        <p>Use tools for financial calculations</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Calculators", key="go_calc", use_container_width=True):
        navigate_to("financial_calculators") # Maps to pages/financial_calculators.py
    st.markdown('</div>', unsafe_allow_html=True)


# --- NAVIGATION INFO & FOOTER ---

st.markdown("---")
st.markdown("""
### 🧭 How to Navigate
The **cards above** will take you directly to the sections. You can also use the sidebar:
- **Finance Trivia** - Interactive quiz game
- **Multi Finance AI** - Interactive AI chatbot for finance questions
- **Resources** - Financial learning materials 2025
- **Financial calculators** - Tools for financial calculations [stock analysis, investment, currency converter, mortgage calculator]
""")

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p>Built with Streamlit | Multipage App</p>
</div>
""", unsafe_allow_html=True)
