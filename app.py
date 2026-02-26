import anthropic
import os
import streamlit as st

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def get_playlist(mood):
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are a music expert and mood analyst. 
                Based on this mood: '{mood}'
                
                Please suggest a playlist with:
                1. 5 song recommendations with artist names
                2. The genre that fits this mood
                3. A short explanation of why this playlist fits the mood
                
                Format it nicely and clearly."""
            }
        ]
    )
    return message.content[0].text

st.set_page_config(page_title="AI Mood Playlist Curator", page_icon="🎵")

st.markdown("""
    <style>
    .main { background-color: #0e0e0e; }
    .stTextInput input { border-radius: 20px; }
    .stButton button { 
        border-radius: 20px; 
        background-color: #9b59b6;
        color: white;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎵 AI Mood Playlist Curator")
st.subheader("Powered by Claude AI")

mood = st.text_input("How are you feeling right now?", 
                      placeholder="e.g. happy and energetic, sad and calm...")

if st.button("Generate My Playlist ✨"):
    if mood:
        with st.spinner("Generating your perfect playlist..."):
            playlist = get_playlist(mood)
            st.success("Here is your playlist!")
            st.markdown(playlist)
    else:
        st.warning("Please enter your mood first!")
