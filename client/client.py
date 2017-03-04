from transmit import connect, send
from parser import *
from navigation import *
from mines import *
from rocketscience import *
import random
import time
import math

#HOST, PORT = "codebb.cloudapp.net", 17429
#USER, PASSWORD = "algowinthis", "unicorns578"

HOST, PORT = "localhost", 17429
USER, PASSWORD = "a", "a"

sock = connect(HOST, PORT, USER, PASSWORD)

send(sock, "ACCELERATE 1 1")
config = configurations(send(sock, "CONFIGURATIONS"))
mapwidth = config['mapwidth']
mapheight = config['mapheight']
scandelay = config['scandelay']
minelist = []
visited = []
closest = {"x": -1,"y": -1}
iii = 0
stopped = False

while(True):
    x = random.randint(0, mapwidth)
    y = random.randint(0, mapwidth)
    sc = send(sock, "SCAN {0} {1}".format(x, y))
    if "ERROR" not in sc:
        sc = scan(sc)
        minelist = update_minelist(sc['mines'], minelist, visited)[0]
    st = status(send(sock, "STATUS"))

    if (iii % 10 == 0):
        print("Num Mines To Explore: {0}".format(len(minelist)))
        print("Visited Mines: {0}".format(len(visited)))
    if (len(minelist) > 0 and closest['x'] < 0):
        closest = closest_mine(st['x'], st['y'], minelist, mapwidth, mapheight)
        minelist.remove(closest)
        visited.append(closest)
    else:
        d = distance_donut(st['x'], st['y'], closest['x'], closest['y'], mapwidth, mapheight)
        speed = min(1, d / (mapwidth / 20))
        #rad = calc_rad_donut(st['x'], st['y'], closest['x'], closest['y'], mapwidth, mapheight)
        rad = rocketscience(st['x'],st['y'],st['dx'],st['dy'],closest['x'],closest['y'],mapwidth,mapheight,0.01,0.9)
        if (iii % 10 == 0):
            print(st['x'],st['y'])
            print(closest['x'],closest['y'])
            print(rad)
        send(sock, "ACCELERATE {0} {1}".format(rad, speed))
        if (d < 50 and not stopped):
            speed = 0
            send(sock, "ACCELERATE {0} {1}".format(rad, speed))
            stopped = True
            time.sleep(0.5)
        if (d < 10):
            closest = {"x": -1,"y": -1}
            stopped = False

    if len(visited) >= 20:
        minelist = minelist + visited[0:10]
        visited = visited[10:]
    iii += 1