data = [(1, 50), (2, 60), (1, 70), (2, 80), (3, 50), (3, 20), (1, 60)]

students = {}
for t in data:
    rollno, marks = t
    total = students.get(rollno, 0) + marks
    students[rollno] = total


print(students)
