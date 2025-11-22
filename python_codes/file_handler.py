# file_handler.py
import os
from student_model import Student

FILE_NAME = "students_data.txt"

def load_students():
    student_list = []
    
    # Check if file exists first to avoid errors
    if not os.path.exists(FILE_NAME):
        return student_list

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
            for line in lines:
                # Split the line by comma to get details
                data = line.strip().split(",")
                if len(data) == 3:
                    # Create a student object and add to list
                    s = Student(int(data[0]), data[1], int(data[2]))
                    student_list.append(s)
    except Exception as e:
        print(f"Error loading data: {e}")
        
    return student_list

def save_all_students(student_list):
    try:
        with open(FILE_NAME, "w") as file:
            for student in student_list:
                file.write(student.to_string() + "\n")
        print("Data saved successfully!")
    except Exception as e:
        print(f"Could not save data: {e}")