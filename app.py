import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NLP Summarization Comparison",
    page_icon="📝",
    layout="wide"
)

# ---------------------------------------------------------
# ORIGINAL TEXTS
# ---------------------------------------------------------

texts = {
    "News Article": """
A powerful storm hit several parts of the country yesterday, causing heavy rain, strong winds, and transport delays.
Local authorities advised residents to stay indoors and avoid unnecessary travel.
Several schools were closed, and emergency teams worked throughout the night.
Weather experts warned that some areas may still experience flooding.
""",

    "Product Review": """
I bought this wireless headphone two weeks ago, and overall I am happy with it.
The sound quality is clear, and the battery lasts for a long time.
However, the microphone quality is not very good during phone calls.
The price is reasonable, but I think the company should improve the microphone.
""",

    "Academic Abstract": """
This study investigates the use of transformer-based models for automatic text summarization.
The research compares different sequence-to-sequence architectures using evaluation metrics such as ROUGE.
The results show that transformer models can generate fluent and informative summaries.
"""
}

# ---------------------------------------------------------
# GENERATED SUMMARIES
# ---------------------------------------------------------

results = {
    "News Article": {
        "DistilBART / BART": {
            "summary": "Storm hit several parts of the country yesterday, causing heavy rain, strong winds and transport delays.",
            "comment": "Most accurate and detailed summary."
        },

        "T5": {
            "summary": "A powerful storm hit several parts of the country yesterday, causing heavy rain, strong winds, and transport delays.",
            "comment": "Short and clear summary."
        },

        "Pegasus": {
            "summary": "Flooding has affected thousands of people in southern China's Guangdong province.",
            "comment": "Added incorrect information."
        },

        "FLAN-T5": {
            "summary": "Heavy rain and strong winds have hit parts of the country.",
            "comment": "General summary but less accurate."
        }
    },

    "Product Review": {
        "DistilBART / BART": {
            "summary": "The sound quality is clear and the battery lasts for a long time.",
            "comment": "Kept both positive and negative points."
        },

        "T5": {
            "summary": "The wireless headphone is comfortable to wear for several hours.",
            "comment": "Missed some important details."
        },

        "Pegasus": {
            "summary": "This is a wireless headphone with a built-in microphone.",
            "comment": "Too general."
        },

        "FLAN-T5": {
            "summary": "Five Stars for a great wireless headphone.",
            "comment": "Added opinions not found in original text."
        }
    },

    "Academic Abstract": {
        "DistilBART / BART": {
            "summary": "This study investigates transformer-based models for automatic text summarization.",
            "comment": "Most faithful to the original text."
        },

        "T5": {
            "summary": "The study compares sequence-to-sequence architectures using evaluation metrics.",
            "comment": "Clear and short."
        },

        "Pegasus": {
            "summary": "Text summarization is a major problem in computer science.",
            "comment": "Very general summary."
        },

        "FLAN-T5": {
            "summary": "Automated text summarization is a useful tool.",
            "comment": "Understandable but repetitive."
        }
    }
}

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("📝 NLP Summarization Model Comparison")

st.markdown("""
This project compares multiple NLP summarization models on different text types.

### Models Compared
- DistilBART / BART
- T5
- Pegasus
- FLAN-T5

### Evaluation Goal
Compare how each model summarizes the same text and analyze:
- Accuracy
- Information kept
- Fluency
- Weaknesses
""")

st.divider()

# ---------------------------------------------------------
# TEXT SELECTION
# ---------------------------------------------------------

selected_text = st.selectbox(
    "Choose Text Type",
    list(texts.keys())
)

# ---------------------------------------------------------
# ORIGINAL TEXT
# ---------------------------------------------------------

st.subheader("📄 Original Text")

st.info(texts[selected_text])

st.divider()

# ---------------------------------------------------------
# MODEL RESULTS
# ---------------------------------------------------------

st.subheader("🤖 Generated Summaries")

models = results[selected_text]

col1, col2 = st.columns(2)

model_names = list(models.keys())

for i, model_name in enumerate(model_names):

    model_data = models[model_name]

    with (col1 if i % 2 == 0 else col2):

        with st.container(border=True):

            st.markdown(f"### {model_name}")

            st.markdown("#### Generated Summary")
            st.write(model_data["summary"])

            st.markdown("#### Analysis")
            st.success(model_data["comment"])

# ---------------------------------------------------------
# FINAL COMPARISON TABLE
# ---------------------------------------------------------

st.divider()

st.subheader("📊 Final Comparison")

comparison_df = pd.DataFrame({
    "Model": ["DistilBART / BART", "T5", "Pegasus", "FLAN-T5"],
    "Strength": [
        "Most accurate",
        "Short and clear",
        "Fluent writing",
        "Understandable summaries"
    ],
    "Weakness": [
        "Sometimes too extractive",
        "Misses details",
        "Hallucinated information",
        "Repetitive / inaccurate"
    ]
})

st.dataframe(
    comparison_df,
    use_container_width=True
)

# ---------------------------------------------------------
# FINAL CONCLUSION
# ---------------------------------------------------------

st.divider()

st.subheader("✅ Final Conclusion")

st.success("""
DistilBART / BART performed best overall because it produced the most accurate summaries and preserved the important information.

T5 produced short and readable summaries but sometimes removed details.

Pegasus generated fluent summaries but added incorrect information.

FLAN-T5 produced understandable summaries but sometimes repeated phrases or changed the meaning.
""")