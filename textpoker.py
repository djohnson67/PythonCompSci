from pokerapp import PokerApp
from pokerapp import Dice
from textinterface import TextInterface

inter = TextInterface()
app = PokerApp(inter)
ddd = Dice()
app.run()