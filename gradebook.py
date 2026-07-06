class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}

    def search_student(self, keyword):
        keyword = keyword.lower()

        for student in self.students.values():
            if (student.get_id().lower() == keyword or
                    student.get_name().lower() == keyword):
                print("🎓 Student Found!")
                student.display_info()
                return student

        print("❌ Student not found.")
        return None

    def add_student(self, student):
        if student.get_id() in self.students:
            print("❌ A student with this ID already exists.")
        else:
            self.students[student.get_id()] = student
            print("✅ Student added successfully!")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("🗑️ Student deleted successfully.")
        else:
            print("❌ Student not found.")

    def add_course(self, course):
        if course.get_course_code() in self.courses:
            print("❌ A course with this code already exists.")
        else:
            self.courses[course.get_course_code()] = course
            print("✅ Course added successfully!")

    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            self.courses[course_code].add_assessment(assessment)
            print("✅ Assessment added successfully.")
        else:
            print("❌ Course not found.")

    def enroll_student(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]

            course.add_student(student)
            print("✅ Student enrolled successfully!")
        else:
            print("❌ Student or course not found.")

    def record_grade(self, student_id, course_code, assessment_title, grade):
        if student_id not in self.students:
            print("❌ Student not found.")
            return

        if course_code not in self.courses:
            print("❌ Course not found.")
            return

        if grade < 0 or grade > 100:
            print("❌ Grade must be between 0 and 100.")
            return

        self.grades[(student_id, course_code, assessment_title)] = grade
        print("✅ Grade recorded successfully.")

    def calculate_average(self, student_id, course_code):
        total = 0
        count = 0

        for key, grade in self.grades.items():
            if key[0] == student_id and key[1] == course_code:
                total += grade
                count += 1

        if count == 0:
            return 0

        return total / count

    def get_result(self, average):
        if average >= 55:
            return "Passed ✅"
        else:
            return "Failed ❌"

    def show_report(self, student_id):
        if student_id not in self.students:
            print("❌ Student not found.")
            return

        student = self.students[student_id]

        print("\n========== 🎓 Student Report ==========")
        student.display_info()
        print()

        for course_code in student.courses:
            print("📚 Course:", course_code)

            average = self.calculate_average(student_id, course_code)

            print("Average:", round(average, 2))
            print("Result:", self.get_result(average))
            print("-" * 40)