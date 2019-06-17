# cball1.py
from math import sin, cos, radians

def getInputs():
  angle = eval(input('Enter the launch angle (in degrees): '))
  vel = eval(input('Enter the initial velocity (in meters/sec: '))
  h0 = eval(input('Enter rthe inital height (in meters): '))
  time = eval(input('Entger the time inteval between position calculations: '))

  return angle,vel,h0,time

def getXYComponents(vel,angle):
  #convert angle to radiaon 
  theta = radians(angle)
  xvel = vel * cos(theta)
  yvel = vel * sin(theta)
  
  return xvel, yvel

def updateCannonBall(time,xpos,ypos,xvel,yvel):
#calulate positino and velocitiy in seconds
  gravity = 9.8
  xpos = xpos + time * xvel
  yvel1 = yvel - time * gravity
  ypos = ypos + time * (yvel + yvel1)/2.0

  return xpos, ypos, yvel1

def main():
  angle ,vel,h0,time = getInputs()
  xpos, ypos = 0, h0
  
   #set the initial positions and velocities in x and y directions
  xvel,yvel = getXYComponents(vel,angle)

  #loop until the ball hits the ground
  while ypos >= 0:
    xpos, ypos, yvel = updateCannonBall(time,xpos,ypos,xvel,yvel)

  print('\nDistance traveled: {0:0.1f} meters.'.format(xpos))
        

