from flask import Flask, render_template, redirect
import connection

app = Flask(__name__)

conn = connection.create_connection("aimDB")

cur = conn.cursor()
cur.execute("SELECT * FROM aimTB")

data = cur.fetchall()

@app.route('/')
def home():
    return render_template('index.html', data=data)

@app.route('/get/<int:id>')
def get_aim(id):
    conn = connection.create_connection("aimDB")
    cur = conn.cursor()
    cur.execute("SELECT name FROM aimTB WHERE id =?", (id ,))
    aim = cur.fetchall()
    print("This is my id: ", id)
    print("This is the aim: ", aim)
    return render_template('index.html', data=data, aim=aim)

@app.route('/add')
def add_aim():
    return render_template("add_aim.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)