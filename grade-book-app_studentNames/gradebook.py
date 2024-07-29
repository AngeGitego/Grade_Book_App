#!/usr/bin/env python3

from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        if any(s.email == email for s in self.student_list):
            print("Student already exists.")
            return
        new_student = Student(email, names)
        self.student_list.append(new_student)

    def add_course(self, course):
        if any(c.name == course.name for c in self.course_list):
            print("Course already exists.")
            return
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
            return True
        return False

    def calculate_ranking(self):
        sorted_students = sorted(self.student_list, key=lambda s: s.GPA, reverse=True)
        for rank, student in enumerate(sorted_students, start=1):
            print(f"Rank {rank}: {student.names} - GPA: {student.GPA:.2f}")

    def search_by_grade(self, course_name, grade_threshold):
        students = [s for s in self.student_list if any(c['course'].name == course_name and c['grade'] >= grade_threshold for c in s.courses_registered)]
        for student in students:
            print(f"{student.names} - Email: {student.email}")

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            print(f"Transcript for {student.names}:")
            for course in student.courses_registered:
                print(f"Course: {course['course'].name}, Trimester: {course['course'].trimester}, Credits: {course['course'].credits}, Grade: {course['grade']}")
            print(f"GPA: {student.GPA:.2f}")
        else:
            print("Student not found.")
