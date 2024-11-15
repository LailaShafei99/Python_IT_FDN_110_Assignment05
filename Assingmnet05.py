Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# -----------------------------------------------------------------------------#
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   LShafei, 12/11/2024, Creating script using dictionaries and files Version 2
# ---------------------------------------------------------------------------- #
import csv

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.

# When the program starts, read the file data into a list of dictionaries
try:
    with open(FILE_NAME, mode='r', newline='') as file:
        reader = csv.DictReader(file)

        # Ensure the CSV headers match expected keys
        expected_fields = ['first_name', 'last_name', 'course_name']
        for row in reader:
            if set(expected_fields).issubset(row.keys()):
                students.append(row)
            else:
                print(f"Warning: The row {row} does not have the expected columns.")
except FileNotFoundError:
    print(f"File {FILE_NAME} not found. Starting with an empty list.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")

# Main Program Loop
while True:
    print(MENU)
    menu_choice = input("What would you like to do: ").strip()

    if menu_choice == "1":  # Register a student for a course
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name:
                raise ValueError("First name cannot be empty.")

            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")

            course_name = input("Enter the course name: ").strip()
            if not course_name:
                raise ValueError("Course name cannot be empty.")

            student_data = {
                "first_name": student_first_name,
                "last_name": student_last_name,
                "course_name": course_name
            }
...             students.append(student_data)
...             print(f"Registered {student_first_name} {student_last_name} for {course_name}.")
...         except ValueError as ve:
...             print(f"Input error: {ve}")
...         except Exception as e:
...             print(f"An unexpected error occurred: {e}")
... 
...     elif menu_choice == "2":  # Show current data
...         if students:
...             print("-" * 50)
...             for student in students:
...                 # Make sure the keys exist
...                 first_name = student.get('first_name', 'N/A')
...                 last_name = student.get('last_name', 'N/A')
...                 course_name = student.get('course_name', 'N/A')
...                 print(f"Student {first_name} {last_name} is enrolled in {course_name}")
...             print("-" * 50)
...         else:
...             print("No student data available.")
... 
...     elif menu_choice == "3":  # Save data to a file
...         try:
...             with open(FILE_NAME, mode='w', newline='') as file:
...                 fieldnames = ['first_name', 'last_name', 'course_name']
...                 writer = csv.DictWriter(file, fieldnames=fieldnames)
...                 writer.writeheader()
...                 writer.writerows(students)
...             print(f"Data saved to {FILE_NAME}.")
...         except Exception as e:
...             print(f"An error occurred while saving data: {e}")
... 
...     elif menu_choice == "4":  # Exit the program
...         print("Exiting the program, thank you.")
...         break
... 
...     else:
...         print("Invalid choice! Please select option 1, 2, 3, or 4.")
