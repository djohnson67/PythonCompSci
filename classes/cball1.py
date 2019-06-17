# cball1.py
from math import sin, cos, radians

def main():
    angle = eval(input('Enter the launch angle (in degrees): '))
    vel = eval(input('Enter the initial velocity (in meters/sec: '))
    h0 = eval(input('Enter rthe inital height (in meters): '))
    time = eval(input('Entger the time inteval between position calculations: '))

    #convert angle to radiaon
    theta = radians(angle)

    #set the initial positions and velocities in x and y directions
    xpos = 0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    gravity = 9.8

    #loop until the ball hits the ground
    while ypos >= 0.0:
        #calulate positino and velocitiy in seconds
        xpos = xpos + time * xvel
        yvel1 = yvel - time * gravity
        ypos = ypos + time * (yvel + yvel1)/2.0
        yvel = yvel1

    print('\nDistance traveled: {0:0.1f} meters.'.format(xpos))
        

