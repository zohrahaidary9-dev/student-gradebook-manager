from assessment import Assessment


class Quiz(Assessment):
    def __init__(self, title, total_marks):
        super().__init__(title, total_marks)

    def display_info(self):
        print("Quiz")
        print("Title:", self.title)
        print("Total Marks:", self.total_marks)