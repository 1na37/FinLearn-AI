import streamlit as st

# Page configuration - ONLY in main app
st.set_page_config(
    page_title="Finance Learning Hub",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
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
</style>
""", unsafe_allow_html=True)

# Main homepage content
st.markdown('<h1 class="main-header">💰 Finance Learning Hub</h1>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <h2>Welcome to Your Financial Education Platform! 🚀</h2>
    <p style="font-size: 1.2rem; color: #666;">
        Choose from our interactive learning tools below:
    </p>
</div>
""", unsafe_allow_html=True)

# Feature cards
col1, col2, col3, col4 = st.columns(3)

with col1:
    st.markdown("""
    <div style="padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                border-radius: 15px; color: white; text-align: center;">
        <h3>🎯 Finance Trivia</h3>
        <p>Test your financial knowledge with interactive quizzes</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="padding: 2rem; background: linear-gradient(135deg, #28a745 0%, #20c997 100%); 
                border-radius: 15px; color: white; text-align: center;">
        <h3>📊 Finance AI</h3>
        <p>Ask your questions here</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="padding: 2rem; background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%); 
                border-radius: 15px; color: white; text-align: center;">
        <h3>📚 Resources</h3>
        <p>Explore financial learning materials</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="padding: 2rem; background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%); 
                border-radius: 15px; color: white; text-align: center;">
        <h3>🧮 Financial Calculators</h3>
        <p>Use tools for financial calculations</p>
    </div>
    """, unsafe_allow_html=True)

# Navigation instructions
st.markdown("---")
st.markdown("""
### 🧭 How to Navigate
Use the sidebar on the left to switch between different sections of the app:
- **Finance Trivia** - Interactive quiz game
- **Multi Finance AI** - Interactive AI chatbot for finance questions
- **Resources** - Financial learning materials 2025
- **Financial calculators** - Tools for financial calculations [stock analysis, investment, currency converter, mortgage calculator]""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p>Built with Streamlit | Multipage App Example</p>
</div>
""", unsafe_allow_html=True)