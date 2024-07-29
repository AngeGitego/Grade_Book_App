#!/usr/bin/env python3

import sqlite3

class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.gpa = 0.0
    
    def calculate_GPA(self):
        conn = sqlite3.connect('gradebook.db')
        cursor = conn.cursor()
        
        cursor.execute('''SELECT SUM(c.credits * r.grade) / SUM(c.credits) 
                          FROM registrations r 
                          JOIN courses c ON r.course_id = c.id 
                          WHERE r.student_email = ?''', (self.email,))
        
        result = cursor.fetchone()
        self.gpa = result[0] if result[0] is not null else 0.0
        
        cursor.execute('UPDATE students SET gpa = ? WHERE email = ?', (self.gpa, self.email))
        conn.commit()
        conn.close()
    
    def register_for_course(self, course_id, grade):
        conn = sqlite3.connect('gradebook.db')
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO registrations (student_email, course_id, grade) VALUES (?, ?, ?)', 
                       (self.email, course_id, grade))
        
        conn.commit()
        conn.close()
        self.calculate_GPA()
