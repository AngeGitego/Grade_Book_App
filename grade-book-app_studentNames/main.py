#!/usr/bin/env python3

from gradebook import GradeBook

def main():
    gradebook = GradeBook()
    
    while True:
        print("\n1. Add student")
        print("2. Add course")
        print("3. Register student for course")
        print("4. Calculate ranking")
        print("5. Search by grade")
        print("6. Generate transcript")
        print("7. Exit")
        
        choice = input("Choose an action: ")
        
        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
            print("Student added.")
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
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
            ranking = gradebook.calculate_ranking()
            print("Student Ranking:")
            for idx, student in enumerate(ranking):
                print(f"{idx + 1}. {student.names} - GPA: {student.GPA}")
        elif choice == '5':
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            results = gradebook.search_by_grade(course_name, grade)
            print("Students with grade", grade, "in", course_name)
            for student in results:
                print(student.names)
        elif choice == '6':
            email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(email)
            print(transcript)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
