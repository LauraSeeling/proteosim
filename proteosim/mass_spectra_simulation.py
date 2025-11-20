def calculate_mol_mass(peptide_seq, amino_acid_mass_dict):
    """
    Calculate the molecular mass for each peptide in a list.

    Parameters
    ----------
    peptide_seq : str
        peptide sequence
    amino_acid_mass_dict : dict
        Dictionary containing molecular masses of all amino acids.

    Returns
    -------
    dict
        Dictionary mapping each peptide to its molecular mass.
    """
    
    peptide_mass = {}

    
    mass = 0                     # reset mass for each peptide

    for aa in peptide_seq:               # each amino acid is extracted separatly from sequence
        mass += amino_acid_mass_dict[aa]

    peptide_mass[peptide_seq] = mass   # save total mass for this peptide

    return peptide_mass

def calculate_mol_mass_collection(peptide_list, amino_acid_mass_dict):
    """
    Calculate molecular mass for a list of peptide sequences.

    Parameters
    ----------
    peptide_list : list of str
        A list containing peptide sequences.
    amino_acid_mass_dict : dict
        Dictionary with amino-acid molecular masses.

    Returns
    -------
    dict
        Dictionary mapping peptide -> molecular mass.
    """
    
    peptide_masses = {}

    for pep in peptide_list:          
        mass = 0

        for aa in pep:               
            mass += amino_acid_mass_dict[aa]

        peptide_masses[pep] = mass

    return peptide_masses

def calculate_mz_collection(peptide_mass_map, charge=2, proton_mass=1.007):
    """
    Add a short description here.

    Parameters
    peptide_mass_map: dict of {str: float}
      dictionary containing peptide sequence and molecular mass

    Returns
    dict of {str: float}
      dictionary containing the peptide sequence and mass to charge ratio

    """
    peptide_mz = {}

    for pep, mass in peptide_mass_map.items():
        mz = 0
        mz = (mass + charge * proton_mass) / charge
        peptide_mz[pep] = mz

    return peptide_mz


import numpy as np
import matplotlib.pyplot as plt

def plot_ms1(mz_map, random_count_range=(1000, 50000), seed=42, title = 'MS Spektrum'): #man könnte hier auch die vorher definierte plot funktion verwenden und nur den title ändern
    """
    Plot an MS2 spectrum (fragment m/z vs intensity).

    Parameters
    ----------
    mz2_map : dict {str: float}
        Dictionary mapping fragment names to m/z values.
    random_count_range : tuple, optional
        Range for random intensities (min, max).
    seed : int
        Seed for reproducible random intensities.

    Returns
    -------
    None
        Displays MS2 bar chart.
    """

    # Extract m/z values and fragment labels
    fragments = list(mz_map.keys())
    mz_values = list(mz_map.values())

    # Random intensities (MS2 always has variable peak heights)
    np.random.seed(seed)
    intensities = np.random.randint(
        random_count_range[0], random_count_range[1], size=len(mz_values)
    )

    plt.figure(figsize=(12, 6))
    plt.bar(mz_values, intensities, width=1.0)

    # Labeling
    for mz, label, inten in zip(mz_values, fragments, intensities):
        plt.text(
            mz,                            # x-Position: m/z-Wert
            inten + inten * 0.03,          # leicht über dem Peak
            label,                         # z.B. "b2"
            rotation=90,                   # senkrechte Beschriftung
            fontsize=8,
            ha='center'                    # zentriert über dem Peak
        )

    plt.xlabel("m/z")
    plt.ylabel("Intensity")
    plt.title(title)
    plt.tight_layout()
    plt.show()


def fragment_peptide(peptide):
    """
    Generate b- and y-ion sequences for a single peptide.

    Parameters
    ----------
    peptide : str
        Peptide sequence

    Returns
    -------
    dict
        Dictionary mapping the peptide to a list of b- and y-ions
    """
    # b-ions: N-term to C-term
    b_ions = [peptide[:i] for i in range(1, len(peptide)+1)]

    # y-ions: C-term to N-term
    y_ions = [peptide[i:] for i in range(len(peptide)-1, -1, -1)]

    return {peptide: b_ions + y_ions}

