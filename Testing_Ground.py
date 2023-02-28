# import pandas
#
# nato_data_frame = pandas.read_csv("NATO_Alphabet/nato_phonetic_alphabet.csv")
# continue_translating = True
# translation = []
#
#
# def translate():
#     user_input = input("What is your word? \n").upper().strip()
#     for char in user_input:
#         for (index, row) in nato_data_frame.iterrows():
#             if row.letter == char:
#                 # print(row.code)
#                 translation.append(row.code)
#     print(translation)
#
#
# def translate_again():
#     global continue_translating
#     user_response = input("Would you like to translate another word? Y or N\n").upper().strip()
#     if user_response == "N":
#         continue_translating = False
#     elif user_response != "Y":
#         print("Sorry, please choose a valid response. Y or N.")
#         translate_again()
#
#
# while continue_translating:
#     translate()
#     translate_again()


# Use a nested list comprehension to find all of the numbers from 1–1000
# that are divisible by any single digit besides 1 (2–9)
dividers = [2, 3, 4, 5, 6, 7, 8, 9]
nums = [num for num in range(1, 21) for div in dividers if num % div == 0]
print(nums)

new_i_list = []
for i in range(20, 31):
    string_i = str(i)
    str_i_sum = int(string_i[0]) + int(string_i[1])
    if str_i_sum % 2 == 0:
        new_i_list.append(i)
print(new_i_list)

new_j_list = [j for j in range(20, 31) if (int(str(j)[0]) + int(str(j)[1])) % 2 != 0]
print(new_j_list)

