import random
word_list = ["apple", "banana", "cantaloupe", "durian", "elderberry", "figs"]

comp_word = random.choice(word_list)
comp_word_blanks = []
print(comp_word)

for a in comp_word:
    comp_word_blanks.append("_")

print(comp_word_blanks)
user_choice = input("Choice?\n")
if user_choice in comp_word:
    print(f"Good guess. There is a '{user_choice}' in the word.")
    for user_choice in comp_word:
        alpha_index = comp_word.index(user_choice)
        print(alpha_index)

print(comp_word_blanks)



