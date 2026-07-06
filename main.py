from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook


def display_menu():
    print("\n" + "=" * 45)
    print("🎓 Student Gradebook Management System")
    print("=" * 45)
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. Add Assessment")
    print("5. Record Grade")
    print("6. Search Student")
    print("7. Show Student Report")
    print("8. Delete Student")
    print("9. Exit")


gradebook = Gradebook()

while True:
    display_menu()

    choice = input("\n👉 Enter your choice (1-9): ")
    print()

    if choice == "1":
        student_id = input("Student ID: ")
        name = input("Student Name: ")
        email = input("Email: ")

        student = Student(student_id, name, email)
        gradebook.add_student(student)

    elif choice == "2":
        course_code = input("Course Code: ")
        course_name = input("Course Name: ")

        course = Course(course_code, course_name)
        gradebook.add_course(course)

        print("✅ Course added successfully!")

    elif choice == "3":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")

        gradebook.enroll_student(student_id, course_code)

    elif choice == "4":
        course_code = input("Course Code: ")

        print("\nAssessment Type")
        print("1. Quiz")
        print("2. Exam")
        print("3. Project")

        assessment_type = input("Choose: ")

        title = input("Assessment Title: ")
        total_marks = float(input("Total Marks: "))

        if assessment_type == "1":
            assessment = Quiz(title, total_marks)

        elif assessment_type == "2":
            assessment = Exam(title, total_marks)

        elif assessment_type == "3":
            assessment = Project(title, total_marks)

        else:
            print("❌ Invalid assessment type.")
            continue

        gradebook.add_assessment(course_code, assessment)

    elif choice == "5":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        assessment_title = input("Assessment Title: ")
        grade = float(input("Student Grade: "))

        gradebook.record_grade(
            student_id,
            course_code,
            assessment_title,
            grade
        )

    elif choice == "6":
        keyword = input("Enter Student ID or Name: ")
        gradebook.search_student(keyword)

    elif choice == "7":
        student_id = input("Student ID: ")
        gradebook.show_report(student_id)

    elif choice == "8":
        student_id = input("Student ID: ")
        gradebook.delete_student(student_id)

    elif choice == "9":
        print("\n👋 Thank you for using the Student Gradebook Manager!")
        break

    else:
        print("❌ Invalid choice. Please try again.")