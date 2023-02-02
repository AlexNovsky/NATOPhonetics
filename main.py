import pandas

# creating a dictionary from CSV file
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# Creatingalexa a list of the phonetic code words from a word that the user inputs.
word = input("Enter your word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)