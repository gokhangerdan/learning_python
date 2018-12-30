# Start with a basic flask app webpage.
from flask_socketio import SocketIO
from flask import Flask, render_template
from time import sleep
from threading import Thread, Event
import serial.tools.list_ports


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

# turn the flask app into a socketio app
socketio = SocketIO(app)

# random number Generator Thread
thread = Thread()
thread_stop_event = Event()


#####

my_serial = '75433313639351C08261'


class ConnectArdu:
    status = False
    my_port = False
    connection = False
    number = False
    number2 = False


def connect_ardu():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if my_serial == p.serial_number:
            ConnectArdu.my_port = p.device

            ConnectArdu.connection = serial.Serial(ConnectArdu.my_port, 9600)

#####


class RandomThread(Thread):
    def __init__(self):
        self.delay = 1
        super(RandomThread, self).__init__()

    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        # infinite loop of magical random numbers
        print("Making random numbers", thread_stop_event.isSet())
        while not thread_stop_event.isSet():

            ser = ConnectArdu.connection
            if ser:
                data = str(ser.readline())
                if data[:7] == "b'val1=":
                    data_list = data[2:-3].split('-')
                    data1 = data_list[0]
                    data2 = data_list[1]
                    if data1[:5] == "val1=":
                        ConnectArdu.number = data1[5:]
                    if data2[:5] == "val2=":
                        ConnectArdu.number2 = data2[5:]

            if ConnectArdu.number and ConnectArdu.number2:
                number = ConnectArdu.number
                number2 = ConnectArdu.number2
            else:
                connect_ardu()
                number = "Device not found!"
                number2 = "Device not found!"

            print(number, number2)
            socketio.emit('newnumber', {'number1': number, 'number2': number2}, namespace='/test')
            sleep(self.delay)

    def run(self):
        self.randomNumberGenerator()


@app.route('/')
def index():
    # only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')


@socketio.on('connect', namespace='/test')
def test_connect():

    connect_ardu()

    # need visibility of the global thread object
    global thread
    print('Client connected')

    # Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = RandomThread()
        thread.start()


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
