import pandas

nato_data_frame = pandas.read_csv("NATO_Alphabet/nato_phonetic_alphabet.csv")
continue_translating = True
translation = []


def translate():
    user_input = input("What is your word? \n").upper().strip()
    for char in user_input:
        for (index, row) in nato_data_frame.iterrows():
            if row.letter == char:
                # print(row.code)
                translation.append(row.code)
    print(translation)


def translate_again():
    global continue_translating
    user_response = input("Would you like to translate another word? Y or N\n").upper().strip()
    if user_response == "N":
        continue_translating = False
    elif user_response != "Y":
        print("Sorry, please choose a valid response. Y or N.")
        translate_again()


while continue_translating:
    translate()
    translate_again()
