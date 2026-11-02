
students = [
    {"name": "Rahul","marks":[67,34,89] },
    {"name": "Aditya","marks":[78,66,90] },
    {"name": "Rahul","marks":[34,54,66] },
]



def add_student():
    name = input("Enter the student name: ")

    marks = []

    for i in range(3):
        mark = int(input(f"Enter the marks for subject {i + 1}: "))
        marks.append(mark)

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")
    print(students)


def calculate_average(marks):
    average = sum(marks) / len(marks)
    return average


def display_students():
    for student in students:
        average = calculate_average(student["marks"])
        print(f"Name: {student['name']}")
        print(f"Marks: {student['marks']}")
        print(f"Average: {average:.2f}")
        print("*" * 30)


add_student()


print(calculate_average(students[0]["marks"]))


display_students()
