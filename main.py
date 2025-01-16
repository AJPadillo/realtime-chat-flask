from flask import Flask, render_template, request, session, redirect
from flask_socketio import SocketIO, emit, join_room, leave_room, send
import os
from dotenv import load_dotenv
from string import ascii_uppercase

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        join = request.form.get('join', False)
        create = request.form.get('create', False)

    return render_template('home.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)



@socketio.on('message')
def handle_message(data):
    print(f'Received message: {data}')
    emit('message', data, broadcast=True)

