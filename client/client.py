from transmit import connect, send
from status import status
from navigation import navigate
import random
import time
import math

#HOST, PORT = "codebb.cloudapp.net", 17429
#USER, PASSWORD = "algowinthis", "unicorns578"

HOST, PORT = "localhost", 17429
USER, PASSWORD = "a", "a"

sock = connect(HOST, PORT, USER, PASSWORD)

send(sock, "ACCELERATE 0 1")

while(True):
    s = status(send(sock, "STATUS"))
    rad = navigate(s)
    send(sock, "ACCELERATE {0} 1".format(rad))
    time.sleep(2)