# Python_Project
This code has code for developing a codon table generator

# Codon Table Generator

A Python program that builds the standard genetic code (all 64 codons) and translates a DNA or RNA sequence into amino acids.

## Features

- Dictionary of all 64 codons and their amino acids
- Accepts a DNA sequence (A, T, G, C) or an RNA sequence (A, U, G, C)
- Cleans the input (removes spaces, converts to uppercase)
- Validates the input and asks again if it contains invalid characters
- Splits the sequence into codons and translates each one
- Identifies start codon (ATG / AUG) and stop codons (TAA, TAG, TGA / UAA, UAG, UGA)
- Handles an incomplete codon at the end of the sequence
- Prints the results as a table and displays the full 64-codon grid
- `compare_tables.py` checks the codon table against the NCBI standard genetic code and Biopython

## How to run

```bash
python codon_table.py
```

Example (DNA):

```
Enter a DNA or RNA sequence: ATGGCTTTTTAA

No.  Codon   Amino acid        Type
-----------------------------------------
1    ATG     Methionine        Start
2    GCT     Alanine           -
3    TTT     Phenylalanine     -
4    TAA     Stop              Stop
-----------------------------------------

Codons:       ATG - GCT - TTT - TAA
Amino acids:  Methionine - Alanine - Phenylalanine - Stop
Start codon:  ATG
Stop codon:   TAA
```

An RNA sequence such as `AUGGCUUUUUAA` gives the same amino acids with U-codons (AUG - GCU - UUU - UAA).

## Compare with reference tables

```bash
pip install biopython      # optional, only needed for the Biopython comparison
python compare_tables.py
```

To compare with a codon table from a GitHub repository, copy its dictionary into a file called `github_table.py` and name it `GITHUB_TABLE` (DNA codons with T, amino acids as 3-letter codes such as `"Phe"`).

## Files

| File | Purpose |
|---|---|
| `codon_table.py` | Main program |
| `compare_tables.py` | Compares our codon table with NCBI / Biopython / GitHub tables |
| `README.md` | Project description |

## Concepts used

Dictionaries, loops, conditional statements, string manipulation, input validation, functions, and basic biological sequence analysis.
