from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room, send
import os
import random
from dotenv import load_dotenv
from string import ascii_uppercase

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

socketio = SocketIO(app)

rooms = {}

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)

        if code not in rooms:
            break

    return code

@app.route('/', methods=['GET', 'POST'])
def home():
    session.clear()
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        join = request.form.get('join', False)
        create = request.form.get('create', False)

        if not name:
            return render_template('home.html', error='Name is required', code = code, name = name)
        
        if join != False and not code:
            return render_template('home.html', error='Code is required')
        
        room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template('home.html', error='Invalid code', code = code, name = name)
        
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))

    return render_template('home.html')

@app.route('/room')
def room():
    return render_template('room.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
