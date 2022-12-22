class LoveCalculator:
    def __init__(self):
        print("Welcome to the Love Calculator.")

    def true_love_calculation(self):
        first_name = input("What is the name of the first person?  \n").lower()
        second_name = input("What is the name of the second person?  \n").lower()
        true = ["t", "r", "u", "e"]
        love = ["l", "o", "v", "e"]
        true_score = 0
        love_score = 0

        for char in first_name:
            if char in true:
                true_score += 1

        for char in first_name:
            if char in love:
                love_score += 1

        for char in second_name:
            if char in true:
                true_score += 1

        for char in second_name:
            if char in love:
                love_score += 1

        true_love_score = str(true_score) + str(love_score)
        return true_love_score

    def love_level(self, score):
        score = int(score)
        if score < 10 or score > 90:
            print(f"Your score is {score}, you go together like coke and mentos.")
        elif 40 < score < 50:
            print(f"Your score is {score}, you are alright together.")
        else:
            print(f"Your score is {score}.")