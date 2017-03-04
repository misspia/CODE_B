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
send(sock, "STATUS")
config = configurations(send(sock, "CONFIGURATIONS"))
mapwidth = config['mapwidth']
mapheight = config['mapheight']
while(True):
    x = random.randint(0, mapwidth)
    y = random.randint(0, mapwidth)
    s = scan(send(sock, "SCAN {0} {1}".format(x, y)))
    print(s)
    time.sleep(2)