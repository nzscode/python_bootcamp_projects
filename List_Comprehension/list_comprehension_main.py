with open("List_Comprehension/file1.txt", "r") as file1:
    lines1 = file1.readlines()

with open("List_Comprehension/file2.txt", "r") as file2:
    lines2 = file2.readlines()

# new_lines1 = [line1 for line1 in lines1]
# new_lines2 = [line2 for line2 in lines2]
new_linus = [int(line1) for line1 in lines1 for line2 in lines2 if line1 == line2]

new_linusa = [int(line1) for line1 in lines1 if line1 in lines2]

new_lines = []
for line1 in lines1:
    for line2 in lines2:
        if line1 == line2:
            new_lines.append(int(line1))

print(new_linusa)