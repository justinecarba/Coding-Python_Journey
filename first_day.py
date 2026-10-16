



# 1. Smart Calculator

"""
Create a calculator that performs addition, subtraction, multiplication, and division.
"""

"""           
running = True

while running:
    class Calculator:
        def add(self, num1, num2):
            return num1 + num2

        def subtract(self, num1, num2):
            return num1 - num2

        def multiply(self, num1, num2):
            return num1 * num2

        def divide(self, num1, num2):
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            return num1 / num2


    def calculate(num1, num2, operator):
        calc = Calculator()

        if operator == "+":
            return calc.add(num1, num2)
        if operator == "-":
            return calc.subtract(num1, num2)
        if operator == "*":
            return calc.multiply(num1, num2)
        if operator == "/":
            return calc.divide(num1, num2)

        raise ValueError("Invalid operator. Use +, -, *, or /.")


    operator = input("Enter the operator (+ - * /) : ").strip()
    num1 = int(input("Enter the first number  : "))
    num2 = int(input("Enter the second number : "))

    result = calculate(num1, num2, operator)
    print(f"Result: {result}")

    again = input("Calculate Again? Y/N : ").upper() .strip()

    if again != "Y" and again == "N":
        print("Exiting the program....")
        running = False

    else:
        continue
"""

# Number Guessing Game

"""
- Let the computer generate a random number. The player guesses until they find the correct answer.
"""

"""   
import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    print("\n====Welcome to Number Guessing Game====")
    print("====Guess the secret number at 1-100====")

    while attempts < max_attempts:
        try:
            guess = int(input("\nGuess the secret number  : "))
        except ValueError:
            print("Please enter a valid number!!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too Low. Higher!")
            remaining = max_attempts - attempts
            print(f"Your remaining Attempts is {remaining}")

        elif guess > secret_number:
            print("Too High. Lower!")
            remaining = max_attempts - attempts
            print(f"Your remaining Attempts is {remaining}")

        else:
            print(f"Correct!! Congratss you guess it with {attempts} attempts!!")

            again = input("Guess Again? Y/N : ").upper() .strip()

            if again != "Y" and again == "N":
                print("Exiting the program...")
                break

            else:
                continue

    else:
        print(f"Your attempts fully used. The Secret Number is = {secret_number}")
        return
    
number_guessing_game()
"""



# Student Grade Management System

"""Store student names and grades, calculate averages, and display pass or fail results."""


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, gender, math, english, science):
        if not name:
            raise ValueError("Student name is required.")

        average = self.calculate_average(math, english, science)
        category = "Pass" if average >= 50 else "Fail"

        student = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Math": math,
            "English": english,
            "Science": science,
            "Average": average,
            "Category": category,
        }
        self.students.append(student)

    def calculate_average(self, math, english, science):
        return (math + english + science) / 3

    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\nStudent Records")
        print("-" * 110)
        print(f"{'Name':<15}{'Age':<5}{'Gender':<8}{'Math':<8}{'English':<9}{'Science':<9}{'Average':<9}{'Status':<7}")
        print("-" * 110)

        for student in self.students:
            print(
                f"{student['Name']:<15}"
                f"{student['Age']:<5}"
                f"{student['Gender']:<8}"
                f"{student['Math']:<8}"
                f"{student['English']:<9}"
                f"{student['Science']:<9}"
                f"{student['Average']:<9.2f}"
                f"{student['Category']:<7}"
            )

    def search_student(self, name):
        for student in self.students:
            if student["Name"].lower() == name.lower():
                return student
        return None

    def update_student(self, name, subject, new_grade):
        student = self.search_student(name)
        if student is None:
            print("Student not found.")
            return

        valid_subjects = ["Math", "English", "Science"]
        if subject not in valid_subjects:
            print("Invalid subject. Choose Math, English, or Science.")
            return

        student[subject] = new_grade
        student["Average"] = self.calculate_average(
            student["Math"], student["English"], student["Science"]
        )
        student["Category"] = "Pass" if student["Average"] >= 50 else "Fail"
        print(f"Updated {name}'s {subject} grade.")

    def delete_student(self, name):
        for index, student in enumerate(self.students):
            if student["Name"].lower() == name.lower():
                del self.students[index]
                print(f"Deleted student: {name}")
                return
        print("Student not found.")


def main():
    system = StudentManagementSystem()

    while True:
        print("\n===== Student Grade Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student Grade")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            try:
                name = input("Enter student name: ").strip()
                age = int(input("Enter student age: "))
                gender = input("Enter student gender: ").strip()
                math = float(input("Enter Math grade: "))
                english = float(input("Enter English grade: "))
                science = float(input("Enter Science grade: "))
                system.add_student(name, age, gender, math, english, science)
                print("Student added successfully.")
            except ValueError as error:
                print(f"Invalid input: {error}")

        elif choice == "2":
            system.display_students()

        elif choice == "3":
            name = input("Enter student name to search: ").strip()
            student = system.search_student(name)
            if student:
                print(student)
            else:
                print("Student not found.")

        elif choice == "4":
            name = input("Enter student name: ").strip()
            subject = input("Enter subject (Math, English, Science): ").strip().title()
            try:
                new_grade = float(input("Enter new grade: "))
                system.update_student(name, subject, new_grade)
            except ValueError:
                print("Grade must be a number.")

        elif choice == "5":
            name = input("Enter student name to delete: ").strip()
            system.delete_student(name)

        elif choice == "6":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid option. Please choose from 1 to 6.")


if __name__ == "__main__":
    main()

