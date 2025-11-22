# actions.py
import file_handler
import validations
from student_model import Student

def add_student(current_list):
    print("\n--- Add New Student ---")
    roll = validations.get_valid_number("Enter Roll Number: ")
    
    # Check for duplicate roll numbers
    for s in current_list:
        if s.roll_no == roll:
            print("Error: A student with this Roll Number already exists.")
            return current_list

    name = validations.get_valid_name("Enter Student Name: ")
    marks = validations.get_valid_number("Enter Marks (0-100): ")

    # Create new student object
    new_student = Student(roll, name, marks)
    current_list.append(new_student)
    
    # Save immediately so we don't lose data
    file_handler.save_all_students(current_list)
    print("Student added successfully!")
    return current_list

def view_students(current_list):
    print("\n--- Student List ---")
    if len(current_list) == 0:
        print("No records found.")
    else:
        print(f"{'Roll No':<10} {'Name':<20} {'Marks':<10}")
        print("-" * 40)
        for s in current_list:
            print(f"{s.roll_no:<10} {s.name:<20} {s.marks:<10}")
    input("\nPress Enter to continue...")

def search_student(current_list):
    print("\n--- Search Student ---")
    target_roll = validations.get_valid_number("Enter Roll No to search: ")
    
    found = False
    for s in current_list:
        if s.roll_no == target_roll:
            print(f"Found: {s.name} | Marks: {s.marks}")
            found = True
            break
    
    if not found:
        print("Student not found.")
    input("\nPress Enter to continue...")

def delete_student(current_list):
    print("\n--- Delete Student ---")
    target_roll = validations.get_valid_number("Enter Roll No to delete: ")
    
    # Create a new list without the deleted student
    new_list = []
    found = False
    
    for s in current_list:
        if s.roll_no == target_roll:
            found = True
            print(f"Deleting {s.name}...")
        else:
            new_list.append(s)
            
    if found:
        file_handler.save_all_students(new_list)
        print("Student deleted.")
        return new_list
    else:
        print("Student not found.")
        return current_list