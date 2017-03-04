from transmit import connect, send
from status import status
import random
import time
import math

HOST, PORT = "codebb.cloudapp.net", 17429
USER, PASSWORD = "algowinthis", "unicorns578"

#HOST, PORT = "localhost", 17429
#USER, PASSWORD = "a", "a"

sock = connect(HOST, PORT, USER, PASSWORD)
while(True):
    a = random.random() * 2 * math.pi
    send(sock, "ACCELERATE 0 0".format(a))
    s = status(send(sock, "STATUS"))
    send(sock, "BOMB {0} {1} 150".format(s['x'], s['y']))
    time.sleep(2)
#send(sock, "BRAKE")