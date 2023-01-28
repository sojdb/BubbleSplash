#button2.py
#Creates a button class that can create graphical buttons.
import sys
sys.path.insert(0, 'C:\\Users\\Josh\\Documents\\College\\CS')
from graphics import *
import random


class Bubble():

    def __init__(self, win, radius, cx, cy, color):
        self.bubble = Circle(Point(cx, cy), radius)
        self.bubble.setFill(color)
        self.radius = radius
        self.cx, self.cy = cx, cy
        self.win = win

    def click(self, win, p):
        #Determines if the bubble has been clicked
        px, py = p.getX(), p.getY()
        distance = self.radius**2 - ((self.cx-px)**2+(self.cy-py)**2)
        return distance


    def undrawBubble(self):
        self.bubble.undraw()

    def drawBubble(self):
        self.bubble.draw(self.win)


    def score(self):
        return self.point, self.miss
