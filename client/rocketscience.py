import math

def rocketscience(x,y,dx,dy,tx,ty):
    
    
    d = [tx - x, ty - y]
    d_norm = [d[0]/math.sqrt(d[0]**2+d[1]**2),d[1]/math.sqrt(d[0]**2+d[1]**2)]
    d_angel = [math.acos(d_norm[0]),math.asin(d_norm[1])]
    
    vec_norm = [dx/math.sqrt(dx**2+dy**2),dy/math.sqrt(dx**2+dy**2)]
    vec_angle = [math.acos(vec_norm),math.asin(vec_norm)]
    
    
    return target_angle