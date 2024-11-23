var ws = new WebSocket('ws://localhost:1234/ws');

ws.onmessage = function(event) {
	var messages = document.getElementById('messages');
	var message = document.createElement('li');
	var content = document.createTextNode(event.data);
	message.append(content);
	messages.appendChild(message);
}

function sendMessage(event){
	var input = document.getElementById("message");
	ws.send(input.value);
	input.value = '';
	event.preventDefault();
}