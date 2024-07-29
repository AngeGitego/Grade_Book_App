#!/usr/bin/env python3

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def register_for_course(self, course, grade):
        self.courses_registered.append({'course': course, 'grade': grade})
        self.calculate_GPA()

    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
            return

        total_credits = sum(course['course'].credits for course in self.courses_registered)
        total_points = sum(course['grade'] * course['course'].credits for course in self.courses_registered)

        if total_credits > 0:
            self.GPA = total_points / total_credits
        else:
            self.GPA = 0.0
