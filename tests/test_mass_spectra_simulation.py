from proteosim.mass_spectra_simulation import(
    calculate_mol_mass,
    calculate_mol_mass_collection,
    calculate_mz_collection,
    fragment_peptide
)

def test_calculate_mol_mass_collection():
    amino_acid_mass_dalton = {
    'A': 71.08, 'R': 156.19, 'N': 114.10, 'D': 115.09,
    'C': 103.15, 'E': 129.12, 'Q': 128.13, 'G': 57.05,
    'H': 137.14, 'I': 113.16, 'L': 113.16, 'K': 128.17,
    'M': 131.19, 'F': 147.18, 'P': 97.12, 'S': 87.08,
    'T': 101.11, 'W': 186.21, 'Y': 163.18, 'V': 99.13,
    }
    peptides = ['AKQE', 'RTSP'] #man könnte sich noch überlegen was funktion ausgeben sollte falls AS nicht in amino_acid_mass drin ist
    expected = {'AKQE': 456.50, 'RTSP': 441.50} #könnte man auch per werte extraktion aus dem dictionary machen
    actual = calculate_mol_mass_collection(peptides, amino_acid_mass_dalton) #wegen amino_acid_mass_dalton ist test nicht unabhängig von skript -> man muss das dictionary nochmal in test reinkopieren

    assert actual == expected

test_calculate_mol_mass_collection()

def test_calculate_mz_collection():
    peptide_mass_map = {'AKQE': 456.50, 'RTSP':441.50}
    actual = calculate_mz_collection(peptide_mass_map, charge=2)
    expected = {'AKQE': 229.257 , 'RTSP': 221.757}

    assert actual == expected

test_calculate_mz_collection()

def test_fragment_peptide():
    peptide = 'PEPT'
    expected = {'PEPT': ['P','PE', 'PEP', 'PEPT', 'T', 'PT', 'EPT', 'PEPT']}
    actual = fragment_peptide(peptide)

    assert set(actual) == set(expected) # set( macht assertion unabhängig von Reihenfolge)

test_fragment_peptide()