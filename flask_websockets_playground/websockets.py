from app import socketio
from flask_socketio import send, emit


@socketio.on('client_connected')
def handle_client_connect_event(json):
    print('received json from client: {0}'.format(str(json)))


@socketio.on('message')
def handle_json_button(json):
    print('received json from client: {0}'.format(str(json)))
    return_json = {}
    return_json['stuff I heard you say'] = json
    send(return_json, json=True)


@socketio.on('alert')
def handle_alert_event(json):
    # it will forward the json to all clients.
    print('Message from Javascript client: {0}'.format(json))
    emit('alert', 'I see you pushed the ALERT button.')
