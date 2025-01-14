from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print(f'Received message: {data}')
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)