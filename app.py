from flask import Flask, render_template, request, jsonify
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def init_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50),
                score INT
            )
        ''')
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("DB Init Error:", e)

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_score', methods=['POST'])
def save_score():
    data = request.json
    username = data.get('username')
    score = data.get('score')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO players (username, score) VALUES (%s, %s)', (username, score))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"status": "success", "message": "Đã lưu dữ liệu lên Neon DB!"})

if __name__ == '__main__':
    app.run(debug=True)
  
