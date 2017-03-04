from transmit import connect, send
from parser import *
from navigation import *
from mines import *
import json
import random
import time
import math

HOST, PORT = "codebb.cloudapp.net", 17429
USER, PASSWORD = "algowinthis", "unicorns578"

#fstatus = open('statusdata', 'w')
#fminelist = open('minedata', 'w')
#fscoreboard = open('scoredata', 'w')

#HOST, PORT = "localhost", 17429
#USER, PASSWORD = "a", "a"

sock = connect(HOST, PORT, USER, PASSWORD)

send(sock, "ACCELERATE 1 1")
config = configurations(send(sock, "CONFIGURATIONS"))
mapwidth = config['mapwidth']
mapheight = config['mapheight']
scandelay = config['scandelay']
bombdelay = config['bombdelay']
print(bombdelay)
minelist = []
visited = []
closest = {"x": -1,"y": -1}
iii = 0
start_brake = False

while(True):
    x = random.randint(0, mapwidth)
    y = random.randint(0, mapwidth)
    sc = send(sock, "SCAN {0} {1}".format(x, y))
    if "ERROR" not in sc:
        sc = scan(sc)
        minelist = update_minelist(sc['mines'], minelist, visited)[0]
    st = status(send(sock, "STATUS"))
    minelist = update_minelist(st['mines'], minelist, visited)[0]
    #fstatus.write(json.dumps(st))
    #fstatus.write('\n')

    if (iii % 10 == 0):
        print("Num Mines To Explore: {0}".format(len(minelist)))
        print("Visited Mines: {0}".format(len(visited)))
        print("Speed: {0}".format(math.sqrt(st['dx']**2 + st['dy']**2)))
        print("")
        #sb = scoreboard(send(sock, "SCOREBOARD"))
        #fscoreboard.write(json.dumps(sb))
        #fscoreboard.write('\n')
    if (len(minelist) > 0 and closest['x'] < 0):
        closest = closest_mine(st['x'], st['y'], minelist, mapwidth, mapheight)
        minelist.remove(closest)
        visited.append(closest)
    else:
        d = distance_donut(st['x'], st['y'], closest['x'], closest['y'], mapwidth, mapheight)
        if start_brake and vel(st['dx'], st['dy']) < 0.5:
            start_brake = False
            print("Full Thrust")
        if (start_brake):
            speed = 0
        else:
            speed = 1
        rad = calc_rad_donut(st['x'], st['y'], closest['x'], closest['y'], st['dx'], st['dy'], mapwidth, mapheight, 10)
        #print(closest)
        #print(rad)
        if (d < 50):
            send(sock, "ACCELERATE {0} {1}".format(rad, -1))
            print("Reverse Thrust")
            time.sleep(2)
            print("Idle")
            closest = {"x": -1,"y": -1}
            start_brake = True
            speed = 0
        send(sock, "ACCELERATE {0} {1}".format(rad, speed))

    if len(visited) >= 20:
        minelist = minelist + visited[0:10]
        visited = visited[10:]
    if len(minelist) >= 30:
        minelist = []
    #fminelist.write(json.dumps(minelist + visited))
    #fminelist.write('\n')
    iii += 1