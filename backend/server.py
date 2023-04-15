from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import zmq.green as zmq
from gevent import monkey

monkey.patch_all()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route("/")
def index():
    render_template("../frontend/public/index.html")


@app.route("/api")
def api():
    return jsonify({"test": "999"})


def read_from_zmq():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5560")
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    print("Starting background loop")
    while True:
        message = socket.recv()
        socketio.emit('message', message.decode("utf-8"))
        print(message)


socketio.start_background_task(target=read_from_zmq)

if __name__ == '__main__':
    socketio.run(app)
