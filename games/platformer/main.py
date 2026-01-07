import pygame as pg
import sys

# Initializing pygame
pg.init()

class Game():

    def __init__(self):
        # Defining our window resolution - A surface we can draw onto.
        self.screen = pg.display.set_mode((1280, 720))
        # Force the game to run at 60 FPS. Our clock object. In a game, each frame is an interation in a loop
        self.clock = pg.time.Clock()
        # A pissed off hacker in black hoodie
        # Takes place in cyberpunk world. Fighting blue team.
        self.game_name = pg.display.set_caption("Attack of The Hacker")   
        # image load function to put an image on the screen. Use PNG because it's lostless
        self.img = pg.image.load('data/images/clouds/cloud_1.png')


    def run(self):
        while True:
            # Despite math, top left is 0, 0 for non-gpu-based rendering techniques
            self.screen.blit(self.img, (100, 200))
            # In SDL, you have full control over the input handling
            # Polling for events with pg.event.get() 
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # pygame exit
                    sys.exit() # graceful system exit

            # Update the display
            pg.display.update()
            self.clock.tick(60)

game = Game()

game.run()





