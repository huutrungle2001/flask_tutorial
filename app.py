from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

SESSIONS = [
    {
        "session_id": 1,
        "session_name": "Ballet",
        "user_id": 1,
        "date": "2021-01-01",
        "duration": 60,
        "performance_notes": "Great session!"
    },
    {
        "session_id": 2,
        "session_name": "Hip-Hop",
        "user_id": 1,
        "date": "2021-01-02",
        "duration": 45,
        "performance_notes": "Good session!"
    },
    {
        "session_id": 3,
        "session_name": "Salsa",
        "user_id": 2,
        "date": "2021-01-03",
        "duration": 30,
        "performance_notes": "Bad session!"
    },
    {
        "session_id": 4,
        "session_name": "Tango",
        "user_id": 2,
        "date": "2021-01-04",
        "duration": 90,
        "performance_notes": "Great session!"
    },
    {
        "session_id": 5,
        "session_name": "Breakdancing",
        "user_id": 3,
        "date": "2021-01-05",
        "duration": 60,
        "performance_notes": "Good session!"
    }
]

@app.route('/')
def hello():
    return render_template('home.html', sessions=SESSIONS, group_name="Dancethology")

@app.route('/sessions')
def sessions_list():
    return jsonify(SESSIONS)