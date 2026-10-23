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

# Full names for the 3-letter amino acid codes
amino_acid_names = {
    "Phe": "Phenylalanine", "Leu": "Leucine", "Ile": "Isoleucine",
    "Met": "Methionine", "Val": "Valine", "Ser": "Serine",
    "Pro": "Proline", "Thr": "Threonine", "Ala": "Alanine",
    "Tyr": "Tyrosine", "His": "Histidine", "Gln": "Glutamine",
    "Asn": "Asparagine", "Lys": "Lysine", "Asp": "Aspartic acid",
    "Glu": "Glutamic acid", "Cys": "Cysteine", "Trp": "Tryptophan",
    "Arg": "Arginine", "Gly": "Glycine", "Stop": "Stop",
}


# Step 2: get the DNA sequence from the user
valid_bases = "ATGC"

while True:
    raw_input = input("Enter a DNA sequence: ")
    dna = raw_input.strip().replace(" ", "").upper()    # clean the input
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
incomplete_codon = ""
for i in range(0, len(dna), 3):
    chunk = dna[i:i + 3]
    if len(chunk) == 3:
        codons.append(chunk)
    else:
        incomplete_codon = chunk   # leftover 1 or 2 nucleotides

# stop if there is not even one full codon
if len(codons) == 0:
    raise SystemExit("Error: the sequence is shorter than one codon (3 nucleotides).")

# Step 4: translate each codon
amino_acids = []
for codon in codons:
    short_name = codon_table[codon]                  # e.g. "Met"
    amino_acids.append(amino_acid_names[short_name])  # e.g. "Methionine"
    
# Step 5: identify start and stop codon
start_codon = "ATG"
stop_codons = ["TAA", "TAG", "TGA"]

found_starts = []
found_stops = []
for codon in codons:
    if codon == start_codon:
        found_starts.append(codon)
    if codon in stop_codons:
        found_stops.append(codon)


# Step 6: show the result as a table
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

# Summary lines
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

# Step 7: display the full codon table as a grid
bases = "TCAG"

print()
print("STANDARD CODON TABLE")
print("=" * 57)

header = "1st   "
for second in bases:
    header += f"{second:<12}"
header += "3rd"
print(header)
print("-" * 57)

for first in bases:
    for third in bases:
        if third == "T":
            row = f"{first:<6}"      # show the first letter once per block
        else:
            row = " " * 6
        for second in bases:
            codon = first + second + third
            row += f"{codon} {codon_table[codon]:<8}"
        row += third
        print(row)
    print("-" * 57)
