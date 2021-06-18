import pandas as pd

#TODO 1. Create a dictionary in this format:

word_data = pd.read_csv('nato_phonetic_alphabet.csv', index_col=0, squeeze=True).to_dict()

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
code = [word_data[letter] for letter in word]
print(code)
