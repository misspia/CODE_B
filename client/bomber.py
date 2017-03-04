def bomb_break(x,y,dx,dy):
    bx=x+3*dx
    by=y+3*dy
    return {"x":bx,"y":by}

def bomb_boost(x,y,dx,dy):
    bx=x-dx
    by=y-dy
    return {"x":bx,"y":by}