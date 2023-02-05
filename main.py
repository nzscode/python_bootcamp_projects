import random
import pygame

names = ["Tom", "Ron", "Bob", "Jane"]
student_scores = {student: random.randint(1, 100) for student in names}

for key in student_scores:
    print(student_scores.fromkeys(key))