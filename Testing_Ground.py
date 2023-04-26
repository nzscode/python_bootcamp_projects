import random
word_list = ['bob', 'ant', 'pat', 'sam', 'nan']

# comp_word = random.choice(word_list)
# comp_word = comp_word.upper()
# comp_word_blanks = []
# print(comp_word)
#
# total = 5
# for a in comp_word:
#     comp_word_blanks.append("_")
# while total > 0:
#     print(comp_word_blanks)
#     user_choice = input("Choice?\n").upper()
#     if user_choice in comp_word:
#         print(f"Good guess. There is a '{user_choice}' in the word.")
#         for alpha in comp_word:
#             index = comp_word.index(user_choice)
#             comp_word_blanks[index] = user_choice
#     else:
#         print(f'Bad Guess. {user_choice} is not in the word.')
#         total -= 1
#         print(f'You have {total}/5 guesses remaining.')
#
# print(comp_word_blanks)



## Chooses Word
word = random.choice(word_list)
word = word.upper()
print(word)

## Replaces aplphabets of word with blanks
word_blanks = []
for _ in word:
    word_blanks.append('_')
print(word_blanks)

## Asks for user choice
user_choice = (input('What is your choice?\n')).upper()

## for every alphabet in the word, check if the user choice exists
for _ in range(0, len(word)):
    if _ == user_choice:
        alpha_index = word.index(user_choice)
        print(alpha_index)



