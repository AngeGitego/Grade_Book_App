import sqlite3

def initialize_db():
    conn = sqlite3.connect('gradebook.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        email TEXT PRIMARY KEY,
                        names TEXT,
                        gpa REAL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        trimester INTEGER,
                        credits INTEGER)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS registrations (
                        student_email TEXT,
                        course_id INTEGER,
                        grade REAL,
                        FOREIGN KEY (student_email) REFERENCES students (email),
                        FOREIGN KEY (course_id) REFERENCES courses (id))''')
    
    conn.commit()
    conn.close()

initialize_db()
