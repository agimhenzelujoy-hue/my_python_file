students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68]
]

for student in students:
    student_name = student[0]
    scores = student[1:]

    total = 0

    for score in scores:
        total += score

    average = total / len(scores)

    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 45:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade = "F"

    print(student_name, "- Average:", f"{average:.2f}", "- Grade:", grade)