from proteosim.protein_digestion import (
    digest_protein_sequence,
    digest_protein_collection,
    compute_sequence_coverage,
)

def test_digest_protein_collection():
    dummy_proteins = {
        "PROTEIN_ID_1": "AQELKEDVPL",
        "PROTEIN_ID_2": "AQWEKADCSR"
    }

    enzyme_cleavage_patterns = {
    'LysC': r'(?<=K)', # nach Lysin geschnitten (rechts)
    'LysN': r'(?=K)', # vor Lysin geschnitten (links)
    'ArgC': r'(?<=R)',
    'Trypsin': r'(?<=[KR])(?!P)', # [] entweder oder der beiden argumente + nicht schneiden wenn Prolin rechts danach kommt
    }
    lys_c_digest_protein_collection = digest_protein_collection(dummy_proteins, cleave_pattern = enzyme_cleavage_patterns["LysC"])

    assert lys_c_digest_protein_collection.get("PROTEIN_ID_1") == ["AQELK", "EDVPL"]  
    assert lys_c_digest_protein_collection.get("PROTEIN_ID_2") == ["AQWEK", "ADCSR"]

test_digest_protein_collection()

def test_compute_sequence_coverage():
    dummy_prot_seq = "AQELKEDVPL"
    dummy_peps = ["AQELK", "EDVPL"]
    # bei isabell als sequenzen voll ungeschnitten, voll geschnitten mit 100% coverage, verschiedenen Prozentzahlen, empty und eine die überhaupt nicht matched
    coverage = 100.0 # wenn jede stelle abgedeckt werden würde -> man müsste noch mehrere andere fälle abdecken (0 af jeden fall noch und noch andere varianten außer grenzfälle)
    assert coverage == compute_sequence_coverage(dummy_prot_seq,dummy_peps)

test_compute_sequence_coverage()
