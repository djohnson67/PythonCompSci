#simulation of a racquetball game
from random import random

class Player:
    #player keeps track of service probability and score
  def __init__(self, prob):
    #create player with probability
    self.__prob = prob
    self.__score = 0

  def winsServe(self):
    #returns a boolean that is True with probability self._prob
    rand = random()
    return  rand <= self.__prob

  def incScore(self):
    #add a point to players score
    self.__score += 1

  def getScore(self):
    #returns player's current score
    return self.__score

class RBallGame:
  #represents a game in progress  - game has two players and keeps track on who is serving
  def __init__(self,probA,probB):
    #create new game with provided probs
    self.__playerA = Player(probA)
    self.__playerB = Player(probB)
    self.__server = self.__playerA #Player A always serves first

  def play(self):
    #play game to completion

    while not self.isOver():
      if self.__server.winsServe():
        self.__server.incScore()
      else:
        self.changeServer()
  
  def isOver(self):
    #returns game is finished(i.e. one of the players has won)
    a,b = self.getScores()
    return a == 15 or b == 15 or \
            (a == 7 and b == 0) or (b==7 and a == 0)
  
  def changeServer(self):
    #switch which player is serving
    if self.__server == self.__playerA:
      self.__server = self.__playerB
    else:
      self.__server = self.__playerA
  
  def getScores(self):
    #returns the current scores of both players
    return self.__playerA.getScore(), self.__playerB.getScore()

class SimStats:
  #handles accumulation of accross multiple (completed) games.
  #tracks the wins and shutouts for each player

  def __init__(self):
    #create a new accumulator for a series of games
    self.__winsA = 0
    self.__winsB = 0
    self.__shutsA = 0
    self.__shutsB = 0

  def update(self, aGame):
    #determine the outcome of aGame and update stats
    a,b = aGame.getScores()
    if a>b: #a wins the game
      self.__winsA +=1;
      if b==0: 
        self.__shutsA += 1;
    else:
      self.__winsB += 1;
      if a == 0:
        self.__shutsB += 1;

  def printReport(self):
    #print a nicely formated report
    n = self.__winsA + self.__winsB
    print('Summary of', n,'games:\n')
    print('          wins (% total)   shutouts (% wins)   ')
    print('--------------------------------------------')
    self.printLine('A',self.__winsA,self.__shutsA,n)
    self.printLine('B',self.__winsB,self.__shutsB,n)

  def printLine(self,label, wins, shuts,n):
    template = 'Player {0}:{1:5}   ({2:5.1%}) {3:11}   {4}'
    if wins == 0: #division by zero check
      shutStr = '----'
    else:
      shutStr = '{0:4.1%}'.format(float(shuts)/wins)
    print(template.format(label,wins,float(wins)/n,shuts,shutStr))

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

def main():
  printIntro()
  probA, probB, n = getInputs()

  #play the game
  stats = SimStats()
  for i in range(n):
    theGame = RBallGame(probA,probB)
    theGame.play()
    stats.update(theGame)

  stats.printReport()
  
main()
input('Press <Enter> to quit')

    
