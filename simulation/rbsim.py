# rbsim.py
from random import random

def printIntro():
  print('This program simulates a game of rqcquetball between two')
  print('players called "A" and "B". The abilities of each player is')
  print('indicated by a probabilty (a number between 0 and 1) that')
  print('the player wins the point  when serving. Player A always has the first serve')

def getInputs():
  #returns three simulation inputs
  a = eval(input('What is the probabilty A wins a serve? '))
  b = eval(input('What ist the probability B wins a serve? '))
  n = int(input('How many games to simulate? '))
  return a,b,n

def simNGames(n, probA,probB):
  #simulates n games and returns winsA and winsB
  winsA = 0
  winsB = 0
  for i in range(n):
    scoreA, scoreB = simOneGame(probA,probB)
    if(scoreA>scoreB):
      winsA += 1
    else:
      winsB += 1
  return winsA, winsB

def simOneGame(probA,probB):
  scoreA = 0
  scoreB = 0
  serving = 'A'
  while not gameOver(scoreA,scoreB):
    if serving == 'A':
      if random() < probA: 
        scoreA += 1 #A wins the serve and gets a point
      else:
        serving = 'B' #A loses the serve - B takes over
    else:
      if random() < probB:
        scoreB += 1 #B wins the server and gets the point
      else:
        serving = 'A'#B loses the serve - A takes over
  
  return scoreA, scoreB

def gameOver(a,b):
  #a and b represent score for a racquetball game
  return a==15 or b==15

def printSummary(winsA,winsB):
  #prints summary of wins for each player
  n = winsA + winsB
  print('\nGames simulated: ',n)
  print('Wins for A: {0} ({1:0.1%})'.format(winsA, winsA/n))
  print('Wins for B: {0} ({1:0.1%})'.format(winsB, winsB/n))

def main():
  printIntro()
  probA, probB, n = getInputs()
  winA,winB = simNGames(n, probA, probB)
  printSummary(winA,winB)

if __name__ == '__main__': main()