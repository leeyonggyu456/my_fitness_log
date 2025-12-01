from flask import Flask, request, redirect, render_template
import sqlite3
import os

app = Flask(__name__)

DB_NAME = 'workout.db'


# --------------------------
# DB 초기화 함수
# --------------------------
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


# --------------------------
# 운동 기록 추가
# --------------------------
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

        return redirect('/list')
    
    return render_template('add.html')


# --------------------------
# 운동 기록 조회
# --------------------------
@app.route('/list')
def list_records():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Workout ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()

    return render_template("list.html", rows=rows)


# --------------------------
# 운동 기록 수정
# --------------------------
@app.route('/edit/<int:record_id>', methods=['GET', 'POST'])
def edit_record(record_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    if request.method == 'POST':
        date = request.form['date']
        exercise_name = request.form['exercise_name']
        sets = request.form['sets']
        reps = request.form['reps']
        weight = request.form['weight']

        cur.execute("""
            UPDATE Workout
            SET date = ?, exercise_name = ?, sets = ?, reps = ?, weight = ?
            WHERE id = ?
        """, (date, exercise_name, sets, reps, weight, record_id))
        
        conn.commit()
        conn.close()
        return redirect('/list')

    cur.execute("SELECT * FROM Workout WHERE id = ?", (record_id,))
    row = cur.fetchone()
    conn.close()

    return render_template("edit.html", row=row)


# --------------------------
# 운동 기록 삭제
# --------------------------
@app.route('/delete/<int:record_id>')
def delete_record(record_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("DELETE FROM Workout WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()

    return redirect('/list')


# --------------------------
# 홈 → /add 로 이동
# --------------------------
@app.route('/')
def home():
    return redirect('/add')


# --------------------------
# 실행부
# --------------------------
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
