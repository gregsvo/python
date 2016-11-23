import os
import time
import random
import sys
import colorama


class Game:
    def __init__(self):
        self.history = []
        self.plays = [
            (colorama.Fore.RED + 'Red', 'r'),
            (colorama.Fore.YELLOW +'Yellow', 'y'),
            (colorama.Fore.GREEN +'Green', 'g'),
            (colorama.Fore.BLUE +'Blue', 'b')
        ]

    def show_level(self):
        self.clear()
        for h in self.history:
            print(h[0], end='  ')
            sys.stdout.flush()
            time.sleep(1)
        self.clear()

    def add_move(self):
        self.history.append(random.choice(self.plays))

    def test_player(self):
        print(colorama.Fore.WHITE + "{} moves:".format(len(self.history)))
        for text, value in self.history:
            guess = input("Next [r,g,b,y]: ")
            if guess != value:
                return False
        return True

    def clear(self):
        os.system('clear')
