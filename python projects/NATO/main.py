# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
import os

# Resolve path relative to this script
current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, "nato_phonetic_alphabet.csv")
data = pandas.read_csv(csv_path)
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
