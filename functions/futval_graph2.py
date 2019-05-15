from graphics import *

def main():
    #intro
    print('This program plots the growth of a 10-year investment')

    #get the principal and interest data
    principal = eval(input('Enter the initital principal: '))
    apr = eval(input('Enter the annual interst rate: '))
    color = 'Blue'

    #create graphics window with labels on left side
    win = createLabelWindow()
    #draw bar for init principal
    drawBar(win,0,principal,color)
    #bar = Rectangle(Point(0,0),Point(1,principal))
   
    for year in range(1,11):
        #calculate next year
        principal = principal * (1 + apr)
        #draw bar for this value
        drawBar(win,year,principal,color)
        
    
    input("Press <Enter> to quit")
    win.close()

def drawBar(window, year, height,color):
    #draw a bar for the given year at the given height
    bar = Rectangle(Point(year,0),Point(year+1, height))
    bar.setFill(color)
    bar.setWidth(2)
    bar.draw(window)

def createLabelWindow():
    #returns a graph window title and labels drawn
    win = GraphWin('Investment Growth Chart', 320, 240)
    win.setBackground('White')
    win.setCoords(-1.75,-200,11.5,10400)
    Text(Point(-1,0),'0.0K').draw(win)
    Text(Point(-1,2500),'2.5K').draw(win)
    Text(Point(-1,5000),'5.0K').draw(win)
    Text(Point(-1,7500),'7.5K').draw(win)
    Text(Point(20,10000),'10.0K').draw(win)
    return win


main()




