import streamlit as st
from transformers import pipeline

# Set page title and header
st.set_page_config(page_title="Sentiment Analysis App", page_icon="🤖")
st.title("🤖 Sentiment Analysis with Hugging Face")

st.markdown("""
This app uses a pre-trained machine learning model from Hugging Face Transformers to analyze the sentiment of your text.
""")

# Load the pipeline (cached to avoid reloading on every interaction)
@st.cache_resource
def load_sentiment_pipeline():
    return pipeline("sentiment-analysis")

classifier = load_sentiment_pipeline()

# User input
text_input = st.text_area("Enter some text here:", height=150, placeholder="I love building cool AI apps!")

if st.button("Analyze Sentiment"):
    if text_input.strip():
        with st.spinner("Analyzing..."):
            result = classifier(text_input)[0]
            label = result['label']
            score = result['score']
            
            if label == 'POSITIVE':
                st.success(f"**Sentiment:** {label} 😊")
            else:
                st.error(f"**Sentiment:** {label} 😔")
            
            st.metric("Confidence Score", f"{score:.4f}")
    else:
        st.warning("Please enter some text to analyze.")
