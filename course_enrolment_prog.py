# Online Course Enrollment System
# Author: Python Programmer
# Version: 1.0

def initialize_courses():
    """Initialize and return the courses dictionary"""
    return {
        "Python": {"seats": 5, "students": []},
        "AI": {"seats": 3, "students": []},
        "Data Science": {"seats": 4, "students": []},
        "Web Development": {"seats": 6, "students": []}
    }

def display_welcome():
    """Display the welcome message"""
    print("\nWelcome to Online Course Enrollment System")
    print("-----------------------------------------")

def display_menu():
    """Display the main menu options"""
    print("\nMain Menu:")
    print("1. View Available Courses")
    print("2. Enroll Student")
    print("3. Drop Course")
    print("4. View Enrolled Students")
    print("5. Exit")

def view_courses(courses):
    """Display available courses with seat information"""
    print("\nAvailable Courses:")
    for course, details in courses.items():
        available_seats = details["seats"] - len(details["students"])
        print(f"{course} - Seats Left: {available_seats}")

def enroll_student(courses):
    """Handle student enrollment process"""
    print("\nEnroll Student")
    view_courses(courses)
    
    course = input("\nEnter course name: ")
    if course not in courses:
        print("Course not found!")
        return
    
    available_seats = courses[course]["seats"] - len(courses[course]["students"])
    if available_seats <= 0:
        print("Course is full!")
        return
    
    student_name = input("Enter student name: ").strip()
    if not student_name:
        print("Student name cannot be empty!")
        return
    
    if student_name in courses[course]["students"]:
        print("Student already enrolled in this course!")
        return
    
    courses[course]["students"].append(student_name)
    print(f"{student_name} enrolled in {course}")

def drop_course(courses):
    """Handle course dropping process"""
    print("\nDrop Course")
    course = input("Enter course name: ")
    if course not in courses:
        print("Course not found!")
        return
    
    if not courses[course]["students"]:
        print("No students enrolled in this course!")
        return
    
    student_name = input("Enter student name to drop: ").strip()
    if not student_name:
        print("Student name cannot be empty!")
        return
    
    if student_name in courses[course]["students"]:
        courses[course]["students"].remove(student_name)
        print(f"{student_name} dropped from {course}")
    else:
        print("Student not found in this course!")

def view_enrolled_students(courses):
    """Display enrolled students for a course"""
    print("\nView Enrolled Students")
    course = input("Enter course name: ")
    if course not in courses:
        print("Course not found!")
        return
    
    if not courses[course]["students"]:
        print(f"No students enrolled in {course} yet!")
    else:
        print(f"\nEnrolled Students in {course}: {courses[course]['students']}")

def main():
    """Main function to run the enrollment system"""
    courses = initialize_courses()
    display_welcome()
    
    while True:
        display_menu()
        
        try:
            option = int(input("\nChoose option (1-5): "))
            
            if option == 1:
                view_courses(courses)
            elif option == 2:
                enroll_student(courses)
            elif option == 3:
                drop_course(courses)
            elif option == 4:
                view_enrolled_students(courses)
            elif option == 5:
                print("\nThank you for using the Online Course Enrollment System. Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1-5.")
                
        except ValueError:
            print("Please enter a valid number (1-5)!")

if __name__ == "__main__":
    main()