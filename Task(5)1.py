# Create dictionary of student marks
student_marks = {
    "Gopal": 85,
    "Sumit": 78,
    "Amit": 92
}

# Ask user for a student's name
name = input("Enter the student's name: ")

# Retrieve and display the marks
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")

