import pygame as pg
from scene import Scene
from menu import PauseMenu
pg.init()
WIDTH = pg.display.Info().current_w
HEIGHT = pg.display.Info().current_h
FPS = 60
screen = pg.display.set_mode((WIDTH, HEIGHT))
scene = Scene("levels/level2/level.json")
clock = pg.time.Clock()
running = True

while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                if scene.pause:
                    PauseMenu(screen).run()
    screen.fill((0, 0, 0))
    scene.update(events, screen)
    pg.display.update()
    clock.tick(FPS)

pg.quit()
