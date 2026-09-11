import streamlit as st


st.set_page_config(
    page_title="Assessment",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Cheminformatics Virtual Lab Assessment")

st.markdown("""
Answer the following questions to assess your understanding
of the experiment.
""")

# -------------------------------------------------
# QUESTIONS
# -------------------------------------------------

questions = [

    {
        "question":
        "What does SMILES represent?",

        "options": [
            "A molecular text representation",
            "A molecular weight",
            "A spectroscopy technique",
            "A laboratory instrument"
        ],

        "answer":
        "A molecular text representation"
    },

    {
        "question":
        "Which descriptor is commonly associated with lipophilicity?",

        "options": [
            "TPSA",
            "LogP",
            "HBD",
            "Molecular Formula"
        ],

        "answer":
        "LogP"
    },

    {
        "question":
        "TPSA mainly provides information about:",

        "options": [
            "Molecular polarity",
            "Atomic number",
            "Colour",
            "Melting apparatus"
        ],

        "answer":
        "Molecular polarity"
    },

    {
        "question":
        "Which toolkit is commonly used for cheminformatics in Python?",

        "options": [
            "RDKit",
            "Microsoft Word",
            "PowerPoint",
            "Excel only"
        ],

        "answer":
        "RDKit"
    },

    {
        "question":
        "HBD stands for:",

        "options": [
            "Hydrogen Bond Donor",
            "Hydrogen Bond Density",
            "High Bond Distance",
            "Hydrogen Binary Data"
        ],

        "answer":
        "Hydrogen Bond Donor"
    }
]


# -------------------------------------------------
# STUDENT ANSWERS
# -------------------------------------------------

student_answers = []

for i, item in enumerate(questions):

    answer = st.radio(

        f"{i+1}. {item['question']}",

        item["options"],

        key=f"question_{i}"
    )

    student_answers.append(answer)


# -------------------------------------------------
# SUBMIT
# -------------------------------------------------

if st.button("Submit Assessment"):

    score = 0

    for i, answer in enumerate(student_answers):

        if answer == questions[i]["answer"]:

            score += 1

    st.divider()

    st.success(
        f"Your Score: {score} / {len(questions)}"
    )

    percentage = (
        score / len(questions)
    ) * 100

    st.metric(
        "Percentage",
        f"{percentage:.1f}%"
    )

    if score == len(questions):

        st.balloons()

        st.success(
            "🎉 Excellent! You have successfully completed the Cheminformatics Virtual Laboratory."
        )

    elif percentage >= 60:

        st.info(
            "Good performance! Review the theory section to strengthen your understanding."
        )

    else:

        st.warning(
            "Please review the theory and repeat the virtual experiment."
        )