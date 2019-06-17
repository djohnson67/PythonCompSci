# button.py
from graphics import *

class Button:
    ''' A button is a labeled rectangle in a window'''
    def __init__(self, win, center, width, height, label):
        '''creates a rectangle button'''
        
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w,x-w
        self.ymax, self.ymin = y+h,y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        '''returns true if button active and p is insided'''
        return(self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)
    
    def getLabel(self):
        '''return label string of button'''
        return self.label.getText()

    def activate(self):
        '''sets biutton to active'''
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        '''sets button to inactive'''
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False

    
