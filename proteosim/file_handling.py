def read_fasta(filepath):
    """
    Add a short description here.

    Parameters
     filepath : str
        Path to a FASTA-formatted text file. The file may contain one
        or multiple entries. Header lines must begin with '>'.
    Returns
    dict of {str: str}
        A dictionary mapping FASTA headers (without the leading '>')
        to their corresponding sequences. Sequences spanning multiple
        lines are concatenated into a single string. Blank lines are
        ignored automatically.
    """
    protein_map = {}
    current_id = None
    current_sequence = []

    with open(filepath, 'r', encoding='utf-8') as fasta_handle:
        for line in fasta_handle:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith('>'):
                if current_id is not None:
                    protein_map[current_id] = ''.join(current_sequence)
                    current_sequence = []
                current_id = stripped.split('|')[1]
            else:
                current_sequence.append(stripped)
        if current_id is not None:
            protein_map[current_id] = ''.join(current_sequence)

    return protein_map