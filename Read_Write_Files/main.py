name_list = ["Tim", "Bob", " Ray"]
for name in name_list:
    stripped_name = name.strip()
    with open("sample_letter.txt") as sample_letter:
        replaced = sample_letter.read()
        new_letter = replaced.replace("[name]", stripped_name)
        with open(f"{stripped_name}.txt", mode="w") as finished:
            write = finished.write(new_letter)
