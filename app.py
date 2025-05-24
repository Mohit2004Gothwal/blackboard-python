from flask import Flask, render_template_string, render_template
from flask_socketio import SocketIO, emit
import subprocess

app = Flask(__name__)
socketio = SocketIO(app)  # Initialize SocketIO

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run1")
def run_main():
    subprocess.Popen(["python", "main.py"])
    socketio.emit('status', {'message': 'main.py started!'}, broadcast=True)
    return render_template_string('''
        <h2 style="text-align:center; color:white;">✅ Running main.py...</h2>
        <div style="text-align: center; margin-top: 30px;">
            <a class="back-home" href="/" style="padding: 12px 24px; background-color: #00ffc3; color: black; text-decoration: none; font-size: 18px; border-radius: 6px;">⬅️ Back to Home</a>
        </div>
        <style>body { background-color: black; color: white; font-family: sans-serif; }</style>
    ''')

@app.route("/run2")
def run_main2():
    subprocess.Popen(["python", "main2.py"])
    socketio.emit('status', {'message': 'main2.py started!'}, broadcast=True)
    return render_template_string('''
        <h2 style="text-align:center; color:white;">✅ Running main2.py...</h2>
        <div style="text-align: center; margin-top: 30px;">
            <a class="back-home" href="/" style="padding: 12px 24px; background-color: #00ffc3; color: black; text-decoration: none; font-size: 18px; border-radius: 6px;">⬅️ Back to Home</a>
        </div>
        <style>body { background-color: black; color: white; font-family: sans-serif; }</style>
    ''')

@app.route("/run3")
def run_main3():
    subprocess.Popen(["python", "main3.py"])
    socketio.emit('status', {'message': 'main3.py started!'}, broadcast=True)
    return render_template_string('''
        <h2 style="text-align:center; color:white;">✅ Running main3.py...</h2>
        <div style="text-align: center; margin-top: 30px;">
            <a class="back-home" href="/" style="padding: 12px 24px; background-color: #00ffc3; color: black; text-decoration: none; font-size: 18px; border-radius: 6px;">⬅️ Back to Home</a>
        </div>
        <style>body { background-color: black; color: white; font-family: sans-serif; }</style>
    ''')

@app.route("/mobile")
def mobile_home():
    return render_template("index2.html")


# SocketIO event handlers - only defined once
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    emit('response', {'data': 'Message received!'}, broadcast=True)

@socketio.on('my event')
def handle_my_event(json):
    print('Received my event:', json)
    emit('response', {'data': 'My event received!'}, broadcast=True)

@socketio.on('chat message')
def handle_chat_message(msg):
    print(f"User says: {msg}")
    # Simple echo bot logic - replace with your chatbot AI if you want
    reply = f"Echo: {msg}"
    emit('bot reply', reply, broadcast=False)  # send only to sender


if __name__ == "__main__":
    socketio.run(app, debug=True)
