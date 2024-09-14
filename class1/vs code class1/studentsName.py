# Sample data
student_grades = {
    "John": "A",
    "Emma": "B",
    "Michael": "C",
    "Sophia": "A",
    "William": "B"
}

# Ask for student's name
student_name = input("Enter student's name: ")

# Check if the student's name is in the dictionary
if student_name in student_grades:
    grade = student_grades[student_name]
    print(f"Grade for {student_name}: {grade}")
else:
    print("Student not found.")