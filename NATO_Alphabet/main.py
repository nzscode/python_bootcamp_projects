import pandas
data = pandas.read_csv("NATO_Alphabet/nato_phonetic_alphabet.csv")
nato_alphas = dict((row.letter, row.code) for index, row in data.iterrows())
user_input = input("What is your word? \n").upper().strip()
input_list = [char for char in user_input]
translate = [nato_alphas[letter] for letter in input_list if letter in nato_alphas.keys()]
print(translate)