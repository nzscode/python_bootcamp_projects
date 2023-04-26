import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

input_letters = int(input("How many letters should your password have?  \n"))
input_numbers = int(input("How many numbers should your password have?  \n"))
input_symbols = int(input("How many symbols should your password have?  \n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
new_pw = ""
for letter in range(0, input_letters):
  alphas = letters[random.randint(0, len(letters)-1)]
  new_pw += alphas

for symbol in range(0, input_symbols):
  syms = symbols[random.randint(0, len(symbols)-1)]
  new_pw += syms

for num in range(0, input_numbers):
  nums = numbers[random.randint(0, len(numbers)-1)]
  new_pw += nums

print(f"Your new password is {new_pw}.")