from classes.studentid import Student

students = []
for i in range(5):
    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Student Course: ")
    student = Student(id, name, course, -1)
    students.append(student)

print(students[0])
if students[0].setMark(int(input("Enter Student Mark: "))):
    print("Mark set")
else:
    print("Mark not set")

for student in students:
    student.printGrade()
