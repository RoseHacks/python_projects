import pygame as pg
import random

# Dice animation with a random number between 1 & 6 being landed on.

pg.init()
#Running = True
#screen = pg.display.set_mode(1280, 720)
#clock = pg.time.Clock()

class Game():

    def roll_die(self):
        return random.randint(1, 6)


g = Game()

i = g.roll_die()
print("You random number is: ", i)

