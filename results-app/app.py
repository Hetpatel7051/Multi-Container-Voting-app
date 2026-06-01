from flask import Flask, render_template_string
import os
import psycopg2

app = Flask(__name__)

def get_votes_count():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'db'),
            user=os.getenv('DB_USER', 'admin'),
            password=os.getenv('DB_PASS', 'secretpassword'),
            database=os.getenv('DB_NAME', 'cloud_votes')
        )
        cur = conn.cursor()
        cur.execute("SELECT candidate, COUNT(*) FROM votes GROUP BY candidate;")
        results = cur.fetchall()
        cur.close()
        conn.close()
        return dict(results)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return {}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Voting Results</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; background: #f4f6f9; margin-top: 50px; }
        .container { display: flex; justify-content: center; gap: 50px; margin-top: 30px; }
        .box { padding: 30px; border-radius: 10px; color: white; min-width: 150px; font-size: 24px; }
        .cats { background: #3498db; } .dogs { background: #e67e22; }
        .refresh { margin-top: 30px; font-size: 14px; color: #7f8c8d; }
    </style>
</head>
<body>
    <h1>Real-Time Election Standings</h1>
    <div class="container">
        <div class="box cats">🐱 Cats: <strong>{{ votes.get('Cats', 0) }}</strong></div>
        <div class="box dogs">🐶 Dogs: <strong>{{ votes.get('Dogs', 0) }}</strong></div>
    </div>
    <p class="refresh">Refresh the page to sync latest data entries.</p>
</body>
</html>
"""

@app.route('/')
def index():
    votes = get_votes_count()
    return render_template_string(HTML_TEMPLATE, votes=votes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
