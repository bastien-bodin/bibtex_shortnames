import re
import sys

def abbreviate_journal_names(input_file, output_file):
    """
    Reads a .bib file, abbreviates journal names word-by-word, and
    writes the output to a new .bib file.
    Args:
        input_file (str): The path to the input .bib file.
        output_file (str): The path for the output .bib file.
    """
    # Dictionary of common words and their abbreviations according to ISO 4 standard.
    # This list can be expanded if necessary.
    word_abbreviations = {
        "journal": "J.",
        "of": "of",
        "the": "the",
        "and": "and",
        "on": "on",
        "in": "in",
        "for": "for",
        "a": "a",
        "an": "an",
        "the": "the",
        "society": "Soc.",
        "series": "Ser.",
        "proceedings": "Proc.",
        "international": "Int.",
        "european": "Eur.",
        "american": "Am.",
        "royal": "R.",
        "national": "Natl.",
        "academy": "Acad.",
        "sciences": "Sci.",
        "sci": "Sci.",
        "research": "Res.",
        "physics": "Phys.",
        "physical": "Phys.",
        "fluids": "Fluids",
        "astronomy": "Astron.",
        "astrophysics": "Astrophys.",
        "volcanology": "Volcanol.",
        "geothermal": "Geotherm.",
        "applied": "Appl.",
        "appl": "Appl.",
        "mechanics": "Mech.",
        "civil": "Civ.",
        "geophysical": "Geophys.",
        "letters": "Lett.",
        "lett": "Lett.",
        "review": "Rev.",
        "rev": "Rev.",
        "reviews": "Rev.",
        "communications": "Commun.",
        "geoscience": "Geosci.",
        "planets": "Planets",
        "planetary": "Planet.",
        "space": "Space",
        "science": "Sci.",
        "volcano": "Volc.",
        "materials": "Mater.",
        "biomedical": "Biomed.",
        "optics": "Opt.",
        "astronomical": "Astron.",
        "comptes": "C.",
        "rendus": "R.",
        "physique": "Phys.",
        "statistical": "Stat.",
        "stat": "Stat.",
        "theory": "Theor.",
        "theor": "Theor.",
        "experiment": "Exp.",
        "exp": "Exp.",
        "mathematical": "Math.",
        "modelling": "Model.",
        "pure": "Pure",
        "chemistry": "Chem.",
        "philosophical": "Philos.",
        "magazine": "Mag.",
        "cryosphere": "Cryosphere",
        "europhysics": "Europhys.",
        "british": "Brit.",
        "remote": "Remote",
        "sensing": "Sens.",
        "hydrological": "Hydrol.",
        "processes": "Process.",
        "nature": "Nature",
        "le": "Le",
        "de": "de",
        "colloques": "Colloques",
        "annual": "Annu.",
        "earth": "Earth",
        "glaciology": "Glaciol.",
        "moon": "Moon",
        "eos": "Eos",
        "transactions": "Trans.",
        "union": "Union",
        "chemical": "Chem.",
        "reference": "Ref.",
        "data": "Data",
        "oceans": "Oceans",
        "solid": "Solid",
        "advances": "Adv.",
        "computational": "Comput.",
        "particle": "Part.",
        "numerical": "Numer.",
        "methods": "Methods",
        "bauzeitung": "Bauztg.",
        "acoustical": "Acoust.",
        "heat": "Heat",
        "mass": "Mass",
        "transfer": "Transfer",
        "scientific": "Sci.",
        "brief": "Brief",
        "hydrodynamics": "Hydrodyn."
    }
    modified_lines = []
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                journal_match = re.search(r'journal\s*=\s*{(.+?)}', line, re.IGNORECASE)
                if journal_match:
                    full_name = journal_match.group(1).strip()

                    # Split the journal name into words while preserving spaces and delimiters
                    words_and_separators = re.split(r'(\s+|[-/])', full_name)

                    abbreviated_parts = []
                    for part in words_and_separators:
                        # Check if the word is in the dictionary (case-insensitive) and remove punctuation
                        lower_part = re.sub(r'[.,;:]', '', part.lower())
                        if lower_part in word_abbreviations:
                            abbreviated_parts.append(word_abbreviations[lower_part])
                        else:
                            # If a word is not found, keep it as is
                            abbreviated_parts.append(part)
                    abbreviated_name = "".join(abbreviated_parts)
                    new_line = line.replace(full_name, abbreviated_name)
                    modified_lines.append(new_line)
                else:
                    # If the line does not contain a journal field, keep it as is
                    modified_lines.append(line)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    # Write the modified content to the new file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)
        print(f"Journal names have been successfully abbreviated. The new file is saved as '{output_file}'.")
    except Exception as e:
        print(f"Error writing the file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python abbreviate_bib.py <input_file.bib> <output_file.bib>")
    else:
        input_bib = sys.argv[1]
        output_bib = sys.argv[2]
        abbreviate_journal_names(input_bib, output_bib)
