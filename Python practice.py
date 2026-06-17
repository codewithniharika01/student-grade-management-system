students_grades = {}

def add_student(name, grade):
    students_grades[name] = grade
    print(f"{name} added with grade {grade}")

def update_grade(name, grade):
    if name in students_grades:
        students_grades[name] = grade
        print(f"{name}'s grade updated to {grade}")
    else:
        print(f"{name} not found")

def delete_student(name):
    if name in students_grades:
        del students_grades[name]
        print(f"{name} deleted successfully")
    else:
        print(f"{name} not found")

def display_all_students():
    if students_grades:
        print("\nStudent Records:")
        for name, grade in students_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No students found")

def main():
    while True:
        print("\n===== Student Grade Management System =====")
        print("1. Add Student")
        print("2. Update Grade")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Enter student name: ")
                grade = int(input("Enter student grade: "))
                add_student(name, grade)

            elif choice == 2:
                name = input("Enter student name: ")
                grade = int(input("Enter new grade: "))
                update_grade(name, grade)

            elif choice == 3:
                name = input("Enter student name: ")
                delete_student(name)

            elif choice == 4:
                display_all_students()

            elif choice == 5:
                print("Program Closed")
                break

            else:
                print("Invalid Choice")

        except ValueError:
            print("Please enter a valid number")

main()