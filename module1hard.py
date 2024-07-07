# 7.07

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
print("Do you wish to add a student's info to the journal?(y/n)")
add_student = input()
if add_student == 'y':
    print("Write student's name")
    a_student = input()
    a_student = a_student.title()
    students.append(a_student)
    students.sort(key=str.lower)
    print("Write student's grades (on a scale of 1 to 5), use space between them")
    a_grade = input()
    a_grade = list(map(int, a_grade.split()))
    grades.insert(students.index(a_student), a_grade)
else:
    students.sort(key=str.lower)
for i in range(len(grades)):
    grades[i] = (sum(grades[i]) / len(grades[i]))
students_average_score = dict(zip(students, grades))
print(students_average_score)
