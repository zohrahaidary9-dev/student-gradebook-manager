class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}

    def show_dashboard(self):
        total_students = len(self.students)
        total_courses = len(self.courses)

        total_assessments = 0
        for course in self.courses.values():
            total_assessments += len(course.assessments)

        print("\n" + "=" * 50)
        print("🎓 STUDENT GRADEBOOK DASHBOARD")
        print("=" * 50)
        print(f"👨‍🎓 Total Students    : {total_students}")
        print(f"📚 Total Courses     : {total_courses}")
        print(f"📝 Total Assessments : {total_assessments}")
        print("=" * 50)

    def search_student(self, keyword):
        keyword = keyword.lower()

        found = False

        for student in self.students.values():
            if (student.get_id().lower() == keyword or
                    student.get_name().lower() == keyword):
                print("\n🎓 Student Found")
                print("-" * 30)
                student.display_info()
                found = True

        if not found:
            print("❌ Student not found.")

    def add_student(self, student):
        if student.get_id() in self.students:
            print("❌ A student with this ID already exists.")
        else:
            self.students[student.get_id()] = student
            print("✅ Student added successfully!")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("❌ Student not found.")
            return

        del self.students[student_id]

        keys_to_delete = []

        for key in self.grades:
            if key[0] == student_id:
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del self.grades[key]

        print("🗑️ Student deleted successfully!")

    def display_all_students(self):
        if not self.students:
            print("📭 No students have been added yet.")
            return

        print("\n========== 👨‍🎓 All Students ==========")

        for student in self.students.values():
            student.display_info()
            print("-" * 40)

    def display_all_courses(self):
        if not self.courses:
            print("📭 No courses have been added yet.")
            return

        print("\n========== 📚 All Courses ==========")

        for course in self.courses.values():
            course.display_info()
            print("-" * 40)

    def add_course(self, course):
        if course.get_course_code() in self.courses:
            print("❌ A course with this code already exists.")
        else:
            self.courses[course.get_course_code()] = course
            print("✅ Course added successfully!")

    def add_assessment(self, course_code, assessment):
        if course_code not in self.courses:
            print("❌ Course not found.")
            return

        course = self.courses[course_code]

        for item in course.assessments:
            if item.title == assessment.title:
                print("❌ Assessment already exists.")
                return

        course.add_assessment(assessment)

        print("✅ Assessment added successfully!")

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

            print(f"📊 Average: {average:.2f}")
            print(f"🏆 Result: {self.get_result(average)}")
            print("-" * 40)