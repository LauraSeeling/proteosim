import re

enzyme_cleavage_patterns = {
    'LysC': r'(?<=K)', # nach Lysin geschnitten (rechts)
    'LysN': r'(?=K)', # vor Lysin geschnitten (links)
    'ArgC': r'(?<=R)',
    'Trypsin': r'(?<=[KR])(?!P)', # [] entweder oder der beiden argumente + nicht schneiden wenn Prolin rechts danach kommt
}

def digest_protein_sequence(protein_seq, cleave_pattern, min_pep_len=5, max_pep_len=30):
     """
     Function description

     Parameters
      protein_seq: str
        letter code for sequence of amino acids in protein

      cleave_pattern: str
        cleavage pattern of enzyme in the following format r'(?<=x)' with x being an amino acid

      min_pep_len: int
        minimum length for LC/MS detection; default = 5 
      max_pep_len: int
        maximum length fpr LC/MS detection; default = 30
    
     Returns
      list 
        list of peptide fragments is returned

     """
     
     if len(protein_seq) == 0:
      return("sequence is empty")
     if min_pep_len > max_pep_len:
      return('Length controls need to be changed')
     else:
      peptides = re.split(cleave_pattern, protein_seq)
      filtered_peptides = [pep for pep in peptides if min_pep_len <= len(pep) <= max_pep_len]
      return filtered_peptides


def digest_protein_collection(protein_map, cleave_pattern, min_pep_len=5, max_pep_len=30):
     """
     Function description

     Parameters
      protein_map: dict
        letter code for sequence of amino acids in protein

      cleave_pattern: str
        cleavage pattern of enzyme in the following format r'(?<=x)' with x being an amino acid

      min_pep_len: int
        minimum length for LC/MS detection
      max_pep_len: int
        maximum length fpr LC/MS detection
    
     Returns
      dict of {str: str}
        dictionary of peptide fragments is returned for each protein ID

     """
     digested_peptides_map = {}
     protein = protein_map.keys()
     for pro in protein:
      if len(protein_map[pro]) == 0:  # oberen beiden if loops wahrscheinlich unnötig
       return("sequence is empty")
      if min_pep_len > max_pep_len:
       return('Length controls need to be changed')
      else:
        digested_peptides = digest_protein_sequence(protein_map[pro], cleave_pattern, min_pep_len, max_pep_len)
        digested_peptides_map[pro]= digested_peptides
     return digested_peptides_map


def compute_sequence_coverage(protein_seq, peptides):
    """
    Add a short description here.
    function to compute sequence coverage of protein with its detected
    Parameters
     protein_seq: str
     peptides: 
    Returns
    float
      shows pcoverage in percent (not as decimal number): percentage of protein sequence covered by peptides
    """
    if not protein_seq or not peptides:
        return 0
    coverage = set()
    for pep in peptides:
        idx_start = 0
        while True:
            idx = protein_seq.find(pep, idx_start)
            if idx == -1:
                break
            coverage.update(range(idx, idx + len(pep)))
            idx_start = idx_start +1 # könnte man auch mit += machen
    coverage_percent = len(coverage) / len(protein_seq) *100

    return coverage_percent