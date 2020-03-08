from flask import Flask, render_template
import connection

app = Flask(__name__)

conn = connection.create_connection("aimDB")

cur = conn.cursor()
cur.execute("SELECT * FROM aimTB")

data = cur.fetchall()

@app.route('/')
def home():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)