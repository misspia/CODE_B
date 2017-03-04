import math

#osc_trigger the minimum amount of radians bewteen trajectory and line-of-sight angle
#  before oscillation principle kicks in
#osc_weight is between 0 and 1, 0.9 => average with 0.9 weighted on vector

def rocketscience(x,y,dx,dy,tx,ty,osc_trigger,osc_weight=0.9):

    d = [tx - x, ty - y]
    d_norm = [d[0]/math.sqrt(d[0]**2+d[1]**2),d[1]/math.sqrt(d[0]**2+d[1]**2)]
    d_angel = math.atan(d[1]/d[0])
    
    vec_norm = [dx/math.sqrt(dx**2+dy**2),dy/math.sqrt(dx**2+dy**2)]
    vec_angle = math.atan(vec_norm[1]/vec_norm[0])
    
    print(d_angel)
    print(d_norm)
    print(vec_norm)
    
    accel = [vec_norm[0]-d_norm[0],vec_norm[1]-d_norm[1]]
    
    if abs(d_angel - vec_angel) < osc_trigger:
        accel_angle = (1-osc_weight)*d_angel + osc_weight*vec_angle
    else:
        accel_angle = math.atan(accel[1]/accel[0])
    
    return accel_angle