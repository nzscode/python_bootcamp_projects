student = {
    "Name": "Jane",
    "Age": 19,
    "Courses": ["Math", "English"],
}

print(student) #Accessing dictionary
print(student["Name"]) # Accessing value of the key "Name"
# print(student["Hobbies"]) #Throws key error
student["phone"] = "111-222-3333" #Adding new key:value pair to dictionary
student["Age"] = 27 #Updates value
# student.update({"Name": "Janet", "Age": 15, "Courses": ["French"]}) #Updates multiple key/vaue pairs
del student["Age"] #Deletes a key and it's value
# newCourse = student.pop("Courses") Removes key and saves it in new variable
print(student.values()) #Returns the values only
print(student.keys()) # Returns the keys only
print(student.items()) # Returns key/Value pairs

#To loop through keys
for key in student:
    print(key)

#To loop through keys
for key, value in student.items():
    print(f"{key} : {value}")
print(15+5+(3*2)/4**2+(3-7)*7)




