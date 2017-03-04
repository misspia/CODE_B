from navigation import *

def update_minelist(viewed,master,visited):
    newmaster = master
    new = 0
    for i in range(len(viewed)):
        if (not viewed[i] in master) and (not viewed[i] in visited):
            newmaster.append(viewed[i])
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