# main.py
import actions
import file_handler

def main():
    # Load data when program starts
    my_students = file_handler.load_students()

    while True:
        print("==========================")
        print(" STUDENT MANAGEMENT SYSTEM")
        print("==========================")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_students = actions.add_student(my_students)
        elif choice == '2':
            actions.view_students(my_students)
        elif choice == '3':
            actions.search_student(my_students)
        elif choice == '4':
            my_students = actions.delete_student(my_students)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")

if __name__ == "__main__":
    main()