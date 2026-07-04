# from student import Student
#
# student1 = Student("S001", "Zohra Haidary", "zohra@gmail.com")
#
# student1.enroll_course("PY101")
# student1.enroll_course("MATH101")
#
# student1.display_info()

# from student import Student
# from course import Course
#
# student1 = Student("S001", "Zohra Haidary", "zohra@gmail.com")
# course1 = Course("CS101", "Python Programming")
#
# course1.add_student(student1)
#
# student1.display_info()
# print()
# course1.display_course()
#
# from quiz import Quiz
#
# quiz1 = Quiz("Quiz 1", 20)
#
# quiz1.display_info()
from quiz import Quiz
from exam import Exam
from project import Project

quiz = Quiz("Quiz 1", 20)
exam = Exam("Midterm Exam", 100)
project = Project("Final Project", 50)

quiz.display_info()
print()

exam.display_info()
print()

project.display_info()