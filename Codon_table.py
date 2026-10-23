# Codon Table Generator
# Translates a DNA sequence into amino acids using the standard genetic code.



# ---------------------------------------------------------------
# Data (constants are written in CAPITAL LETTERS by convention)
# ---------------------------------------------------------------

# Dictionary of all 64 codons -> amino acids (3-letter code)
CODON_TABLE = {
    "TTT": "Phe", "TTC": "Phe", "TTA": "Leu", "TTG": "Leu",
    "CTT": "Leu", "CTC": "Leu", "CTA": "Leu", "CTG": "Leu",
    "ATT": "Ile", "ATC": "Ile", "ATA": "Ile", "ATG": "Met",
    "GTT": "Val", "GTC": "Val", "GTA": "Val", "GTG": "Val",
    "TCT": "Ser", "TCC": "Ser", "TCA": "Ser", "TCG": "Ser",
    "CCT": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACT": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCT": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "TAT": "Tyr", "TAC": "Tyr", "TAA": "Stop", "TAG": "Stop",
    "CAT": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "AAT": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "GAT": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "TGT": "Cys", "TGC": "Cys", "TGA": "Stop", "TGG": "Trp",
    "CGT": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGT": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GGT": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
}

# Full names for the 3-letter amino acid codes
AMINO_ACID_NAMES = {
    "Phe": "Phenylalanine", "Leu": "Leucine", "Ile": "Isoleucine",
    "Met": "Methionine", "Val": "Valine", "Ser": "Serine",
    "Pro": "Proline", "Thr": "Threonine", "Ala": "Alanine",
    "Tyr": "Tyrosine", "His": "Histidine", "Gln": "Glutamine",
    "Asn": "Asparagine", "Lys": "Lysine", "Asp": "Aspartic acid",
    "Glu": "Glutamic acid", "Cys": "Cysteine", "Trp": "Tryptophan",
    "Arg": "Arginine", "Gly": "Glycine", "Stop": "Stop",
}


def make_rna_table(dna_table):
    """Build the RNA codon table by replacing T with U in every codon."""
    rna_table = {}
    for codon, amino_acid in dna_table.items():
        rna_table[codon.replace("T", "U")] = amino_acid
    return rna_table


RNA_CODON_TABLE = make_rna_table(CODON_TABLE)

# Rules for each sequence type
GENETIC_CODES = {
    "DNA": {
        "table": CODON_TABLE,
        "valid_bases": "ATGC",
        "start": "ATG",
        "stops": ["TAA", "TAG", "TGA"],
        "grid_order": "TCAG",
    },
    "RNA": {
        "table": RNA_CODON_TABLE,
        "valid_bases": "AUGC",
        "start": "AUG",
        "stops": ["UAA", "UAG", "UGA"],
        "grid_order": "UCAG",
    },
}


# ---------------------------------------------------------------
# Input functions
# ---------------------------------------------------------------

def clean_sequence(raw):
    """Remove surrounding/inner spaces and convert to uppercase."""
    return raw.strip().replace(" ", "").upper()


def detect_sequence_type(sequence):
    """A sequence containing U is RNA; otherwise it is treated as DNA."""
    if "U" in sequence:
        return "RNA"
    return "DNA"


def find_invalid_base(sequence, valid_bases):
    """Return the first character that is not a valid base (None if all are valid)."""
    for base in sequence:
        if base not in valid_bases:
            return base
    return None


def get_sequence():
    """Keep asking until a valid DNA or RNA sequence is entered.
    Returns (sequence, sequence_type)."""
    while True:
        sequence = clean_sequence(input("Enter a DNA or RNA sequence: "))

        if len(sequence) == 0:
            print("Error: the sequence cannot be empty.")
            continue

        if "T" in sequence and "U" in sequence:
            print("Error: the sequence contains both T and U. Enter either DNA or RNA.")
            continue

        sequence_type = detect_sequence_type(sequence)
        valid_bases = GENETIC_CODES[sequence_type]["valid_bases"]

        bad_base = find_invalid_base(sequence, valid_bases)
        if bad_base is not None:
            print(f"Error: '{bad_base}' is not a valid {sequence_type} nucleotide. "
                  f"Use only {', '.join(valid_bases)}.")
            continue

        return sequence, sequence_type


# ---------------------------------------------------------------
# Analysis functions
# ---------------------------------------------------------------

def split_into_codons(sequence):
    """Split the sequence into full codons. Returns (codons, incomplete_codon)."""
    codons = []
    incomplete_codon = ""
    for i in range(0, len(sequence), 3):
        chunk = sequence[i:i + 3]
        if len(chunk) == 3:
            codons.append(chunk)
        else:
            incomplete_codon = chunk   # leftover 1 or 2 nucleotides
    return codons, incomplete_codon


def translate_codons(codons, table):
    """Translate a list of codons into a list of full amino acid names."""
    amino_acids = []
    for codon in codons:
        short_name = table[codon]                         # e.g. "Met"
        amino_acids.append(AMINO_ACID_NAMES[short_name])  # e.g. "Methionine"
    return amino_acids


def find_start_and_stop(codons, start_codon, stop_codons):
    """Return (start codons found, stop codons found)."""
    found_starts = []
    found_stops = []
    for codon in codons:
        if codon == start_codon:
            found_starts.append(codon)
        if codon in stop_codons:
            found_stops.append(codon)
    return found_starts, found_stops


# ---------------------------------------------------------------
# Output functions
# ---------------------------------------------------------------

def print_results_table(codons, amino_acids, start_codon, stop_codons):
    """Print one row per codon: number, codon, amino acid, type."""
    print()
    print(f"{'No.':<5}{'Codon':<8}{'Amino acid':<18}{'Type':<10}")
    print("-" * 41)

    for number, codon in enumerate(codons, start=1):
        amino_acid = amino_acids[number - 1]
        if codon == start_codon:
            codon_type = "Start"
        elif codon in stop_codons:
            codon_type = "Stop"
        else:
            codon_type = "-"
        print(f"{number:<5}{codon:<8}{amino_acid:<18}{codon_type:<10}")

    print("-" * 41)
    print()


def print_summary(codons, amino_acids, found_starts, found_stops, incomplete_codon):
    """Print the one-line summaries and the incomplete codon note."""
    print("Codons:      ", " - ".join(codons))
    print("Amino acids: ", " - ".join(amino_acids))

    if found_starts:
        print("Start codon: ", " - ".join(found_starts))
    else:
        print("Start codon:  None found")

    if found_stops:
        print("Stop codon:  ", " - ".join(found_stops))
    else:
        print("Stop codon:   None found")

    if incomplete_codon:
        print(f"Note: incomplete codon '{incomplete_codon}' at the end was not translated.")


def print_codon_table(table, grid_order, sequence_type):
    """Print the full 64-codon table as a grid."""
    print()
    print(f"STANDARD CODON TABLE ({sequence_type})")
    print("=" * 57)

    header = "1st   "
    for second in grid_order:
        header += f"{second:<12}"
    header += "3rd"
    print(header)
    print("-" * 57)

    for first in grid_order:
        for third in grid_order:
            if third == grid_order[0]:
                row = f"{first:<6}"      # show the first letter once per block
            else:
                row = " " * 6
            for second in grid_order:
                codon = first + second + third
                row += f"{codon} {table[codon]:<8}"
            row += third
            print(row)
        print("-" * 57)


# ---------------------------------------------------------------
# Main program
# ---------------------------------------------------------------

def main():
    sequence, sequence_type = get_sequence()
    rules = GENETIC_CODES[sequence_type]

    codons, incomplete_codon = split_into_codons(sequence)

    # stop if there is not even one full codon
    if len(codons) == 0:
        print("Error: the sequence is shorter than one codon (3 nucleotides).")
        return

    amino_acids = translate_codons(codons, rules["table"])
    found_starts, found_stops = find_start_and_stop(codons, rules["start"], rules["stops"])

    print(f"Sequence type: {sequence_type}")
    print_results_table(codons, amino_acids, rules["start"], rules["stops"])
    print_summary(codons, amino_acids, found_starts, found_stops, incomplete_codon)
    print_codon_table(rules["table"], rules["grid_order"], sequence_type)


if __name__ == "__main__":
    main()
