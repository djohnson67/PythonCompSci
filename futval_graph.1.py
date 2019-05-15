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
    win.setCoords(-1.75,-200,11.5,10400)
    Text(Point(-1,0),'0.0K').draw(win)
    Text(Point(-1,2500),'2.5K').draw(win)
    Text(Point(-1,5000),'5.0K').draw(win)
    Text(Point(-1,7500),'7.5K').draw(win)
    Text(Point(20,10000),'10.0K').draw(win)

    #draw bar for init principal
    bar = Rectangle(Point(0,0),Point(1,principal))
    bar.setFill('Green')
    bar.setWidth(2)
    bar.draw(win)
    #draw bars for successive years
    for year in range(1,11):
        #calculate next year
        principal = principal * (1 + apr)
        #draw bar for this value
        bar = Rectangle(Point(year,0),Point(year+1, principal))
        bar.setFill('Green')
        bar.setWidth(2)
        bar.draw(win)
    
    input("Press <Enter> to quit")
    win.close()

main()




