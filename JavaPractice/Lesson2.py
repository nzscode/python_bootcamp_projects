import math

print("Variables: Lesson 2.1")
points = 0

print("Harry was caught wandering the halls. -50 points for Gryffindor")
points -= 50
print("Harry was being cheeky in class. -3 points for Gryffindor")
points -= 3
print("Hermione got full marks on Lockhart's quiz. 30 points for Gryffindor")
points += 30
print("Ron won the underground chess game. 100 points for Gryffindor")
points += 100
print("Harry defeated Quirrell. 60 points for Gryffindor")
points += 60
print(f"Points: {points}")

print("Variables: Lesson 2.2")

name = "Noor"
age = 38
country = "Canada"
hours = 5
sport = "Reading"
game = "Stardew Valley"
subject = "Language"
grade = 98

print(f"My name is {name}. I'm {age} years old, and I'm from {country}.")
print(f"My favourite sport is {sport}. I play for {hours} hours a day")
print(f"When I'm tired, I like to play {game}.")
print(f"In school, my favourite subject was {subject}, I scored a {grade}.")

print("Variables: Lesson 2.3")

num_of_apples = 0
num_of_customers = 0
profit = 0

print("You picked 500 apples from an apple orchard")
num_of_apples += 500
print("Time for business! You're selling each apple for 40 cents")
print("One customer walked in. He bought 4 apples!")
num_of_apples -= 4
num_of_customers += 1
profit += (4 * 0.40)
print("Another customer walked in. He bought 20 apples!")
num_of_apples -= 20
num_of_customers += 1
profit += (20 * 0.40)
print("Another customer walked in. She bought 200 apples!")
num_of_apples -= 200
num_of_customers += 1
profit += (200 * 0.40)
print(f"Wow! So far, you made: ${profit}.")
print(f"{num_of_customers} customers love your apples.")
print(f"You have {num_of_apples} apples left. We'll sell more tomorrow.")

print("Variables: Lesson 2.4")
sales = 24309.65
profit = 18562.18
refunds = 688.78
shipping = 1233.57

print(f"This month, we made ${math.floor(sales)} in sales")
print(f"Factoring in costs, we made ${math.floor(profit)} in profit")
print(f"The refunds are at a low ${math.floor(refunds)}. This is a good sign!")
print(f"Shipping costs were high. We paid ${math.floor(shipping)} in shipping")

print("Variables: Lesson 2.5")
print("Welcome to JavaGram! Let's sign you up.")

# firstName = input("What is your first name?\n")
firstName = "Noor"
# lastName = input("What is your last name?\n")
lastName = "Zaq"
# javagramAge = input("How old are you?\n")
javagramAge = 38
# userName = input("Make a username\n")
userName = "sdfsf"
# city = input("What city do you live in?\n")
city = "Ajax"
# javagramCountry = input("What country is that?\n")
javagramCountry = "Canada"


print("Thank you for joining JavaGram!")
print("\nHere is the information you entered:")
print(f"\tFirst Name: {firstName}")
print(f"\tLast Name: {lastName}")
print(f"\tAge: {javagramAge}")
print(f"\tUsername: {userName}")
print(f"\tCity: {city}")
print(f"\tCountry: {javagramCountry}")

print("Variables: Challenge")
chatBotName = input("Hello. What is your name?\n")
chatBotCity = input(f"\nHi {chatBotName}! I'm Javabot. Where are you from?\n")
print(f"\nI hear it's beautiful at {chatBotCity}! I'm from a place called Oracle")
chatBotAge = input("How old are you?\n")
print(f"\nSo you're {chatBotAge}, cool! I'm 400 years old.")
new_age = 400/int(chatBotAge)
print(f"This means I'm {math.floor(new_age)} times older than you.")
chtBotLanguage = input("Enough about me. What's your favourite language? (just don't say Java)\n")
print(f"\n{chtBotLanguage}, that's great! Nice chatting with you {chatBotName}. I have to log off now. See ya!")
