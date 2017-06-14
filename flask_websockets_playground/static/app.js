socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function() {
    socket.emit('client_connected', {data: "Hello, I'm a new client. Nice to meet you."});
});

socket.on('message', function (data) {
    console.log(data);
});

socket.on('alert', function (data) {
    alert(data);
});

function json_button() {
    socket.send('{"message": "I pushed the JSON button."}');
}

function alert_button() {
    socket.emit('alert', 'I pushed the ALERT button.')
}
