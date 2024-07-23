#!/usr/bin/env python3

from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
        return student

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        return course

    def register_student_for_course(self, student_email, course_name, grade):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
            return True
        return False

    def calculate_ranking(self):
        return sorted(self.student_list, key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, course_name, grade):
        results = []
        for student in self.student_list:
            for course in student.courses_registered:
                if course['course'].name == course_name and course['grade'] == grade:
                    results.append(student)
        return results

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            transcript = f"Transcript for {student.names}:\n"
            for course in student.courses_registered:
                transcript += f"{course['course'].name}: {course['grade']}\n"
            transcript += f"GPA: {student.GPA}\n"
            return transcript
        return "Student not found."
