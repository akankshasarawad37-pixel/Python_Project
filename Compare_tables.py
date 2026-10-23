# compare_tables.py
# Compares the codon table from codon_table.py with reference codon tables.

from codon_table import CODON_TABLE

# One-letter amino acid codes -> 3-letter codes (used by the reference tables)
ONE_TO_THREE = {
    "F": "Phe", "L": "Leu", "I": "Ile", "M": "Met", "V": "Val",
    "S": "Ser", "P": "Pro", "T": "Thr", "A": "Ala", "Y": "Tyr",
    "H": "His", "Q": "Gln", "N": "Asn", "K": "Lys", "D": "Asp",
    "E": "Glu", "C": "Cys", "W": "Trp", "R": "Arg", "G": "Gly",
    "*": "Stop",
}

# The standard genetic code (NCBI translation table 1) written as one string.
# Codons are ordered T, C, A, G for the 1st, 2nd and 3rd letters; * = stop.
NCBI_AMINO_ACIDS = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"


def build_ncbi_table():
    """Build a codon dictionary from the NCBI one-string standard genetic code."""
    table = {}
    index = 0
    for first in "TCAG":
        for second in "TCAG":
            for third in "TCAG":
                codon = first + second + third
                table[codon] = ONE_TO_THREE[NCBI_AMINO_ACIDS[index]]
                index += 1
    return table


def build_biopython_table():
    """Build a codon dictionary from Biopython's standard table (None if not installed)."""
    try:
        from Bio.Data import CodonTable
    except ImportError:
        return None

    standard = CodonTable.unambiguous_dna_by_id[1]   # table 1 = standard genetic code
    table = {}
    for codon, one_letter in standard.forward_table.items():
        table[codon] = ONE_TO_THREE[one_letter]
    for codon in standard.stop_codons:
        table[codon] = "Stop"
    return table


def compare_tables(my_table, reference_table, reference_name):
    """Compare two codon dictionaries and print any differences."""
    print(f"\nComparing with: {reference_name}")
    print(f"  My table: {len(my_table)} codons | Reference: {len(reference_table)} codons")

    differences = []
    all_codons = sorted(set(my_table) | set(reference_table))   # union of both key sets
    for codon in all_codons:
        mine = my_table.get(codon, "MISSING")
        other = reference_table.get(codon, "MISSING")
        if mine != other:
            differences.append((codon, mine, other))

    if len(differences) == 0:
        print("  Result: MATCH - all codons are identical.")
        return True

    print(f"  Result: {len(differences)} difference(s) found")
    print(f"  {'Codon':<8}{'Mine':<10}{'Reference':<10}")
    for codon, mine, other in differences:
        print(f"  {codon:<8}{mine:<10}{other:<10}")
    return False


def main():
    # 1. NCBI standard genetic code (always available, no install needed)
    compare_tables(CODON_TABLE, build_ncbi_table(), "NCBI standard genetic code (table 1)")

    # 2. Biopython's standard table (needs: pip install biopython)
    biopython_table = build_biopython_table()
    if biopython_table is None:
        print("\nBiopython is not installed - skipping. Install it with: pip install biopython")
    else:
        compare_tables(CODON_TABLE, biopython_table, "Biopython standard table")

    # 3. Optional: a codon table copied from a GitHub repository.
    #    Copy the dictionary into a file named github_table.py and call it
    #    GITHUB_TABLE (DNA codons with T, amino acids as 3-letter codes like "Phe").
    try:
        from github_table import GITHUB_TABLE
        compare_tables(CODON_TABLE, GITHUB_TABLE, "GitHub repository table")
    except ImportError:
        print("\nNo github_table.py found - skipping the GitHub comparison.")


if __name__ == "__main__":
    main()