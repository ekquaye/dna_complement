"""Main module."""


def complement_DNA(dna_sequence=None) -> None:
    """
    complement_DNA(dna_sequence: Prints the dna reverse complement sequence.

    Parameters
    ----------
    dna_sequence : dna.sequence
           reverse complement of the dna sequence.

    """
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement_sequence = ''.join([complement_dict[base] for base in dna_sequence])
    return complement_sequence
