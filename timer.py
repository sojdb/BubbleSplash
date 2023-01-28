#timer.py
#creates a functioning timer in a graphics window
import sys
sys.path.insert(0, 'C:\\Users\\Josh\\Documents\\College\\CS')
from graphics import *
import time

class Timer():

    def __init__(self, description):
        self.win = GraphWin('Timer', 250, 250)
        self.win.setCoords(0,0,10,10)
        self.timelabel = Text(Point(5,5), '')
        self.timelabel.draw(self.win)
        Text(Point(5,2), description).draw(self.win)


    def countdown(self, sec, label):
        #Creates a time that counts down to 0 from a specified time
        while True:
            time.sleep(1)
            for i in range(sec, 0, -1):
                self.timelabel.setText(str(i))
                self.timelabel.setSize(30)
                time.sleep(1)
            self.timelabel.setText(label)
            time.sleep(1)
            self.win.close()
            break

    def countup(self):
        #Creates a timer that counts up to a specified time
        while True:
            for i in range(0, self.time):
                time.sleep(1)
                self.timelabel.setText(str(i))
                self.timelabel.setSize(30)

    def startTime(self):
        self.start = time.time()
        return self.start

    def updateTime(self):
        elapsed_time = time.time() - self.start
        return elapsed_time

    def close(self):
        self.win.close()
