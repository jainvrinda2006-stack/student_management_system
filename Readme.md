# Student Management System

## 🌟 Overview

The Student Management System is a robust, file-based **Command-Line Interface (CLI)** application developed in **Python**. It's designed to streamline the management of student academic records, offering an easy-to-use, digitized alternative to traditional paper-based mark registers and attendance sheets.

## ✨ Key Features (CRUD Operations)

This application provides full **CRUD** (Create, Read, Update, Delete) functionality for student records:

* **1. Add New Student:** Allows input of Roll Number, Name, and Marks.
    * Includes **input validation** for numbers (positive integers) and non-empty strings.
    * Checks for and prevents **duplicate Roll Numbers**.
* **2. View All Students:** Displays all saved student records in a clean, formatted table.
* **3. Search Student:** Quickly finds and displays a student's details by searching for their unique Roll Number.
* **4. Delete Student:** Permanently removes a student's record from the system based on their Roll Number.
* **Data Persistence:** All data is automatically saved to and loaded from the `students_data.txt` file, ensuring no records are lost between sessions.

## ⚙️ Project Structure

The code is logically split into modular files for easy maintenance:

| File Name | Responsibility |
| :--- | :--- |
| `main.py` | Runs the main application loop and menu interface. |
| `actions.py` | Contains the core business logic (Add, View, Search, Delete). |
| `student_model.py`| Defines the `Student` class and its string representation for file storage. |
| `validations.py` | Handles all user input checks (number and name validation). |
| `file_handler.py` | Manages file I/O operations (loading from/saving to `students_data.txt`). |

## 🚀 How to Run

1.  **Prerequisites:** Ensure you have **Python 3.x** installed on your system.
2.  **Run:** Navigate to the project's root directory in your terminal and execute:
    ```bash
    python main.py
    ```
3.  **Interact:** Follow the on-screen menu prompts (1-5) to manage student records.
