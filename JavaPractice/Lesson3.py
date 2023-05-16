print("Booleans & Conditionals: Lesson 3.7")
print("\n****ROYAL BANK OF JAVA****")
# decision = input("Are you here to get a mortgage? (yes or no)\n").lower()
decision = "yes"
match decision:
    case "yes":
        print("Great!")
        # savings = int(input("How much money do you have in your savings?\n"))
        savings = 10000
        # debt = int(input("And, how much do you owe in credit card debt?\n"))
        debt = 5000
        # years = int(input("How many years have you worked for?\n"))
        years = 3
        # name = input("What is your name?\n")
        name = "Noor"
        if savings >= 10000 and debt < 5000 and years > 2:
            print(f"Congratulations {name} You have been approved!")
        else:
            print(f"Sorry {name}, you are not eligible for a mortgage.")
    case default:
        print("OK, Have a nice day.")

print("\n\n\nBooleans & Conditionals: Challenge")
score = 0
question1 = input("1. Which country held the 2016 Summer Olympics?\na) China\nb) Ireland\nc) Brazil\nd) Italy\n").lower()
question2 = input("2. Which planet is the hottest?\na) Venus\nb) Saturn\nc) Mercury\nd) Mars\n").lower()
question3 = input("3. What is the rarest blood type?\na) O\nb) A\nc) B\nd) AB-Negative\n").lower()
question4 = input("4. Which one of these characters is friends with Harry Potter?"
                  "\na) Ron Weasley\nb) Hermione Granger\nc) Draco Malfoy\nd) A & B\n").lower()
if question1 == "c":
    score += 5

if question2 == "a":
    score += 5

if question3 == "d":
    score += 5

if question4 == "d":
    score += 5

print(f"Your final score is: {score}/20")

if score > 15:
    print("Wow, you know your stuff!")
elif 15 > score > 5:
    print ("Not bad!")
else:
    print("Better luck next time.")
