#seen_mines = [{"x":1700,"y":2000}]
#master_mines = [{"x":1000,"y":2000},{"x":1500,"y":2500}]
#update_minelist(seen_mines,master_mines)

def update_minelist(viewed,master):
    newmaster = master
    new = 0
    for i in range(len(viewed)):
        if not viewed[i] in master:
            new += 1
            newmaster.append(viewed[i])
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