from flask import Flask, request, redirect
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

@app.route('/add', methods=['GET','POST'])
def add_record():
    if request.method == 'POST':
        date = request.form['date']
        exercise_name = request.form['exercise_name']
        sets = request.form['sets']
        reps = request.form['reps']
        weight = request.form['weight']

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Workout (date, exercise_name, sets, reps, weight) VALUES (?, ?, ?, ?, ?)",
            (date, exercise_name, sets, reps, weight)
        )
        conn.commit()
        conn.close()

        return redirect('/')
    
    return '''
        <h2>운동 기록 추가</h2>
        <form method="post">
            날짜: <input type="text" name="date"><br>
            운동명: <input type="text" name="exercise_name"><br>
            세트 수: <input type="number" name="sets"><br>
            반복 수: <input type="number" name="reps"><br>
            무게(kg): <input type="number" step="0.1" name="weight"><br>
            <input type="submit" value="저장">
        </form>
        <p><a href="/">홈으로</a></p>
    '''


@app.route('/')
def home():
    return "My Fitness Log - DB Initialized!"


if __name__ == '__main__':
    init_db()
    app.run(debug=True)