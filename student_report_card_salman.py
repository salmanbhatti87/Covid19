# Student Report Card Generator

students = {}

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def add_student():
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()

    marks = []
    for i in range(1, 6):
        while True:
            try:
                mark = int(input(f"Enter marks for Subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("❌ Marks must be between 0 and 100.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
    
    students[name] = {
        "roll": roll,
        "marks": marks
    }
    print(f"✅ Record added for {name}.\n")

def generate_report_card(name):
    if name not in students:
        print("❌ Student not found.\n")
        return

    data = students[name]
    marks = data["marks"]
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    print("\n📄 Report Card")
    print(f"Student Name: {name}")
    print(f"Roll No: {data['roll']}")
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}\n")

def view_all_students():
    if not students:
        print("📂 No student records available.\n")
        return
    for name in students:
        generate_report_card(name)

def main():
    print("📘 Welcome to the Student Report Card Generator")
    while True:
        print("\n1. Add Student\n2. View Report Card\n3. View All Students\n4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            name = input("Enter student name to view report: ").strip()
            generate_report_card(name)
        elif choice == '3':
            view_all_students()
        elif choice == '4':
            print("👋 Thank you for using the Report Card Generator!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
