#!/usr/bin/env python3
#-*-coding:utf-8-*-

#in case host chat app on public domain need to change ip-address and port number in /home/boris/venv/Python3.7/lib/python3.7/site-packages/flask_socketio/__init__.py
#Also need to install next python apps- "pip install eventlet" and "pip install gevent-websocket"
#template folder is required for the chat app. 


from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET KEY'] = 'qwertyasdfgh11223344'
socketio = SocketIO(app)

@app.route('/')
def sessions():
	return render_template('session.html')

def messageReceived(methods = ['GET', 'POST']):
	print('Message was received!!')

@socketio.on('my event')
	
def hendle_my_custom_event(json, methods = ['GET', 'POST']):
	print('Received my event' + str(json))
	socketio.emit('my response', json, callback = messageReceived) 

if __name__ == '__main__':
	socketio.run(app, debug = True)
	
