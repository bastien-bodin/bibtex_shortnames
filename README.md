# Journal Name Abbreviator for BibTeX Files

A Python script to automatically abbreviate journal names in `.bib` files according to the [List of Title Word Abbreviations](https://www.issn.org/services/online-services/access-to-the-ltwa/) (based on the ISO 4 standard).

---

# Features
- Reads a `.bib` file and identifies journal names in `journal = {...}` fields.
- Abbreviates each word in the journal name using a predefined dictionary (based on ISO 4).
- Preserves punctuation, spaces, and delimiters (e.g., hyphens, slashes).
- Writes the abbreviated entries to a new `.bib` file.
- Handles common academic journal terms (e.g., "Journal" → "J.", "Science" → "Sci.").



# Requirements
- Python 3.x
- No external libraries required (uses built-in `re` and `sys`).

---

# Usage

## Run the Script
```bash
python abbreviate_journal_names.py <input_file.bib> <output_file.bib>
```
- `<input_file.bib>`:  Path to your input `.bib` file.
- `<output_file.bib>`: Path for the output `.bib` file with abbreviated journal names.

## Example
```bash
python abbreviate_journal_names.py references.bib references_abbreviated.bib
```
This will create a new file, references_abbreviated.bib, with abbreviated journal names.

---

# How it works
1. The script reads the input `.bib` file line by line.
2. For each line containing a `journal = {...}` field, it splits the journal name into words and abbreviates them using the predefined dictionary.
3. Words not found in the dictionary remain unchanged.
4. The modified entries are written to the output file.

---

# Customization
- *Extend the dictionary*: Add more words and their abbreviations to the `word_abbreviations` dictionary in the script to cover additional journals.

---

# License
This script is open-source and free to use. Modify and distribute as needed.
