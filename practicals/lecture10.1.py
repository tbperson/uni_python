students = [
("Alice", 20, 85),
("Bob", 22, 72),
("Charlie", 19, 58),
("David", 21, 90),
("Eva", 20, 65)]


def calculate_average_grade(students):
    total_grade = 0
    for student in students:
        total_grade += student[2]
    average_grade = total_grade / len(students)
    print(f"Average grade: {average_grade}")

def calculate_highest_grade(students):
    highest_grade = 0
    for student in students:
        if student[2] > highest_grade:
            student[2] = highest_grade
    print(f"Highest grade is{highest_grade}")        

def passing_students():
    pass_mark = 65
    passing_students = []
    for student in students:
        if student[2] >= 65:
            passing_students.append(student[1])
    for student in passing_students:
        print(f"Student {student} passed")