import streamlit as st
from recommender import recommend

# Page configuration
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    
    .stTitle {
        font-size: 3rem !important;
        background: linear-gradient(120deg, #e74c3c, #8e44ad);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem 0;
    }
    
    .subtitle {
        text-align: center;
        color: #7f8c8d;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .movie-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
        color: white;
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    .movie-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    .search-container {
        max-width: 600px;
        margin: 0 auto 3rem auto;
    }
    
    div[data-testid="stTextInput"] > label {
        font-size: 1.2rem;
        font-weight: 600;
        color: #2c3e50;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(120deg, #e74c3c, #8e44ad);
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.75rem 2rem;
        border: none;
        border-radius: 10px;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    .results-header {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        color: #2c3e50;
        margin: 2rem 0 1.5rem 0;
    }
    
    .input-movie {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.1rem;
        color: #2c3e50;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='stTitle'>🎬 Movie Recommender</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Discover your next favorite movie based on what you love</p>", unsafe_allow_html=True)

# Search section
with st.container():
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown("<div class='search-container'>", unsafe_allow_html=True)
        movie_name = st.text_input(
            "Enter a movie you like",
            placeholder="e.g., The Dark Knight, Inception, Titanic...",
            label_visibility="visible"
        )
        
        recommend_button = st.button("🔍 Find Similar Movies", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Results section
if recommend_button:
    if movie_name.strip() == "":
        st.warning("⚠️ Please enter a movie name to get recommendations.")
    else:
        with st.spinner("🎯 Finding the best recommendations for you..."):
            results = recommend(movie_name)
            
        if results is None:
            st.error("😕 Movie not found in our database. Please try another movie title.")
        else:
            # Display input movie
            st.markdown(f"<div class='input-movie'>🎥 Based on: <strong>{movie_name}</strong></div>", unsafe_allow_html=True)
            
            # Display results header
            st.markdown("<h2 class='results-header'>✨ Recommended Movies for You</h2>", unsafe_allow_html=True)
            
            # Display recommendations in columns
            cols = st.columns(2)
            
            for idx, movie in enumerate(results):
                with cols[idx % 2]:
                    st.markdown(f"""
                        <div class='movie-card'>
                            🎬 {movie}
                        </div>
                    """, unsafe_allow_html=True)
            
            # Add some spacing
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Footer message
            st.info("💡 Tip: Try different movie titles to explore more recommendations!")
