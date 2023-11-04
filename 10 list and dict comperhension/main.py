import random

names = ["zale", "saloka", "messi", "harzato", "gilang"]

student_score = { student:random.randint(50,100) for student in names}

print(student_score)

passed_student = { student:score for (student,score)in student_score.items() if score >= 70  }
print(passed_student)

