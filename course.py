class Course:
    def __init__(self, course_code, course_name):
        self.__course_code = course_code
        self.__course_name = course_name
        self.students = []
        self.assessments = []

    def get_course_code(self):
        return self.__course_code

    def get_course_name(self):
        return self.__course_name

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll_course(self.get_course_code())

    def add_assessment(self, assessment):
        self.assessments.append(assessment)

    def display_info(self):
        print("Course Code:", self.__course_code)
        print("Course Name:", self.__course_name)
        print("Number of Students:", len(self.students))