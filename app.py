from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML page

@socketio.on('update_status')
def handle_status_update(data):
    status = data['status']
    person_info = data.get('person_info')  # Get person information, if available
    print(f"Status Received: {status}")
    print(f"Person Info: {person_info}")

    # Emit the status update along with person info if available
    emit('status_update', {'status': status, 'person_info': person_info}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
