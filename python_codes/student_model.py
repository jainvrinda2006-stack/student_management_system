# student_model.py

class Student:
    def __init__(self, roll_no, name, marks):
        # Initialize the student details
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def to_string(self):
        # This helps us save the data easily as a string line
        # Format: RollNo,Name,Marks
        return f"{self.roll_no},{self.name},{self.marks}"