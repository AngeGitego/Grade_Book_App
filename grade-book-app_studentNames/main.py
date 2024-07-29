#!/usr/bin/env python3
from gradebook import GradeBook

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
        
        choice = input("Choose an action: ")
        
        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
            print("Student added.")
        
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = int(input("Enter course trimester: "))
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
            print("Course added.")
        
        elif choice == '3':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            if gradebook.register_student_for_course(email, course_name, grade):
                print("Student registered for course.")
            else:
                print("Error registering student for course.")
        
        elif choice == '4':
            gradebook.calculate_ranking()
        
        elif choice == '5':
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade threshold: "))
            gradebook.search_by_grade(course_name, grade)
        
        elif choice == '6':
            email = input("Enter student email: ")
            gradebook.generate_transcript(email)
        
        elif choice == '7':
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
