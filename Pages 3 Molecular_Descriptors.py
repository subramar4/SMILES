import streamlit as st
import pandas as pd

from rdkit import Chem
from rdkit.Chem import (
    Descriptors,
    Crippen,
    Lipinski,
    rdMolDescriptors
)


st.set_page_config(
    page_title="Molecular Descriptors",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Molecular Descriptor Calculator")

st.markdown("""
Enter a molecular SMILES string to calculate important
physicochemical descriptors.
""")

# -------------------------------------------------
# INPUT
# -------------------------------------------------

smiles = st.text_input(
    "Enter SMILES",
    value="CCO"
)

mol = Chem.MolFromSmiles(smiles)

if mol is None:

    st.error("❌ Invalid SMILES.")

else:

    # ---------------------------------------------
    # CALCULATE DESCRIPTORS
    # ---------------------------------------------

    molecular_weight = round(
        Descriptors.MolWt(mol),
        2
    )

    logp = round(
        Crippen.MolLogP(mol),
        2
    )

    tpsa = round(
        rdMolDescriptors.CalcTPSA(mol),
        2
    )

    hbd = Lipinski.NumHDonors(mol)

    hba = Lipinski.NumHAcceptors(mol)

    rotatable_bonds = Lipinski.NumRotatableBonds(mol)

    ring_count = Lipinski.RingCount(mol)

    # ---------------------------------------------
    # METRICS
    # ---------------------------------------------

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Molecular Weight",
        molecular_weight
    )

    col2.metric(
        "LogP",
        logp
    )

    col3.metric(
        "TPSA",
        tpsa
    )

    st.divider()

    # ---------------------------------------------
    # TABLE
    # ---------------------------------------------

    data = {

        "Descriptor": [
            "Molecular Weight",
            "LogP",
            "TPSA",
            "Hydrogen Bond Donors",
            "Hydrogen Bond Acceptors",
            "Rotatable Bonds",
            "Ring Count"
        ],

        "Value": [
            molecular_weight,
            logp,
            tpsa,
            hbd,
            hba,
            rotatable_bonds,
            ring_count
        ]
    }

    df = pd.DataFrame(data)

    st.subheader("Complete Molecular Descriptor Table")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # ---------------------------------------------
    # INTERPRETATION
    # ---------------------------------------------

    st.subheader("🔍 Interpretation")

    if logp > 3:

        st.warning(
            "The molecule has relatively high lipophilicity."
        )

    else:

        st.info(
            "The molecule has low to moderate lipophilicity."
        )

    if tpsa > 90:

        st.info(
            "The molecule has a relatively high polar surface area."
        )

    if hbd > 0:

        st.success(
            f"The molecule contains {hbd} hydrogen bond donor(s)."
        )

    if hba > 0:

        st.success(
            f"The molecule contains {hba} hydrogen bond acceptor(s)."
        )