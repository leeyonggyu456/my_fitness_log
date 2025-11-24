from flask import Flask
import sqlite3
import os

app = Flask(__name__)

DB_NAME = 'workout.db'


#DB 초기화 함수
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Workout (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            exercise_name TEXT,
            sets INTEGER,
            reps INTEGER,
            weight REAL
        )
    ''')
    conn.commit()
    conn.close()




@app.route('/')
def home():
    return "My Fitness Log - DB Initialized!"


if __name__ == '__main__':
    init_db()
    app.run(debug=True)