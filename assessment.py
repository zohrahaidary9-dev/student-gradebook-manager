class Assessment:
    def __init__(self, title, total_marks):
        self.title = title
        self.total_marks = total_marks

    def display_info(self):
        print("Title:", self.title)
        print("Total Marks:", self.total_marks)