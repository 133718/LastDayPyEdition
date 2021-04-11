import json
import pygame as pg
from gui import Layers, Camera
from person import Player


class Scene(object):
    def __init__(self, file_path, surface):
        self.js = json.loads(open(file_path).read())
        self.layers = Layers(file=self.js["level"]["level_data"])
        self.player = Player(self.js["level"]["startX"] * 64, self.js["level"]["startY"] * 64, 64, 64, self.layers.entity)
        self.camera = Camera(self.player.rect)
        self.clock = pg.time.Clock()
        self.screen = surface
        self.running = True
        self.FPS = 60

    def run(self):
        while self.running:
            events = pg.event.get()
            self.player.update(events, self.layers.get_tiles(self.player.rect.center))
            self.camera.update()
            for event in events:
                if event.type == pg.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            self.layers.draw(self.screen, self.camera)
            pg.display.update()
            self.clock.tick(self.FPS)
