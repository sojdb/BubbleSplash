import sys
sys.path.insert(0, 'C:\\Users\\Josh\\Documents\\College\\CS')
from graphics import *
from button import Button

class Difficulty():
    """
    A custom window for allowing the user to choose which difficulty they play
    """

    def __init__(self):
        self.win = win = GraphWin("Gamemodes", 200, 300)
        win.setCoords(0,0, 5, 5)

        self.easy = Button(win, Point(2.5, 3.5), 3, .8, 'Easy')
        self.easy.activate()

        self.hard = Button(win, Point(2.5, 1.5), 3, .8, 'Hard')
        self.hard.activate()

    def interact(self):
        """
        Wait for the user to click difficulty Button, Return a string indicating
        which button was clicked
        """
        while True:
            pt = self.win.getMouse()
            if self.easy.clicked(pt):
                return "Easy"
            elif self.hard.clicked(pt):
                return 'Hard'

    def close(self):
        self.win.close()
