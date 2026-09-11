import streamlit as st

st.set_page_config(
    page_title="Theory | Cheminformatics Lab",
    page_icon="📖",
    layout="wide"
)

st.title("📖 Theory: Basics of Cheminformatics")

st.divider()

st.markdown("""
# What is Cheminformatics?

**Cheminformatics** is an interdisciplinary field that combines:

- ⚗️ Chemistry
- 💻 Computer Science
- 📊 Data Science

It involves the storage, retrieval, analysis and visualization of
chemical information using computational methods.

Cheminformatics is widely used in:

- Drug discovery
- Molecular modelling
- Chemical database searching
- Property prediction
- Materials discovery
- Computational chemistry
""")

st.markdown("## 🧬 Molecular Representations")

st.markdown("""
Chemical molecules can be represented in several ways.
""")

st.markdown("""
### 1. Molecular Formula

A molecular formula represents the number of atoms present in a molecule.

Example:

**Ethanol → C₂H₆O**
""")

st.markdown("""
### 2. Structural Formula

A structural formula shows how atoms are connected.

Example:

CH₃–CH₂–OH
""")

st.markdown("""
### 3. SMILES

**SMILES** stands for:

> Simplified Molecular Input Line Entry System

It represents chemical structures using a text string.
""")

st.markdown("""
| Molecule | SMILES |
|---|---|
| Ethanol | `CCO` |
| Benzene | `c1ccccc1` |
| Acetic Acid | `CC(=O)O` |
| Water | `O` |
""")

st.markdown("## 📊 Molecular Descriptors")

st.markdown("""
Molecular descriptors are numerical values that describe the
properties of molecules.
""")

st.markdown("""
### Molecular Weight (MW)

The total mass of a molecule.

### LogP

LogP represents the **lipophilicity** of a molecule.

Higher LogP generally indicates greater affinity for non-polar
environments.

### TPSA

TPSA stands for:

**Topological Polar Surface Area**

It provides information about molecular polarity.

### HBD

**Hydrogen Bond Donors**

Atoms or groups capable of donating hydrogen bonds.

### HBA

**Hydrogen Bond Acceptors**

Atoms or groups capable of accepting hydrogen bonds.
""")

st.markdown("## 🔬 Structure–Property Relationships")

st.markdown("""
The chemical structure of a molecule influences its physical and
chemical properties.

Changes in:

- Functional groups
- Molecular size
- Number of heteroatoms
- Aromatic rings
- Molecular polarity

can influence:

- Solubility
- Lipophilicity
- Molecular weight
- Hydrogen bonding
- Biological activity
""")

st.info("""
The next section allows you to enter a SMILES string and visualize
the corresponding chemical structure.
""")