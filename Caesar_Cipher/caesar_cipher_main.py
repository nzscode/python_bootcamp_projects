alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

repeat = True
def go_again():
    global repeat
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").title()
    if again == "Yes":
        cipher()
    elif again == "No":
        repeat = False
    else:
        print("Please choose a valid response.")
        go_again()

def cipher():
    coded_message = ""
    global repeat
    while repeat:
        encryption = input("Type 'encode' to encrypt, type 'decode' to decrypt.\n").title()
        if encryption == "Encode":
            message = input("What is your message:\n")
            shift = int(input("Type the shift number.\n"))
            for i in range(len(message)):
                if message[i] in alphabets:
                    alphabet_index = alphabets.index(message[i])
                    new_alphabet = alphabets[alphabet_index + 5]
                    coded_message += new_alphabet
                else:
                    coded_message += message[i]
            print(f"Here's the encoded result:\n{coded_message}\n\n")
        elif encryption == "Decode":
            message = input("What is your message:\n")
            shift = int(input("Type the shift number.\n"))
            for i in range(len(message)):
                if message[i] in alphabets:
                    alphabet_index = alphabets.index(message[i])
                    new_alphabet = alphabets[alphabet_index - 5]
                    coded_message += new_alphabet
                else:
                    coded_message += message[i]
            print(f"Here's the decoded result:\n{coded_message}\n")
        else:
            print("Please choose a valid response.")
            cipher()


        go_again()

cipher()