"""
Name: Nicholas Zankl
Date: August 20, 2026
Assignment: Module 8.2 - JSON Practice (student_records.py)
Purpose: Ingest student records from a JSON file, print formatted
outputs, append a new student entry, and write updates back to disk.
"""

import json


def print_students(student_list):
    """Loops through the student list and prints formatted records."""
    for student in student_list:
        l_name = student['L_Name']
        f_name = student['F_Name']
        s_id = student['Student_ID']
        email = student['Email']
        print(f"{l_name}, {f_name} : ID = {s_id} , Email = {email}")


# 1. Load existing JSON data into a list
with open('student.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

# 2. Notify user and display original list
print("--- Original Student List ---")
print_students(students)

# 3. Append your details
new_student = {
    "F_Name": "Nicholas",
    "L_Name": "Zankl",
    "Student_ID": 21615196,
    "Email": "nzankl.my365.bellevue.edu"
}
students.append(new_student)

# 4. Notify user and display updated list
print("\n--- Updated Student List ---")
print_students(students)

# 5. Write the updated list back to student.json
with open('student.json', 'w', encoding='utf-8') as file:
    json.dump(students, file, indent=4)

# 6. Notify user that file was updated
print("\nNotification: The student.json file has been updated.")
