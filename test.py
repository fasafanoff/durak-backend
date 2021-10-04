from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def home():
    return '''<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js" integrity="sha512-q/dWJ3kcmjBLU4Qc47E4A9kTB4m3wuTY7vkFJDTZKjTs8jhyGQnaUrxa0Ytd0ssMZhbNua9hE+E7Qv1j+DyZwA==" crossorigin="anonymous"></script>
<script type="text/javascript" charset="utf-8">
    var socket = io();
    socket.on('connect', function() {
        socket.emit('my event',"I'm connected");
    });
</script>
<button id="button" >click</button>
<script>
    const button = document.getElementById('button')
    button.addEventListener('click', ()=> socket.emit('my event','clicked'))
</script>
'''


@socketio.on('my event')
def handle_message(data):
    print('received message: ' + data)


if __name__ == '__main__':
    socketio.run(app, port=8000)
    app.run(port=8000)
