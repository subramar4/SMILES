import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from rdkit import Chem
from rdkit.Chem import (
    Descriptors,
    Crippen,
    Lipinski,
    rdMolDescriptors
)


st.set_page_config(
    page_title="Structure Property Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Structure–Property Relationship Analysis")

st.markdown("""
Compare different molecules and investigate how molecular structure
influences physicochemical properties.
""")

# -------------------------------------------------
# DEFAULT MOLECULES
# -------------------------------------------------

default_data = """Ethanol,CCO
Phenol,Oc1ccccc1
Acetic Acid,CC(=O)O
Caffeine,CN1C=NC2=C1C(=O)N(C(=O)N2C)C
Benzene,c1ccccc1
"""

# -------------------------------------------------
# USER INPUT
# -------------------------------------------------

text = st.text_area(
    "Enter molecules in the format: Name,SMILES",
    value=default_data,
    height=200
)

# -------------------------------------------------
# PROCESS MOLECULES
# -------------------------------------------------

rows = []

for line in text.strip().splitlines():

    if "," not in line:
        continue

    name, smiles = line.split(",", 1)

    mol = Chem.MolFromSmiles(
        smiles.strip()
    )

    if mol is not None:

        rows.append({

            "Molecule": name.strip(),

            "SMILES":
            Chem.MolToSmiles(mol),

            "MW":
            round(Descriptors.MolWt(mol), 2),

            "LogP":
            round(Crippen.MolLogP(mol), 2),

            "TPSA":
            round(
                rdMolDescriptors.CalcTPSA(mol),
                2
            ),

            "HBD":
            Lipinski.NumHDonors(mol),

            "HBA":
            Lipinski.NumHAcceptors(mol)
        })


# -------------------------------------------------
# DISPLAY RESULTS
# -------------------------------------------------

if rows:

    df = pd.DataFrame(rows)

    st.subheader("📊 Molecular Property Comparison")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ---------------------------------------------
    # GRAPH SELECTION
    # ---------------------------------------------

    properties = [
        "MW",
        "LogP",
        "TPSA",
        "HBD",
        "HBA"
    ]

    col1, col2 = st.columns(2)

    with col1:

        x_axis = st.selectbox(
            "Select X-axis",
            properties,
            index=0
        )

    with col2:

        y_axis = st.selectbox(
            "Select Y-axis",
            properties,
            index=1
        )

    # ---------------------------------------------
    # PLOT
    # ---------------------------------------------

    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    ax.scatter(
        df[x_axis],
        df[y_axis],
        s=100
    )

    for _, row in df.iterrows():

        ax.annotate(
            row["Molecule"],
            (
                row[x_axis],
                row[y_axis]
            )
        )

    ax.set_xlabel(x_axis)

    ax.set_ylabel(y_axis)

    ax.set_title(
        f"{x_axis} vs {y_axis}"
    )

    st.pyplot(fig)

    # ---------------------------------------------
    # STUDENT QUESTIONS
    # ---------------------------------------------

    st.subheader("🧠 Student Analysis")

    st.markdown("""
Answer the following questions based on your results:

1. Which molecule has the highest molecular weight?

2. Which molecule has the highest LogP?

3. Which molecule has the highest TPSA?

4. How do functional groups influence HBD and HBA?

5. What relationship can you observe between molecular structure
and molecular properties?
""")

else:

    st.warning(
        "Please enter at least one valid molecule."
    )