import sys
sys.path.insert(0, 'C:\\Users\\Josh\\Documents\\College\\CS')
from graphics import *
from button import Button

class Menu():
    """
    A custom window for allowing the user to choose which gamemode they play
    """

    def __init__(self, title, color):
        self.win = win = GraphWin("Gamemodes", 200, 300)
        win.setCoords(0,0, 15,13)

        gametitle = Text(Point(7.5, 12), title)
        gametitle.draw(win)
        gametitle.setTextColor(color)

        self.classic = Button(win, Point(7.5,10), 12, 1, "Classic")
        self.classic.activate()

        self.splash = Button(win, Point(7.5,8), 12, 1, "Splash!")
        self.splash.activate()

        self.freeplay = Button(win, Point(7.5, 6), 12, 1, 'Free Play')
        self.freeplay.activate()

        self.rules = Button(win, Point(7.5, 4), 12, 1, 'Rules')
        self.rules.activate()

        self.exit = Button(win, Point(7.5, 2), 12, 1, 'Exit')
        self.exit.activate()

    def interact(self):
        """
        Wait for the user to click gamemode Button, Return a string indicating
        which button was clicked
        """
        while True:
            pt = self.win.getMouse()
            if self.classic.clicked(pt):
                return "Classic"
            elif self.splash.clicked(pt):
                return "Splash!"
            elif self.freeplay.clicked(pt):
                return "Free Play"
            elif self.exit.clicked(pt):
                return 'Exit'
            elif self.rules.clicked(pt):
                return 'Rules'

    def close(self):
        self.win.close()
