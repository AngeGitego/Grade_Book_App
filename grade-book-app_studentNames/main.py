#!/usr/bin/env python3

from gradebook import GradeBook
from course import Course

def main():
    gradebook = GradeBook()

    while True:
        print("""
        1. Add student
        2. Add course
        3. Register student for course
        4. Calculate ranking
        5. Search by grade
        6. Generate transcript
        7. Exit
        """)
        action = input("Choose an action: ")

        if action == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
            print("Student added.")
        elif action == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            course = Course(name, trimester, credits)
            gradebook.add_course(course)
            print("Course added.")
        elif action == '3':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            if gradebook.register_student_for_course(email, course_name, grade):
                print("Student registered for course.")
            else:
                print("Error registering student for course.")
        elif action == '4':
            gradebook.calculate_ranking()
        elif action == '5':
            course_name = input("Enter course name: ")
            grade_threshold = float(input("Enter minimum grade: "))
            gradebook.search_by_grade(course_name, grade_threshold)
        elif action == '6':
            email = input("Enter student email: ")
            gradebook.generate_transcript(email)
        elif action == '7':
            print("Exiting...")
            break
        else:
            print("Invalid action. Please choose a valid option.")

if __name__ == "__main__":
    main()
