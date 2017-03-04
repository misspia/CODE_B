import math

#osc_trigger the minimum amount of radians bewteen trajectory and line-of-sight angle
#  before oscillation principle kicks in
#osc_weight is between 0 and 1, 0.9 => average with 0.9 weighted on vector

def rocketscience2(x,y,dx,dy,tx,ty,width,height,osc_trigger=0.3,osc_weight=0.2):

    ddx = abs(x - tx)
    if (ddx > width/2):
        if tx > x:
            tx -= width
        else:
            tx += width
    ddy = abs(y - ty)
    if (ddy > height/2):
        if ty > y:
            ty -= height
        else:
            ty += height

    d = [tx - x, ty - y]
    d_norm = [d[0]/math.sqrt(d[0]**2+d[1]**2),d[1]/math.sqrt(d[0]**2+d[1]**2)]
    d_angle = math.atan2(d[1], d[0])
    if (d_angle < 0):
        d_angle += 2 * math.pi

    vec_norm = [dx/math.sqrt(dx**2+dy**2),dy/math.sqrt(dx**2+dy**2)]
    vec_angle = math.atan2(d[1], d[0])
    if (vec_angle < 0):
        vec_angle += 2 * math.pi
    
    #print(d_angle)
    #print(d_norm)
    #print(vec_norm)
    
    accel = [vec_norm[0]-d_norm[0],vec_norm[1]-d_norm[1]]
    
    if abs(d_angle - vec_angle) < osc_trigger:
        accel_angle = osc_weight*(d_angle-vec_angle)+d_angle
        #accel_angle = (1-osc_weight)*d_angle + osc_weight*vec_angle
    else:
        accel_angle = math.atan2(accel[1], accel[0])
        if (accel_angle < 0):
            accel_angle += 2 * math.pi
    
    return accel_angle