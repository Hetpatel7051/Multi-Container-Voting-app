from flask import Flask, render_template_string, request, redirect
import os
import psycopg2
import time

app = Flask(__name__)

# Wait for DB to wake up and connect
def get_db_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'db'),
                user=os.getenv('DB_USER', 'admin'),
                password=os.getenv('DB_PASS', 'secretpassword'),
                database=os.getenv('DB_NAME', 'cloud_votes')
            )
            return conn
        except psycopg2.OperationalError:
            print("Waiting for database connection...")
            time.sleep(1)

# Initialize Table
conn = get_db_connection()
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS votes (id SERIAL PRIMARY KEY, candidate TEXT);")
conn.commit()
cur.close()
conn.close()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Voting App</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background: #f4f6f9; margin-top: 50px; }
        .btn { padding: 20px 40px; font-size: 24px; margin: 20px; cursor: pointer; border: none; border-radius: 8px; color: white; transition: 0.2s; }
        .btn-cat { background: #3498db; } .btn-cat:hover { background: #2980b9; }
        .btn-dog { background: #e67e22; } .btn-dog:hover { background: #d35400; }
    </style>
</head>
<body>
    <h1>Cast Your Vote!</h1>
    <form action="/vote" method="POST">
        <button class="btn btn-cat" name="vote" value="Cats">🐱 Vote Cats</button>
        <button class="btn btn-dog" name="vote" value="Dogs">🐶 Vote Dogs</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/vote', methods=['POST'])
def vote():
    choice = request.form.get('vote')
    if choice in ['Cats', 'Dogs']:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO votes (candidate) VALUES (%s);", (choice,))
        conn.commit()
        cur.close()
        conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
