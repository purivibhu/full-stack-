def main():
    student_grades = {}

    while True:
        print("\nOptions:")
        print("1. Add student and grades")
        print("2. Add more grades for existing student")
        print("3. Display grades for a student")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter student's name: ")
            grades = input("Enter grades separated by commas: ")
            student_grades[name] = [float(grade) for grade in grades.split(',')]
            print(f"Added {name} with grades: {student_grades[name]}")

        elif choice == '2':
            name = input("Enter student's name: ")
            if name in student_grades:
                grades = input("Enter additional grades separated by commas: ")
                student_grades[name].extend(float(grade) for grade in grades.split(','))
                print(f"Updated {name}'s grades: {student_grades[name]}")
            else:
                print("Student not found.")

        elif choice == '3':
            name = input("Enter student's name: ")
            if name in student_grades:
                print(f"{name}'s grades: {student_grades[name]}")
            else:
                print("Student not found.")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()