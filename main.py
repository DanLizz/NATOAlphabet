import pandas as pd

word_data = pd.read_csv('nato_phonetic_alphabet.csv', index_col=0, squeeze=True).to_dict()


def generate_phonectic():
    word = input("Enter a word: ").upper()
    try:
        code = [word_data[letter] for letter in word]
    except KeyError:
        print("Sorry, input alphabets only")
        generate_phonectic()
    else:
        print(code)


generate_phonectic()
