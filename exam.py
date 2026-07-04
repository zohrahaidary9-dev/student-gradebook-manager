from assessment import Assessment


class Exam(Assessment):
    def __init__(self, title, total_marks):
        super().__init__(title, total_marks)

    def display_info(self):
        print("Exam")
        print("Title:", self.title)
        print("Total Marks:", self.total_marks)