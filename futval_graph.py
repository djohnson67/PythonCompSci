from graphics import *

def main():
    #intro
    print('This program plots the growth of a 10-year investment')

    #get the principal and interest data
    principal = eval(input('Enter the initital principal: '))
    apr = eval(input('Enter the annual interst rate: '))

    #create graphics window with labels on left side
    win = GraphWin('Investment Growth Chart', 320, 240)
    win.setBackground('White')
    Text(Point(20,230),'0.0K').draw(win)
    Text(Point(20,180),'2.5K').draw(win)
    Text(Point(20,130),'5.0K').draw(win)
    Text(Point(20,80),'7.5K').draw(win)
    Text(Point(20,30),'10.0K').draw(win)

    #draw bar for init principal
    height = principal * 0.02
    bar = Rectangle(Point(40,230),Point(65, 230 - height))
    bar.setFill('Green')
    bar.setWidth(2)
    bar.draw(win)
    barwidth = 25
    #draw bars for successive years
    for year in range(1,11):
        #calculate next year
        principal = principal * (1 + apr)
        #draw bar for this value
        x11 = year * 25+40
        height = principal * 0.02
        bar = Rectangle(Point(x11,230),Point(x11+barwidth, 230 - height))
        bar.setFill('Green')
        bar.setWidth(2)
        bar.draw(win)
    
    input("Press <Enter> to quit")
    win.close()

main()




