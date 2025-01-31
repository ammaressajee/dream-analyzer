import streamlit as st
from transformers import pipeline
import random

# Load NLP model for text generation
dream_analyzer = pipeline("text-generation", model="gpt2")

# App title and description
st.title("🌙 AI Dream Interpreter 🔮")
st.write("Describe your dream, and our AI will analyze its meaning based on psychology and mythology!")

# User input
dream = st.text_area("Describe your dream in detail:")

if st.button("Interpret My Dream"):
    if dream:
        # Generate AI-based dream interpretation
        response = dream_analyzer(dream, max_length=100, do_sample=True, temperature=0.7)
        interpretation = response[0]['generated_text']

        # Randomized symbolic meanings
        symbols = ["🐍 Snakes: Hidden Homosexuality", "💧 Water: Loose Poops ", "🔥 Fire: Spicy Bumhole",
                   "🕊️ Birds: Freedom", "🌕 Moon: AKA butt crack", "🌀 Tornado: Chaos/Change"]
        random_symbol = random.choice(symbols)

        # Display results
        st.subheader("🌌 Your Dream Interpretation:")
        st.write(interpretation)

        st.subheader("✨ Your Dream's Key Symbol Analysis:")
        st.write(random_symbol)
    else:
        st.warning("Please enter a dream description first!")

# Fun footer
st.write("---")
st.write("🚀 Created for the **princess** - Betsy 🎉")
