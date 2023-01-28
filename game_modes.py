#gamemodes for the game BubbleSplash
import sys
sys.path.insert(0, 'C:\\Users\\Josh\\Documents\\College\\CS')
from graphics import *
import time
import random
from bubble import Bubble

class Gamemodes():

    def __init__(self, win):
        self.win = win
        self.timelabel = Text(Point(43, 470), '')
        self.timelabel.draw(win)
        self.pointlabel = Text(Point(17, 500), '')
        self.pointlabel.draw(win)
        self.misslabel = Text(Point(26, 490), '')
        self.misslabel.draw(win)
        self.accuracylabel = Text(Point(54, 480), '')
        self.accuracylabel.draw(win)
        self.avgtimelabel = Text(Point(72, 460), '')
        self.avgtimelabel.draw(win)


    def freeplay(self):
        #initiates game and variables
        start_time = time.time()
        point, miss = 0, 0
        timelist = []
        while True:
            #create exit criteria
            exit = self.win.checkKey()
            if exit == 'Escape':
                self.win.close()
                break
            else:
                #establishes the random placement of the bubbles
                cx, cy = random.randint(0,500), random.randint(0,500)
                radius = random.randint(10, 30)
                bubble = Bubble(self.win, radius, cx, cy, 'lightblue')
                bubble.drawBubble()
                while True:
                    #Adjusts variables based on if the bubble was clicked
                    p = self.win.checkMouse()
                    if p == None:
                        pass
                    else:
                        distance = bubble.click(self.win, p)
                        if (distance>=0):
                            bubble.undrawBubble()
                            point += 1
                            self.pointlabel.setText(str(point))
                            try:
                                accuracy = round(float(point/miss), 2)
                            except ZeroDivisionError:
                                accuracy = round(float(point), 2)
                            self.accuracylabel.setText(str(accuracy))
                            break
                        else:
                            miss += 1
                            self.misslabel.setText(str(miss))
                            try:
                                accuracy = round(float(point/miss), 2)
                            except ZeroDivisionError:
                                accuracy = round(float(point), 2)
                            self.accuracylabel.setText(str(accuracy))
                            continue
                #calculates the time variables
                elapsed_time = time.time() - start_time
                timelist.append(elapsed_time)
                avgtime = sum(timelist)/len(timelist)
                self.avgtimelabel.setText(str(round(float(avgtime), 3)))
                start_time = time.time()
                self.timelabel.setText(str(round(float(elapsed_time), 4)))

    def classic(self, time_interval):
        #establishes variables
        point = 0
        miss = 0
        startgame = time.time()
        continuegame = True
        time.sleep(1)
        while continuegame:
            #Sets the games time limit
            game_time = time.time() - startgame
            if game_time <= 30:
                #Creates the various bubbles with random placement
                #As well as decides what bubble will be drawn.
                cx, cy = random.randint(0,500), random.randint(0,500)
                radius = random.randint(10, 30)
                chance = random.randint(0,100)
                redBubble = Bubble(self.win, radius, cx, cy, 'red')
                pinkBubble = Bubble(self.win, radius, cx, cy, 'pink')
                bubble = Bubble(self.win, radius, cx, cy, 'lightblue')
                if chance <= 15:
                    redBubble.drawBubble()
                    start_time = time.time()
                    click = True
                    while click:
                        elapsed_time = time.time() - start_time
                        p = self.win.checkMouse()
                        if p == None:
                            if elapsed_time >= time_interval:
                                redBubble.undrawBubble()
                                click = False
                                break
                            else:
                                pass
                        else:
                            distance = redBubble.click(self.win, p)
                            while True:
                                if (distance>=0):
                                    redBubble.undrawBubble()
                                    Text(Point(250, 300), 'Oh no!').draw(self.win)
                                    continuegame = False
                                    click = False
                                    break
                                elif (distance<0):
                                    redBubble.undrawBubble()
                                    continuegame = False
                                    click = False
                                    break
                                else:
                                    pass
                elif chance >= 90:
                    pinkBubble.drawBubble()
                    start_time = time.time()
                    click = True
                    while click:
                        elapsed_time = time.time() - start_time
                        p = self.win.checkMouse()
                        if p == None:
                            if elapsed_time >= time_interval:
                                pinkBubble.undrawBubble()
                                click = False
                                break
                            else:
                                pass
                        else:
                            distance = pinkBubble.click(self.win, p)
                            while True:
                                if (distance>=0):
                                    pinkBubble.undrawBubble()
                                    point = point *2
                                    click = False
                                    break
                                elif (distance<0):
                                    pinkBubble.undrawBubble()
                                    continuegame = False
                                    click = False
                                    break
                                else:
                                    pass
                else:
                    bubble.drawBubble()
                    start_time = time.time()
                    click = True
                    while click:
                        elapsed_time = time.time() - start_time
                        p = self.win.checkMouse()
                        if p == None:
                            if elapsed_time >= time_interval:
                                bubble.undrawBubble()
                                continuegame = False
                                click = False
                                break
                            else:
                                pass
                        else:
                            distance = bubble.click(self.win, p)
                            while True:
                                if (distance>=0):
                                    bubble.undrawBubble()
                                    point += 1
                                    click = False
                                    break
                                elif (distance<0):
                                    bubble.undrawBubble()
                                    continuegame = False
                                    click = False
                                    break
                                else:
                                    pass
            elif game_time >30:
                break
        Text(Point(250, 280), 'GAME OVER!').draw(self.win)
        time.sleep(2)
        Text(Point(250, 250), 'Score = {}'.format(str(point))).draw(self.win)
        time.sleep(3)
        self.win.close()

    def splash(self, amount):
        #Creates the bubbles in a list of largest to smallest, and draws them to the screen.
        start_time = time.time()
        bubble = []
        prev = 48
        latter = 50
        for i in range(amount):
            cx, cy = random.randint(0,500), random.randint(0,500)
            radius = random.randint(prev, latter)
            bubble.append(Bubble(self.win, radius, cx, cy, 'lightblue'))
            bubble[i].drawBubble()
            prev -= 2
            latter -= 2
        while True:
            #Allows the user to click the bubbles in the order that the list specified.
            for i in range(amount):
                elapsed_time = time.time() - start_time
                if elapsed_time > 15:
                    Text(Point(250, 250), 'GAME OVER! You lose!').draw(self.win)
                    time.sleep(3)
                    self.win.close()
                    break
                else:
                    while True:
                        p = self.win.checkMouse()
                        if p == None:
                            pass
                        else:
                            distance = bubble[i].click(self.win, p)
                            if (distance>=0):
                                bubble[i].undrawBubble()
                                break
                            else:
                                continue
            if elapsed_time <= 15:
                #Creates win criteria
                Text(Point(250, 250), 'Congrats! Time left was {} seconds'.format(round(float(15-elapsed_time)),3)).draw(self.win)
                time.sleep(3)
                self.win.close()
                break
            else:
                break
