import pygame as pg
from scene import Scene
pg.init()
WIDTH = pg.display.Info().current_w
HEIGHT = pg.display.Info().current_h
screen = pg.display.set_mode((WIDTH, HEIGHT))
level = Scene("levels/level1/level.json", screen)
level.run()
pg.quit()
