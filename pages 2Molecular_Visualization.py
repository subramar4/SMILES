import streamlit as st

from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem

import py3Dmol
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Molecular Visualization",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Molecular Representation and Visualization")

st.markdown("""
Enter a **SMILES string** to generate and visualize the molecular
structure.
""")

# -------------------------------------------------
# USER INPUT
# -------------------------------------------------

smiles = st.text_input(
    "Enter SMILES",
    value="CCO"
)

# -------------------------------------------------
# CREATE MOLECULE
# -------------------------------------------------

mol = Chem.MolFromSmiles(smiles)

if mol is None:

    st.error("❌ Invalid SMILES. Please enter a valid SMILES string.")

else:

    col1, col2 = st.columns(2)

    # ---------------------------------------------
    # 2D STRUCTURE
    # ---------------------------------------------

    with col1:

        st.subheader("2D Molecular Structure")

        image = Draw.MolToImage(
            mol,
            size=(500, 400)
        )

        st.image(image)

    # ---------------------------------------------
    # MOLECULAR INFORMATION
    # ---------------------------------------------

    with col2:

        st.subheader("Molecular Information")

        canonical_smiles = Chem.MolToSmiles(mol)

        st.write(
            "**Canonical SMILES:**",
            canonical_smiles
        )

        st.write(
            "**Number of atoms:**",
            mol.GetNumAtoms()
        )

        st.write(
            "**Number of bonds:**",
            mol.GetNumBonds()
        )

        st.success(
            "SMILES successfully converted into a molecular structure."
        )

    st.divider()

    # ---------------------------------------------
    # 3D STRUCTURE
    # ---------------------------------------------

    st.subheader("🧬 3D Molecular Visualization")

    if st.button("Generate 3D Structure"):

        mol3d = Chem.AddHs(mol)

        status = AllChem.EmbedMolecule(
            mol3d,
            randomSeed=42
        )

        if status == 0:

            try:

                AllChem.MMFFOptimizeMolecule(mol3d)

            except:

                pass

            mol_block = Chem.MolToMolBlock(mol3d)

            view = py3Dmol.view(
                width=800,
                height=500
            )

            view.addModel(
                mol_block,
                "mol"
            )

            view.setStyle(
                {"stick": {}}
            )

            view.setBackgroundColor("white")

            view.zoomTo()

            components.html(
                view._make_html(),
                height=520,
                scrolling=False
            )

        else:

            st.warning(
                "Unable to generate the 3D structure for this molecule."
            )