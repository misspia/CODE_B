import math
import random

# Given ship at (x1, y1) and target at (x2, y2)
# Finds angle between them relative to the vector (1, 0)
def calc_rad(x1, y1, x2, y2):
    rad = math.atan2(y1 - y2, x2 - x1)
    if (rad < 0):
        rad += 2 * math.pi
    return rad

# Given ship at (x1, y1) and target at (x2, y2)
# and ship moving at (dx, dy)
# Finds angle to direct ship towards target
def calc_move_rad(x1, y1, x2, y2, dx, dy):
    x3 = x2 - x1
    y3 = y2 - y1
    return calc_rad(dx, dy, x3, y3)

def navigate(status):
    x = status['x']
    y = status['y']
    dx = status['dx']
    dy = status['dy']
    players = status['players']

    if len(players) > 0:
        first = players[0]
        return calc_move_rad(x, y, first['x'], first['y'], dx, dy)
    else:
        return random.random() * math.pi / 2