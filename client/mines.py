from navigation import *

def update_minelist(viewed,master,dgg, visited):
    newmaster = master
    newdgg = dgg
    new = 0
    for i in range(len(viewed)):
        dictentry = {'x': viewed[i]['x'], 'y': viewed[i]['y']}
        if (not dictentry in master) and (not dictentry in visited) and (viewed[i]['name'] != 'algowinthis'):
            if viewed[i]['name'] == 'exodia' or viewed[i]['name'] == 'duckduckgoose':
                dgg.append(dictentry)
            newmaster.append(dictentry)
            new += 1
    return [newmaster,newdgg,new]

def closest_mine(x,y,minelist,width,height):
    shortest_distance=width+height
    shortest_index = -1
    if len(minelist)==0:
        return {}
    else:
        for i in range(len(minelist)):
            distance=distance_donut(x,y,minelist[i]["x"],minelist[i]["y"],width,height)
            angle = calc_rad_donut(x,y,minelist[i]["x"],minelist[i]["y"],0,0,width,height,0)
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