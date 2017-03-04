from transmit import connect, send
from parser import *
from navigation import navigate
import random
import time
import math

HOST, PORT = "codebb.cloudapp.net", 17429
USER, PASSWORD = "algowinthis", "unicorns578"

#HOST, PORT = "localhost", 17429
#USER, PASSWORD = "a", "a"

sock = connect(HOST, PORT, USER, PASSWORD)

send(sock, "ACCELERATE 0 1")
config = configurations(send(sock, "CONFIGURATIONS"))
mapwidth = config['mapwidth']
mapheight = config['mapheight']
while(True):
    s = status(send(sock, "STATUS"))
    score = send(sock, "SCAN {0} {1}".format(s['x'], s['y']))
    print(score)
    time.sleep(2)