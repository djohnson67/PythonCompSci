# projectile.py
'''projectile.py
Provides a simple class for modeling the flight of the projectiles '''
from math import sin, cos, radians

class Projectile:
  ''' Simulates the flight of simple projectile near the earths surface '''

  def __init__(self, angle, velocity, height):
    '''create projectile with given launch angle, velocity, and height '''
    self.xpos = 0.0
    self.ypos = height
    theta = radians(angle)
    self.xvel = velocity * cos(theta)
    self.yvel = velocity * sin(theta)

  def update(self, time):
    ''' update state of projectile'''
    gravity = 9.8
    self.xpos = self.xpos + time * self.xvel
    yvel1 = self.yvel - gravity * time
    self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
    self.yvel = yvel1

  def getY(self):
    '''returns the y position'''
    return self.ypos

  def getX(self):
    return self.xpos
