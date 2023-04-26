import random
from Hangman.Hangman_stages import stages
from Hangman.Hangman_words import word_list

word = random.choice(word_list)
word = word.upper()
print(word)

word_blanks = []
for _ in range(len(word)):
    word_blanks.append('_')
print(word_blanks)

tries = 7
game_over = False
guessed = []
def guess():
    global tries
    global game_over
    while not game_over:
        user_choice = (input('What is your choice?\n')).upper()
        if user_choice in word:
            for i in range(len(word)):
                if word[i] == user_choice:
                    word_blanks[i] = user_choice
            print(word_blanks)
        elif user_choice in guessed:
            print("You've already guessed that")
        else:
            guessed.append(user_choice)
            tries -= 1
            print(f'You have {tries}/7 tries left.')
            print(stages[tries])
            print(word_blanks)
        if tries < 1:
            print(f'Too bad, the word was:{word}')
            game_over = True
        elif "_" not in word_blanks:
            print(f'Good job you guessed the whole word!')
            game_over = True

guess()