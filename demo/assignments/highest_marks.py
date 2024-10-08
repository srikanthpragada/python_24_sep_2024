data = [(1, 50), (2, 60), (1, 70), (2, 80), (3, 50), (3, 20), (1, 60)]

students = {}
for t in data:
    rollno, marks = t
    if rollno in students:
         if marks > students[rollno]:
               students[rollno] = marks
    else:
        students[rollno] =  marks


print(students)
