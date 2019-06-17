#cball4.py
from projectile import Projectile
      
def getInputs():
  a = eval(input('Enter the launch angle (in degrees): '))
  v = eval(input('Enter the initial velocity (in meters/sec: '))
  h = eval(input('Enter rthe inital height (in meters): '))
  t = eval(input('Entger the time inteval between position calculations: '))

  return a,v,h,t

def main():
  angle ,vel,h0,time = getInputs()
  cBall = Projectile(angle,vel,h0)

  #loop until the ball hits the ground
  while cBall.getY() >= 0:
    cBall.update(time)

  print('\nDistance traveled: {0:0.1f} meters.'.format(cBall.getX()))
        
if __name__ == '__main__':
  main()
