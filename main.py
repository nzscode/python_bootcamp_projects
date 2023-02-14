student_dict = {
    "student": ["Jane", "Harry", "Sam", "Yanni", "Bella"],
    "score": [85, 59, 72, 91, 23]
}

# for (key, value) in student_dict.items():
#   print(value)
import pandas

# Creating a new Dataframe from student_dict
nato_alphas = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(student_data)

# Looping through a dataframe
# for (key, value) in student_data.items():
#     print(value)

# Looping through rows of dataframe
# word = "cat"
# for (index, row) in nato_alphas.iterrows():
#     for char in word.upper():
#         if row.letter == char:
#             print(row.code)
keep_translating = True

def translate():
    word = input("What word do you want to convert? \n").upper().strip()
    char_list = [char for char in word]
    print(char_list)
    result = {row.letter: row.code for char in word for (index, row) in nato_alphas.iterrows() if row.letter == char}
    print(result)


def continue_translating():
    global keep_translating
    cont_translating = input("Continue? Y/N\n").upper().strip()
    if cont_translating == "N":
        keep_translating = False
    elif cont_translating != "Y":
        print("Please choose a valid answer: ")
        continue_translating()




while keep_translating:
    translate()
    continue_translating()
    # word = input("What word do you want to convert? \n").upper().strip()
    # char_list = [char for char in word]
    # print(char_list)
    #
    # result = {row.letter: row.code for char in word for (index, row) in nato_alphas.iterrows() if row.letter == char}
    # # result = {row.letter: row.code for (index, row) in nato_alphas.iterrows() for char in word if row.letter == char}
    # # result = {row.letter: row.code for (index, row) in nato_alphas.iterrows() if row.letter == char_list}
    #
    # print(result)

    # continue_translating = input("Continue? Y/N\n").upper().strip()
    # if continue_translating == "N":
    #     keep_translating = False
    # elif continue_translating != "Y":
    #     print("Please choose a valid answer: ")

# nato_data = pandas.DataFrame("na")
word = input("What is your word? \n")
char = [char for char in word]

for (index, row) in nato_alphas.iterrows():
    if row.letter == char:
        print(row.code)