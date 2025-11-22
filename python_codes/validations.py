# validations.py

def get_valid_number(prompt):
    # Keep asking until the user enters a valid number
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            # If they type text instead of a number, this catches the error
            print("Error: That is not a number. Please try again.")

def get_valid_name(prompt):
    # Simple check to ensure name isn't empty
    while True:
        name = input(prompt).strip()
        if len(name) > 0:
            return name
        print("Name cannot be empty.")