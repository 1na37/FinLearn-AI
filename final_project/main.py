import streamlit as st
import time

# ==============================================================================
# 🌟 PYTHON NAVIGATION TRICK 🌟
# This function is necessary to redirect the user to a specific page
# in a Streamlit multi-page app structure without using the sidebar.
# It uses a Streamlit component (st.components.v1.html) to inject a tiny
# JavaScript snippet that changes the browser's URL path.
# ==============================================================================
def navigate_to(page_name):
    """
    Simulates navigation to a different page in a Streamlit multi-page app.
    The page_name must match the filename in your 'pages/' folder (e.g., 'finance_trivia').
    """
    # Create the expected URL path for the page file (e.g., /finance_trivia)
    path = f"/{page_name.lower().replace(' ', '_')}"
    
    # Use a hidden Streamlit HTML component to change the browser URL
    st.components.v1.html(
        f"""
        <script>
            window.parent.location.pathname = "{path}";
        </script>
        """,
        height=0, # Make the component invisible
        width=0
    )

    
# ==============================================================================
# 1. PAGE CONFIG & CUSTOM CSS
# ==============================================================================

st.set_page_config(
    page_title="Finance Learning Hub",
    page_icon="💰",
    layout="wide",
    # Set sidebar to collapsed initially since we're promoting column navigation
    initial_sidebar_state="collapsed" 
)

# Custom CSS
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
    /* Style to hide the default button look, making the card the focus */
    div.stButton > button {
        visibility: hidden; /* Hide the actual button */
        height: 100%; /* Force it to take up space */
        position: absolute; /* Allows overlay */
        top: 0;
        left: 0;
        width: 100%;
        cursor: pointer;
    }
    /* Style the container that holds the card and the invisible button */
    .clickable-card {
        position: relative; /* Needed for absolute positioning of the button */
        border-radius: 15px; 
        overflow: hidden; /* Keep button inside */
        margin-bottom: 2rem; /* Spacing between rows */
    }
</style>
""", unsafe_allow_html=True)


# ==============================================================================
# 2. HEADER & INTRO
# ==============================================================================

st.markdown('<h1 class="main-header">💰 Finance Learning Hub</h1>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <h2>Welcome to Your Financial Education Platform! 🚀</h2>
    <p style="font-size: 1.2rem; color: #666;">
        Choose from our interactive learning tools below:
    </p>
</div>
""", unsafe_allow_html=True)


# ==============================================================================
# 3. CLICKABLE FEATURE CARDS 
# ==============================================================================

# Note: The navigation function (navigate_to) is called when the invisible button is clicked.
# We use a button with use_container_width=True to cover the column area
#if st.button("Go to Trivia", key="go_trivia", use_container_width=True):
# 🚨 IMPORTANT: 'finance_trivia' must match the filename in your pages/ folder (e.g., pages/finance_trivia.py)
#navigate_to("finance_trivia") 
#st.markdown('</div>', unsafe_allow_html=True) # Close the clickable-card container
    
# Create four columns for the cards
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


# ==============================================================================
# 4. NAVIGATION INFO & FOOTER (Optional/Can be removed)
# ==============================================================================

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
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p>Built with Streamlit | Multipage App</p>
</div>
""", unsafe_allow_html=True)
