# Demo: ZMQ to Websockets with Flask using Gevent

This is a Flask backend that can read messages from ZMQ and forward them to browsers over Websockets

## Running
Open three terminals as follows:

### On terminal 1
```
cd frontend
npm install
npm start | cat
```

### On terminal 2
```
cd backend
pip install -r requirements.txt
gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 --reload server:app

```

### On terminal 3
```
python sender.py
```


Finally, point your browser to port 3000.