import streamlit as st
import pandas as pd

st.set_page_config(
    page_title=" Summarization Model Comparison",
    page_icon="📝",
    layout="wide"
)

# ---------------------------------------------------
# Data from the experiment
# ---------------------------------------------------

results_data = [
    {
        "Model": "DistilBART / BART",
        "Text Type": "News Article",
        "Generated Summary": "Storm hit several parts of the country yesterday, causing heavy rain, strong winds and transport delays. Local authorities advised residents to stay indoors and avoid unnecessary travel. Weather experts said the storm is expected to weaken by tomorrow, but warned that some areas may still experience flooding.",
        "Accuracy": 5,
        "Info Kept": 5,
        "Fluency": 5,
        "Error Level": 1,
        "Comment": "Very faithful summary. It kept the main facts from the news article."
    },
    {
        "Model": "DistilBART / BART",
        "Text Type": "Product Review",
        "Generated Summary": "The sound quality is clear, and the battery lasts for a long time. The microphone quality is not very good during phone calls, especially in noisy places. The price is reasonable, but the company should improve the microphone.",
        "Accuracy": 5,
        "Info Kept": 5,
        "Fluency": 5,
        "Error Level": 1,
        "Comment": "Strong result. It kept both positive and negative opinions."
    },
    {
        "Model": "DistilBART / BART",
        "Text Type": "Academic Abstract",
        "Generated Summary": "This study investigates the use of transformer-based models for automatic text summarization. The research compares different sequence-to-sequence architectures using evaluation metrics such as ROUGE-1. The study highlights the importance of combining automatic metrics with human evaluation.",
        "Accuracy": 4,
        "Info Kept": 4,
        "Fluency": 5,
        "Error Level": 1,
        "Comment": "Accurate but slightly long and close to the original text."
    },
    {
        "Model": "DistilBART / BART",
        "Text Type": "Movie Plot Summary",
        "Generated Summary": "A young engineer discovers that the company he works for is secretly building a dangerous artificial intelligence system. He later realizes that the system is being used to control personal data and make unfair decisions.",
        "Accuracy": 5,
        "Info Kept": 4,
        "Fluency": 5,
        "Error Level": 1,
        "Comment": "Clear and accurate summary of the main plot."
    },
    {
        "Model": "DistilBART / BART",
        "Text Type": "Blog Paragraph",
        "Generated Summary": "Over the past year, I have tried to improve my daily routine by waking up earlier and planning my tasks. After a few weeks, I noticed that I had more energy, completed my work faster, and felt less stressed.",
        "Accuracy": 5,
        "Info Kept": 4,
        "Fluency": 5,
        "Error Level": 1,
        "Comment": "Readable and accurate. It kept the main personal improvement idea."
    },

    {
        "Model": "T5",
        "Text Type": "News Article",
        "Generated Summary": "A powerful storm hit several parts of the country yesterday, causing heavy rain, strong winds, and transport delays. Local authorities advised residents to stay indoors and avoid unnecessary travel.",
        "Accuracy": 4,
        "Info Kept": 4,
        "Fluency": 4,
        "Error Level": 1,
        "Comment": "Good short summary, but it missed the flood warning."
    },
    {
        "Model": "T5",
        "Text Type": "Product Review",
        "Generated Summary": "The wireless headphone is comfortable to wear for several hours. The price is reasonable, but the company should improve the case.",
        "Accuracy": 3,
        "Info Kept": 3,
        "Fluency": 4,
        "Error Level": 2,
        "Comment": "Readable, but it missed important details like sound quality, battery life, and weak microphone."
    },
    {
        "Model": "T5",
        "Text Type": "Academic Abstract",
        "Generated Summary": "The study compares different sequence-to-sequence architectures using evaluation metrics. Results show that pre-trained transformer models can generate fluent summaries.",
        "Accuracy": 4,
        "Info Kept": 4,
        "Fluency": 4,
        "Error Level": 1,
        "Comment": "Good summary of the main academic idea."
    },
    {
        "Model": "T5",
        "Text Type": "Movie Plot Summary",
        "Generated Summary": "A young engineer discovers that the company he works for is secretly building a dangerous artificial intelligence system. The system is being used to control personal data and make unfair decisions. He tries to expose the truth before it is released to the public.",
        "Accuracy": 5,
        "Info Kept": 5,
        "Fluency": 4,
        "Error Level": 1,
        "Comment": "One of the strongest T5 summaries. It kept the main plot clearly."
    },
    {
        "Model": "T5",
        "Text Type": "Blog Paragraph",
        "Generated Summary": "Over the past year, I have tried to improve my daily routine by waking up earlier, planning my tasks, and reducing the time I spend on social media. Building small habits helped me become more organized and productive.",
        "Accuracy": 5,
        "Info Kept": 5,
        "Fluency": 4,
        "Error Level": 1,
        "Comment": "Very clear and focused summary."
    },

    {
        "Model": "Pegasus",
        "Text Type": "News Article",
        "Generated Summary": "Flooding has affected thousands of people in southern China's Guangdong province, state media reported on Saturday, with some areas seeing more than a metre of water in some places.",
        "Accuracy": 1,
        "Info Kept": 2,
        "Fluency": 4,
        "Error Level": 5,
        "Comment": "Fluent, but it added incorrect information not found in the original text."
    },
    {
        "Model": "Pegasus",
        "Text Type": "Product Review",
        "Generated Summary": "This is a wireless headphone with a built-in microphone, so you can use it as a stand-alone device, or as part of a larger set of headphones.",
        "Accuracy": 2,
        "Info Kept": 2,
        "Fluency": 4,
        "Error Level": 4,
        "Comment": "It did not keep the real review opinion clearly."
    },
    {
        "Model": "Pegasus",
        "Text Type": "Academic Abstract",
        "Generated Summary": "The summarization of text is a major problem in computer science, and the use of machine learning to do so has become increasingly popular.",
        "Accuracy": 3,
        "Info Kept": 3,
        "Fluency": 4,
        "Error Level": 3,
        "Comment": "General and related to the topic, but it missed many specific points."
    },
    {
        "Model": "Pegasus",
        "Text Type": "Movie Plot Summary",
        "Generated Summary": "A dystopian thriller set in the world of artificial intelligence, the film is written and directed by the award-winning director of the BBC's The Night Manager.",
        "Accuracy": 1,
        "Info Kept": 2,
        "Fluency": 4,
        "Error Level": 5,
        "Comment": "It hallucinated extra information about a director and film details."
    },
    {
        "Model": "Pegasus",
        "Text Type": "Blog Paragraph",
        "Generated Summary": "In our series of letters from African journalists, film-maker, and columnist Sharmila Tagore reflects on her life-changing year-long habit of building small habits.",
        "Accuracy": 1,
        "Info Kept": 2,
        "Fluency": 4,
        "Error Level": 5,
        "Comment": "It added incorrect information that was not in the original blog paragraph."
    },

    {
        "Model": "FLAN-T5",
        "Text Type": "News Article",
        "Generated Summary": "Heavy rain, strong winds and heavy winds have hit parts of the country's northernmost part of the country, officials say.",
        "Accuracy": 2,
        "Info Kept": 3,
        "Fluency": 2,
        "Error Level": 4,
        "Comment": "It kept the weather idea but repeated words and changed the meaning."
    },
    {
        "Model": "FLAN-T5",
        "Text Type": "Product Review",
        "Generated Summary": "Five Stars for a great wireless headphone. It's a little pricey for a wireless headphone, but it's worth it.",
        "Accuracy": 1,
        "Info Kept": 2,
        "Fluency": 4,
        "Error Level": 5,
        "Comment": "It added opinions that were not in the original review."
    },
    {
        "Model": "FLAN-T5",
        "Text Type": "Academic Abstract",
        "Generated Summary": "Automated text summarization is a useful tool for automating text summarization. It can be used to summarise text summaries, but its performance depends on the type of input text and quality of the reference summary.",
        "Accuracy": 3,
        "Info Kept": 3,
        "Fluency": 3,
        "Error Level": 3,
        "Comment": "Partly correct, but repetitive and less precise."
    },
    {
        "Model": "FLAN-T5",
        "Text Type": "Movie Plot Summary",
        "Generated Summary": "Using artificial intelligence, he tries to expose the truth before the technology is released to the public to the public.",
        "Accuracy": 3,
        "Info Kept": 3,
        "Fluency": 2,
        "Error Level": 3,
        "Comment": "It captured part of the idea but repeated words."
    },
    {
        "Model": "FLAN-T5",
        "Text Type": "Blog Paragraph",
        "Generated Summary": "Having a habit of waking up earlier helped me become more organized and productive in the long run. Having small habits helped me become more organized and productive in the long run.",
        "Accuracy": 4,
        "Info Kept": 4,
        "Fluency": 3,
        "Error Level": 2,
        "Comment": "Mostly correct, but repetitive."
    },
]

df = pd.DataFrame(results_data)
df["Overall Score"] = ((df["Accuracy"] + df["Info Kept"] + df["Fluency"]) / 3).round(2)

model_summary = (
    df.groupby("Model")
    .agg({
        "Accuracy": "mean",
        "Info Kept": "mean",
        "Fluency": "mean",
        "Error Level": "mean",
        "Overall Score": "mean"
    })
    .round(2)
    .reset_index()
)

text_type_summary = (
    df.groupby("Text Type")
    .agg({
        "Accuracy": "mean",
        "Info Kept": "mean",
        "Fluency": "mean",
        "Error Level": "mean",
        "Overall Score": "mean"
    })
    .round(2)
    .reset_index()
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Choose a section:",
    [
        "Project Overview",
        "Generated Summaries",
        "Model Comparison",
        "Text Type Analysis",
        "Final Conclusion"
    ]
)

# ---------------------------------------------------
# Page 1: Overview
# ---------------------------------------------------

if page == "Project Overview":
    st.title("Summarization Model Comparison")

    st.markdown("""

    The goal is to compare different summarization models on the same text types using a clear and organized interface.

    ### Models Compared
    - DistilBART / BART
    - T5
    - Pegasus
    - FLAN-T5

    ### Text Types Used
    - News article
    - Product review
    - Academic abstract
    - Movie plot summary
    - Blog paragraph / long social media post

    ### Evaluation Criteria
    The summaries were compared using manual evaluation based on:

    - Accuracy
    - Important information kept
    - Fluency and readability
    - Weaknesses or errors
    - Best and worst text type for each model
    """)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Models", df["Model"].nunique())
    col2.metric("Text Types", df["Text Type"].nunique())
    col3.metric("Total Summaries", len(df))
    col4.metric("Best Model", "DistilBART / BART")

    st.info(
        "Note: These scores are based on human/manual evaluation of the generated summaries, not automatic ROUGE scores."
    )

# ---------------------------------------------------
# Page 2: Generated Summaries
# ---------------------------------------------------

elif page == "Generated Summaries":
    st.title("Generated Summaries")

    selected_model = st.selectbox("Select model:", sorted(df["Model"].unique()))
    selected_text_type = st.selectbox("Select text type:", sorted(df["Text Type"].unique()))

    filtered = df[
        (df["Model"] == selected_model) &
        (df["Text Type"] == selected_text_type)
    ]

    if not filtered.empty:
        row = filtered.iloc[0]

        st.subheader(f"{selected_model} - {selected_text_type}")

        st.markdown("### Generated Summary")
        st.write(row["Generated Summary"])

        st.markdown("### Evaluation")
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Accuracy", f"{row['Accuracy']}/5")
        col2.metric("Info Kept", f"{row['Info Kept']}/5")
        col3.metric("Fluency", f"{row['Fluency']}/5")
        col4.metric("Error Level", f"{row['Error Level']}/5")

        st.markdown("### Comment")
        st.write(row["Comment"])

    st.markdown("---")
    st.markdown("### Full Results Table")
    st.dataframe(df, use_container_width=True)

# ---------------------------------------------------
# Page 3: Model Comparison
# ---------------------------------------------------

elif page == "Model Comparison":
    st.title("Model Comparison")

    st.markdown("""
    This section compares the average performance of each model across all five text types.
    """)

    st.subheader("Average Scores by Model")
    st.dataframe(model_summary, use_container_width=True)

    st.subheader("Overall Score by Model")
    chart_data = model_summary.set_index("Model")["Overall Score"]
    st.bar_chart(chart_data)

    st.subheader("Error Level by Model")
    error_chart = model_summary.set_index("Model")["Error Level"]
    st.bar_chart(error_chart)

    st.markdown("""
    ### Short Analysis

    **DistilBART / BART** performed best overall because it kept the original meaning and important details.

    **T5** was also strong, especially for the movie plot summary and blog paragraph, but it sometimes removed smaller details.

    **Pegasus** produced fluent summaries, but it hallucinated information that was not in the input.

    **FLAN-T5** was understandable, but it sometimes repeated phrases or added opinions that were not in the original text.
    """)

# ---------------------------------------------------
# Page 4: Text Type Analysis
# ---------------------------------------------------

elif page == "Text Type Analysis":
    st.title("Text Type Analysis")

    st.markdown("""
    This section shows which text types were easier or harder to summarize.
    """)

    st.subheader("Average Scores by Text Type")
    st.dataframe(text_type_summary, use_container_width=True)

    st.subheader("Overall Score by Text Type")
    chart_data = text_type_summary.set_index("Text Type")["Overall Score"]
    st.bar_chart(chart_data)

    st.subheader("Error Level by Text Type")
    error_chart = text_type_summary.set_index("Text Type")["Error Level"]
    st.bar_chart(error_chart)

    st.markdown("""
    ### Short Analysis

    The **news article** and **blog paragraph** were easier for most models because they had clear structure and direct meaning.

    The **product review** was harder because models needed to keep both positive and negative opinions.

    The **academic abstract** was also challenging because it contained technical language.

    Pegasus and FLAN-T5 struggled more because they sometimes added information that was not in the original text.
    """)

# ---------------------------------------------------
# Page 5: Final Conclusion
# ---------------------------------------------------

elif page == "Final Conclusion":
    st.title("Final Conclusion")

    st.markdown("""
    ## Final Comparison

    ### Best Model Overall
    **DistilBART / BART** performed best overall.

    It produced the most accurate and faithful summaries. It kept important information and did not add many incorrect details.

    ### Second Best Model
    **T5** was also strong.

    It produced short and clear summaries, but it sometimes removed important smaller details.

    ### Weakest Model
    **Pegasus** struggled the most in this experiment.

    Even though its summaries sounded fluent, it added information that was not in the original input. This is called hallucination.

    ### Extra Model Result
    **FLAN-T5** was better than Pegasus in some cases, but it still made mistakes.

    It sometimes repeated phrases or added opinions that were not in the original text.

    ## Easiest Text Type
    The easiest text type to summarize was the **news article** because it had clear facts and a direct structure.

    ## Hardest Text Type
    The hardest text type was the **product review** because the model needed to keep both positive and negative opinions without changing the meaning.

    ## Main Lesson
    Higher fluency does not always mean a better summary.

    A model can produce a readable summary but still be wrong if it adds information that was not in the original text.
    """)

    st.success("Final answer: DistilBART / BART was the best model overall in this experiment.")