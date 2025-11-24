from flask import Flask, request, redirect
import sqlite3
import os

app = Flask(__name__)

DB_NAME = 'workout.db'

# Step 4: 운동 기록 조회 기능
@app.route('/list')
def list_records():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Workout ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()

    table = '''
        <h2>운동 기록 목록</h2>
        <table border="1" cellspacing="0" cellpadding="5">
            <tr>
                <th>ID</th>
                <th>날짜</th>
                <th>운동명</th>
                <th>세트</th>
                <th>반복</th>
                <th>무게(kg)</th>
            </tr>
    '''

    for r in rows:
        table += f"""
            <tr>
                <td>{r[0]}</td>
                <td>{r[1]}</td>
                <td>{r[2]}</td>
                <td>{r[3]}</td>
                <td>{r[4]}</td>
                <td>{r[5]}</td>
            </tr>
        """

    table += "</table><br><a href='/'>홈으로</a> | <a href='/add'>운동 기록 추가</a>"

    return table
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
    return redirect('/add')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)