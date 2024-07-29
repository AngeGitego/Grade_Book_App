#!/usr/bin/env python3

import sqlite3
from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.conn = sqlite3.connect('gradebook.db')
        self.cursor = self.conn.cursor()
    
    def add_student(self, email, names):
        student = Student(email, names)
        self.cursor.execute('INSERT INTO students (email, names, gpa) VALUES (?, ?, ?)', (email, names, student.gpa))
        self.conn.commit()
    
    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.cursor.execute('INSERT INTO courses (name, trimester, credits) VALUES (?, ?, ?)', (name, trimester, credits))
        self.conn.commit()
    
    def register_student_for_course(self, email, course_name, grade):
        self.cursor.execute('SELECT id FROM courses WHERE name = ?', (course_name,))
        course_id = self.cursor.fetchone()
        if not course_id:
            print("Course not found.")
            return False
        
        student = Student(email, "")
        student.register_for_course(course_id[0], grade)
        print("Student registered for course.")
        return True
    
    def calculate_ranking(self):
        self.cursor.execute('SELECT email, gpa FROM students ORDER BY gpa DESC')
        rankings = self.cursor.fetchall()
        for rank, (email, gpa) in enumerate(rankings, start=1):
            print(f'Rank {rank}: {email} - GPA: {gpa}')
    
    def search_by_grade(self, course_name, grade):
        self.cursor.execute('''SELECT s.email, s.names 
                               FROM registrations r 
                               JOIN courses c ON r.course_id = c.id 
                               JOIN students s ON r.student_email = s.email 
                               WHERE c.name = ? AND r.grade >= ?''', (course_name, grade))
        students = self.cursor.fetchall()
        for email, names in students:
            print(f'Student: {names}, Email: {email}')
    
    def generate_transcript(self, email):
        self.cursor.execute('''SELECT c.name, r.grade 
                               FROM registrations r 
                               JOIN courses c ON r.course_id = c.id 
                               WHERE r.student_email = ?''', (email,))
        transcript = self.cursor.fetchall()
        self.cursor.execute('SELECT gpa FROM students WHERE email = ?', (email,))
        gpa = self.cursor.fetchone()[0]
        
        print(f'Transcript for {email}:')
        for course_name, grade in transcript:
            print(f'Course: {course_name}, Grade: {grade}')
        print(f'GPA: {gpa}')

gradebook = GradeBook()

