#bubblesplash.py
#A game which relies on reflexes to pop 'bubbles'
import sys
sys.path.insert(0, 'C:\\Users\\joshm\\OneDrive\\Documents\\NSC\\spring 2022\\Computer Science')
from graphics import *
from timer import Timer
from game_modes import Gamemodes
from gamemodemenu import Menu
from difficultyselection import Difficulty

def main():
    while True:
        #Allow user to choose the game mode
        modeselection = Menu('Bubble Splash!', 'blue')
        mode = modeselection.interact()
        modeselection.close()
        #Takes the selected gamemode and runs it.
        if mode == 'Free Play':
            #Implement a countdown timer before game window is created and game is started
            timer = Timer('Free Play\nHave fun!')
            timer.countdown(5, 'GO')
            gamewin = GraphWin('Bubble Splash!', 1000, 800)
            gamewin.setCoords(-10,-10,510,510)
            game = Gamemodes(gamewin)
            Text(Point(12, 470), 'Click time: ').draw(gamewin)
            Text(Point(2, 500), 'Pops: ').draw(gamewin)
            Text(Point(8, 490), 'Misses: ').draw(gamewin)
            Text(Point(20, 480), 'Accuracy ratio: ').draw(gamewin)
            Text(Point(28, 460), 'Average click time: ').draw(gamewin)
            Text(Point(45, 450), 'ESC, then click bubble to quit').draw(gamewin)
            game.freeplay()
        elif mode == 'Classic':
            #Allows user to select difficulty
            difficultymenu = Difficulty()
            difficulty = difficultymenu.interact()
            difficultymenu.close()
            if difficulty == 'Easy':
                #Implement a countdown timer before game window is created and game is started
                timer = Timer('Classic: Easy\nBeware of the Red Bubbles!')
                timer.countdown(5, 'GO')
                gamewin = GraphWin('Bubble Splash!', 1000, 800)
                gamewin.setCoords(-10,-10,510,510)
                game = Gamemodes(gamewin)
                game.classic(1.5)
            elif difficulty == 'Hard':
                #Implement a countdown timer before game window is created and game is started
                timer = Timer('Classic: Hard\nTime is of the essence!')
                timer.countdown(5, 'GO')
                gamewin = GraphWin('Bubble Splash!', 1000, 800)
                gamewin.setCoords(-10,-10,510,510)
                game = Gamemodes(gamewin)
                game.classic(0.8)
        elif mode == 'Splash!':
            #Allows user to select difficulty
            difficultymenu = Difficulty()
            difficulty = difficultymenu.interact()
            difficultymenu.close()
            if difficulty == 'Easy':
                #Implement a countdown timer before game window is created and game is started
                timer = Timer('Splash!: Easy\nSize perception time!')
                timer.countdown(5, 'GO')
                gamewin = GraphWin('Bubble Splash!', 1000, 800)
                gamewin.setCoords(-10,-10,510,510)
                game = Gamemodes(gamewin)
                game.splash(15)
            elif difficulty == 'Hard':
                #Implement a countdown timer before game window is created and game is started
                timer = Timer('Splash!: Hard\nHope you like bubbles!')
                timer.countdown(5, 'GO')
                gamewin = GraphWin('Bubble Splash!', 1000, 800)
                gamewin.setCoords(-10,-10,510,510)
                game = Gamemodes(gamewin)
                game.splash(20)
        elif mode == 'Rules':
            #Establishes the rules of the games and allows the user to read.
            rulewin = GraphWin('Rules', 640, 640)
            rulewin.setCoords(0,-1,10,29)
            rules = open('bubblesplashrules.txt', 'r')
            for i in range(1, 28):
                Text(Point(5, 29-i), rules.readline()).draw(rulewin)
            rules.close()
            Text(Point(5, 0), "Press 'Escape' to exit").draw(rulewin)
            while True:
                if rulewin.checkKey() == 'Escape':
                    rulewin.close()
                    break
                else:
                    pass

        elif mode == 'Exit':
            break




main()
