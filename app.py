from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os
from dotenv import load_dotenv

load_dotenv()