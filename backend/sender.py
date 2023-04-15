import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5560")

counter = 0

while True:
    msg = f"Greetings from zmq, already {counter} times!"
    socket.send(msg.encode("utf-8"))
    time.sleep(1)
    counter += 1
