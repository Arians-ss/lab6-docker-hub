from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    student_surname = "Kodynets Arina KN-22"  # ваше прізвище латиницею
    return f"<h1>Hello from Docker! V1</h1><p>Виконала: {student_surname}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
