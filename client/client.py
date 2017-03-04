from transmit import connect, send
from parser import *
from navigation import *
import random
import time
import math

HOST, PORT = "codebb.cloudapp.net", 17429
USER, PASSWORD = "algowinthis", "unicorns578"

#HOST, PORT = "localhost", 17429
#USER, PASSWORD = "a", "a"

sock = connect(HOST, PORT, USER, PASSWORD)

send(sock, "ACCELERATE 1 1")
config = configurations(send(sock, "CONFIGURATIONS"))
mapwidth = config['mapwidth']
mapheight = config['mapheight']
scandelay = config['scandelay']
targetx = -1
targety = -1
num_mines = 0

while(True):
    x = random.randint(0, mapwidth)
    y = random.randint(0, mapwidth)
    sc = send(sock, "SCAN {0} {1}".format(x, y))
    if "ERROR" not in sc:
        sc = scan(sc)
        if (targetx < 0 and len(sc['mines']) > 0):
            targetx = sc['mines'][0]['x']
            targety = sc['mines'][0]['y']
    st = status(send(sock, "STATUS"))
    d = distance_donut(st['x'], st['y'], targetx, targety, mapwidth, mapheight)

    #print("Num Mines: {0}".format(num_mines))
    if (targetx > 0):
        speed = min(1, d / (mapwidth / 20))
        rad = calc_rad_donut(st['x'], st['y'], targetx, targety, mapwidth, mapheight)
        send(sock, "ACCELERATE {0} {1}".format(rad, speed))
        print("Speed: {0}".format(speed))
        print("Radians: {0}".format(rad / math.pi))
    print("Target: {0}, {1}".format(targetx, targety))
    print("Me: {0}, {1}".format(st['x'], st['y']))
    print("Distance: {0}".format(d))
    if (d < 10):
        targetx = -1
        targety = -1
        send(sock, "ACCELERATE 1 1")
    print("")
    #time.sleep(0.5)