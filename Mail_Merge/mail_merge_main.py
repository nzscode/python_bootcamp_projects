# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Mail_Merge/Input/Names/invited_names.txt") as name_list:
    for n in name_list:
        n_stripped = n.strip()
        with open("Mail_Merge/Input/Letters/starting_letter.txt") as letter_template:
            new_letter = letter_template.read()
            new_name = new_letter.replace("[name]", f"{n_stripped}")
            with open(f"Mail_Merge/Output/ReadyToSend/{n_stripped}.txt", mode="w") as finished_letter:
                write = finished_letter.write(new_name)



