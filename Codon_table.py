# Codon Table Generator
# Translates a DNA sequence into amino acids using the standard genetic code.

# Step 1: dictionary of all 64 codons -> amino acids
codon_table = {
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

# Step 2: get the DNA sequence from the user
valid_bases = "ATGC"

while True:
    dna = input("Enter a DNA sequence: ")
    is_valid = True

    if len(dna) == 0:
        print("Error: the sequence cannot be empty.")
        is_valid = False

    for base in dna:
        if base not in valid_bases:
            print(f"Error: '{base}' is not a valid DNA nucleotide. Use only A, T, G, C.")
            is_valid = False
            break

    if is_valid:
        break

# Step 3: split into codons (groups of 3)
codons = []
for i in range(0, len(dna), 3):
    codons.append(dna[i:i + 3])

# Step 4: translate each codon
amino_acids = []
for codon in codons:
    amino_acids.append(codon_table[codon])

# Step 5: show the result
print("Codons:      ", " - ".join(codons))
print("Amino acids: ", " - ".join(amino_acids))
