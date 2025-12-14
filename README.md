# My Fitness Log

My Fitness Log는 Flask와 SQLite를 이용하여 구현한  
운동 기록 관리 웹 애플리케이션입니다.

본 프로젝트는 데이터베이스가 웹 응용에서  
정보의 저장, 조회, 수정, 삭제(CRUD)에  
어떤 역할을 하는지 이해하는 것을 목표로 합니다.

---

## 📌 주요 기능

- 운동 기록 추가 (Create)
- 운동 기록 목록 조회 (Read)
- 운동 기록 수정 (Update)
- 운동 기록 삭제 (Delete)
- SQLite DB(workout.db)에 데이터 영구 저장

---

## 🛠 사용 기술

- Programming Language: Python
- Web Framework: Flask
- Database (DBMS): SQLite
- Frontend: HTML, CSS
- Development Tool: VS Code
- Version Control: Git / GitHub

---

## 🗄 데이터베이스 구성

- Database File: `workout.db`
- Table Name: `Workout`

### 테이블 스키마

```sql
CREATE TABLE Workout (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    exercise_name TEXT,
    sets INTEGER,
    reps INTEGER,
    weight REAL
);

---
## 실행 방법
1.Python 설치
2.Flask 설치
3.서버 실행
4.웹 브라우저에서 접속

## 📄 웹 페이지 구성

- `/add`  
사용자가 운동 정보를 입력하여 데이터베이스에 저장하는 페이지

- `/list`  
데이터베이스에 저장된 모든 운동 기록을 조회하는 페이지

- `/edit/<id>`  
선택한 운동 기록을 수정하는 페이지

- `/delete/<id>`  
선택한 운동 기록을 삭제하는 기능

---

## 📁 프로젝트 구조

my_fitness_log/
├── app.py
├── workout.db
├── templates/
│ ├── add.html
│ ├── list.html
│ └── edit.html
└── static/
└── style.css