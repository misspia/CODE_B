import math
import random

# Given ship at (x1, y1) and target at (x2, y2)
# Finds angle between them relative to the vector (1, 0)
def calc_rad(x1, y1, x2, y2):
    rad = math.atan2(y2 - y1, x2 - x1)
    if (rad < 0):
        rad += 2 * math.pi
    return rad

def calc_rad_donut(x1, y1, x2, y2, width, height):
    dx = abs(x1 - x2)
    if (dx > width/2):
        if x2 > x1:
            x2 -= width
        else:
            x2 += width
    dy = abs(y1 - y2)
    if (dy > height/2):
        if y2 > y1:
            y2 -= height
        else:
            y2 += height

    return calc_rad(x1, y1, x2, y2)

def distance(x1, y1, x2, y2):
    return math.sqrt((y2 - y1)**2 + (x2 - x1)**2)

def distance_donut(x1, y1, x2, y2, width, height):
    dx = abs(x1 - x2)
    if (dx > width/2):
        dx = width - dx
    dy = abs(y1 - y2)
    if (dy > height/2):
        dy = height - dx

    return math.sqrt(dx**2 + dy**2)

#print(calc_rad_donut(500, 9000, 500, 9000, 10000, 10000) / (math.pi))
#print(calc_rad_donut(500, 9000, 9000, 9000, 10000, 10000) / (math.pi))
#print(calc_rad_donut(500, 9000, 9000, 500, 10000, 10000) / (math.pi))
#print(calc_rad_donut(500, 9000, 500, 500, 10000, 10000) / (math.pi))