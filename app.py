import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Summarization Model Comparison",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Summarization Model Comparison")

st.markdown("""
This app compares different NLP summarization models on three text types.

### Models
- DistilBART / BART
- T5
- Pegasus
- FLAN-T5

### Text Types
- News Article
- Product Review
- Academic Abstract
""")

# ---------------------------------------------------
# Data
# ---------------------------------------------------

data = [
    {
        "Model": "DistilBART / BART",
        "Text Type": "News Article",
        "Summary": "Storm hit several parts of the country yesterday, causing heavy rain, strong winds and transport delays.",
        "Comment": "Most accurate and detailed summary."
    },

    {
        "Model": "T5",
        "Text Type": "News Article",
        "Summary": "A powerful storm hit several parts of the country yesterday, causing heavy rain, strong winds, and transport delays.",
        "Comment": "Short and clear summary."
    },

    {
        "Model": "Pegasus",
        "Text Type": "News Article",
        "Summary": "Flooding has affected thousands of people in southern China's Guangdong province.",
        "Comment": "Added incorrect information."
    },

    {
        "Model": "FLAN-T5",
        "Text Type": "News Article",
        "Summary": "Heavy rain and strong winds have hit parts of the country.",
        "Comment": "General summary but less accurate."
    },

    {
        "Model": "DistilBART / BART",
        "Text Type": "Product Review",
        "Summary": "The sound quality is clear and the battery lasts for a long time.",
        "Comment": "Kept both positive and negative points."
    },

    {
        "Model": "T5",
        "Text Type": "Product Review",
        "Summary": "The wireless headphone is comfortable to wear for several hours.",
        "Comment": "Missed some important details."
    },

    {
        "Model": "Pegasus",
        "Text Type": "Product Review",
        "Summary": "This is a wireless headphone with a built-in microphone.",
        "Comment": "Too general."
    },

    {
        "Model": "FLAN-T5",
        "Text Type": "Product Review",
        "Summary": "Five Stars for a great wireless headphone.",
        "Comment": "Added opinions not found in original text."
    },

    {
        "Model": "DistilBART / BART",
        "Text Type": "Academic Abstract",
        "Summary": "This study investigates transformer-based models for automatic text summarization.",
        "Comment": "Most faithful to the original text."
    },

    {
        "Model": "T5",
        "Text Type": "Academic Abstract",
        "Summary": "The study compares sequence-to-sequence architectures using evaluation metrics.",
        "Comment": "Clear and short."
    },

    {
        "Model": "Pegasus",
        "Text Type": "Academic Abstract",
        "Summary": "Text summarization is a major problem in computer science.",
        "Comment": "Very general summary."
    },

    {
        "Model": "FLAN-T5",
        "Text Type": "Academic Abstract",
        "Summary": "Automated text summarization is a useful tool.",
        "Comment": "Understandable but repetitive."
    },
]

df = pd.DataFrame(data)

# ---------------------------------------------------
# Filters
# ---------------------------------------------------

selected_text = st.selectbox(
    "Choose Text Type",
    df["Text Type"].unique()
)

filtered_df = df[df["Text Type"] == selected_text]

# ---------------------------------------------------
# Display
# ---------------------------------------------------

st.subheader(f"Results for: {selected_text}")

for _, row in filtered_df.iterrows():

    with st.container(border=True):

        st.markdown(f"## {row['Model']}")

        st.markdown("### Generated Summary")
        st.write(row["Summary"])

        st.markdown("### Comment")
        st.info(row["Comment"])

# ---------------------------------------------------
# Final Conclusion
# ---------------------------------------------------

st.markdown("---")

st.header("Final Conclusion")

st.success("""
DistilBART / BART performed best overall because it produced the most accurate summaries and kept the important information.

T5 produced short and clear summaries but sometimes removed details.

Pegasus struggled because it added incorrect information.

FLAN-T5 was understandable but sometimes repetitive or inaccurate.
""")