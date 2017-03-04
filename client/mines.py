from navigation import *

def update_minelist(viewed,master):
    newmaster = master
    new = 0
    for i in range(len(viewed)):
        if (not {'x': viewed[i]['x'], 'y': viewed[i]['y']} in master) and (viewed[i]['name'] != 'algowinthis'):
            newmaster.append({'x': viewed[i]['x'], 'y': viewed[i]['y']})
            new += 1
    return [newmaster,new]

def closest_mine(x,y,minelist,width,height):
    shortest_index=0
    shortest_distance=width+height
    if len(minelist)==0:
        return {}
    else:
        for i in range(len(minelist)):
            distance=distance_donut(x,y,minelist[i]["x"],minelist[i]["y"],width,height)
            if distance < shortest_distance:
                shortest_distance=distance
                shortest_index=i
        return minelist[shortest_index]

def furthest_mine(x,y,minelist,width,height):
    shortest_index=0
    shortest_distance=0
    if len(minelist)==0:
        return {}
    else:
        for i in range(len(minelist)):
            distance=distance_donut(x,y,minelist[i]["x"],minelist[i]["y"],width,height)
            if distance > shortest_distance:
                shortest_distance=distance
                shortest_index=i
        return minelist[shortest_index]