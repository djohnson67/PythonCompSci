from graphics import *
from button import Button

class Calculator:
  def __init__(self):
    #create window for calc
    win = GraphWin('Calculator')
    win.setCoords(0,0,6,7)
    win.setBackground('slategrey')
    self.win = win
    #create the widgets
    self.__createButtons()
    self.__createDisplay()

  # create a list of buttons
  #start with standard sized buttons
  def __createButtons(self):
    #bSpec gives the center coords and label of buttons
    #each of the () is a tuple
    bSpec = [(2,1,'0'),(3,1,'.'),
              (1,2,'1'),(2,2,'2'),(3,2,'3'),(4,2,'+'),(5,2,'-'),
              (1,3,'4'),(2,3,'5'),(3,3,'6'),(4,3,'*'),(5,3,'/'),
              (1,4,'7'),(2,4,'8'),(3,4,'9'),(4,4,'<-'),(5,4,'C')]
    self.buttons = []
    for (cx,cy,label) in bSpec:
      self.buttons.append(Button(self.win,Point(cx,cy),.75,.75,label))

    #create the larger '=' button
    self.buttons.append(Button(self.win,Point(4.5,1),1.75,.75,'='))

    #activate all buttons
    for b in self.buttons:
      b.activate()

  def __createDisplay(self):
    bg= Rectangle(Point(.5,5.5),Point(5.5,6.5))
    bg.setFill('white')
    bg.draw(self.win)
    text = Text(Point(3,6),'')
    text.draw(self.win)
    text.setFace('courier')
    text.setStyle('bold')
    text.setSize(16)
    self.display = text

  def getButton(self):
    #waits for a button to be clicked and returns the label
    while True:
      p = self.win.getMouse()
      for b in self.buttons:
        if b.clicked(p):
          return b.getLabel() #method exit

  def processButton(self,key):
    #updates the display of the calculator for press of this key
    text = self.display.getText()
    if key == 'C':
      self.display.setText('')
    elif key =='<-':
      #backspace slices off the last character
      self.display.setText(text[:-1])
    elif key == '=':
      #evaluate expression and display the results
      #try statement 'catches' errors in the formula
      try:
        result = eval(text)
      except:
        result = 'Error'
      self.display.setText(str(result))
    else:
      #normal key press append to end of display
      self.display.setText(text+key)

  def run(self):
    #infinent 'event loop' to process button clicks
    while True:
      key = self.getButton()
      self.processButton(key)

#this runs the program
if __name__ == '__main__':
  #first create the calculator
  theCalc = Calculator()
  #now call the run method
  theCalc.run()
