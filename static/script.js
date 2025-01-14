const socket = io();

const messages = document.getElementById('messages');
const input = document.getElementById('message');
const button = document.getElementById('send');

button.addEventListener('click', () => {
    const message = input.value;
    if (message) {
        socket.send(message);
        input.value = '';
    }
});

socket.on('message', data => {
    const li = document.createElement('li');
    li.textContent = data;
    messages.appendChild(li);
});
