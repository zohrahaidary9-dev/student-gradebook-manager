# from student import Student
#
# student1 = Student("S001", "Zohra Haidary", "zohra@gmail.com")
#
# student1.enroll_course("PY101")
# student1.enroll_course("MATH101")
#
# student1.display_info()

from student import Student
from course import Course

student1 = Student("S001", "Zohra Haidary", "zohra@gmail.com")
course1 = Course("CS101", "Python Programming")

course1.add_student(student1)

student1.display_info()
print()
course1.display_course()