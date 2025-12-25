#Exercise 1 - Exercise XP + 

# Initial Data
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# Initialize dictionaries to store calculated data
student_averages = {}
student_letter_grades = {}

# --- Calculation of Averages and Letter Grades ---
for student, grades in student_grades.items():
    # Calculate the average for each student
    average = sum(grades) / len(grades)
    student_averages[student] = average
    
    # Determine the letter grade based on the average
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
        
    student_letter_grades[student] = letter_grade

# --- Calculation of Class Average ---
class_average = sum(student_averages.values()) / len(student_averages)

# --- Print the Summary Report ---
print("--- Student Grade Summary Report ---")
for student in student_grades.keys():
    average = student_averages[student]
    letter = student_letter_grades[student]
    
    print(f"{student:<10}: Average = {average:.2f}, Letter Grade = {letter}")

print("-" * 37)
print(f"Class Average: {class_average:.2f}")
print("-" * 37)

