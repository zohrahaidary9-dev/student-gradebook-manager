from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook


def display_menu():
    print("\n" + "=" * 50)
    print("🎓 Student Gradebook Management System")
    print("=" * 50)
    print("1️⃣  Dashboard")
    print("2️⃣  Add Student")
    print("3️⃣  Add Course")
    print("4️⃣  Enroll Student")
    print("5️⃣  Add Assessment")
    print("6️⃣  Record Grade")
    print("7️⃣  Search Student")
    print("8️⃣  Show Student Report")
    print("9️⃣  Delete Student")
    print("🔟 View All Students")
    print("1️⃣1️⃣ View All Courses")
    print("0️⃣  Exit")


gradebook = Gradebook()

while True:
    display_menu()

    choice = input("\n👉 Enter your choice (0-11): ")
    print()

    if choice == "1":
        gradebook.show_dashboard()

    elif choice == "2":
        student_id = input("🆔 Student ID: ")
        name = input("👤 Student Name: ")
        email = input("📧 Email: ")

        student = Student(student_id, name, email)
        gradebook.add_student(student)

    elif choice == "3":
        course_code = input("📚 Course Code: ")
        course_name = input("📖 Course Name: ")

        course = Course(course_code, course_name)
        gradebook.add_course(course)

    elif choice == "4":
        student_id = input("🆔 Student ID: ")
        course_code = input("📚 Course Code: ")

        gradebook.enroll_student(student_id, course_code)

    elif choice == "5":
        course_code = input("📚 Course Code: ")

        print("\nChoose Assessment Type")
        print("1. Quiz")
        print("2. Exam")
        print("3. Project")

        assessment_type = input("Choice: ")

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

    elif choice == "6":
        student_id = input("🆔 Student ID: ")
        course_code = input("📚 Course Code: ")
        assessment_title = input("📝 Assessment Title: ")
        grade = float(input("🎯 Grade: "))

        gradebook.record_grade(student_id, course_code, assessment_title, grade)

    elif choice == "7":
        keyword = input("🔍 Enter Student ID or Name: ")
        gradebook.search_student(keyword)

    elif choice == "8":
        student_id = input("🆔 Student ID: ")
        gradebook.show_report(student_id)

    elif choice == "9":
        student_id = input("🆔 Student ID: ")
        gradebook.delete_student(student_id)

    elif choice == "10":
        gradebook.display_all_students()

    elif choice == "11":
        gradebook.display_all_courses()

    elif choice == "0":
        print("\n👋 Thank you for using the Student Gradebook Management System!")
        print("📚 Goodbye and have a great day!")
        break

    else:
        print("❌ Invalid choice! Please try again.")