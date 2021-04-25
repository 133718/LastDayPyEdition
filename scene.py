import json
import pygame as pg
from gui import Layers, Camera
from person import Player
from menu import *
from tools import _Object


class Scene(object):
    def __init__(self, file_path):
        self.layers = None
        self.player = None
        self.camera = None
        self.menu_object = None
        self.pause = False
        self.font = pg.font.Font('fonts/font.ttf', 36)
        self.FPS = 60
        self.screen = _Object(0, 0, pg.display.Info().current_w, pg.display.Info().current_h, color=(0, 0, 0))
        self.screen.image.set_alpha(0)
        self.load_scene(file_path)

    def load_scene(self, file_path):
        js = json.loads(open(file_path).read())
        self.layers = Layers(file=js["level"]["level_data"])
        if js["level"]["pause"] == 1:
            self.pause = True
        if js["level"]["player"] != "None":
            self.player = Player(js["level"]["player"]["startX"] * 64,
                                 js["level"]["player"]["startY"] * 64, 64, 64, self.layers.entity)
        if self.player is None:
            self.camera = Camera(pg.Rect(0, 0, 0, 0))
        else:
            self.camera = Camera(self.player.rect)
        for i in js["level"]["gui"]:
            if i["name"] == "Logo":
                menu = StartMenu(0, 0, pg.display.Info().current_w, pg.display.Info().current_h)
                self.layers.GUI.add(menu)
                self.menu_object = menu
        if self.menu_object is None:
            menu = Menu(0, 0, pg.display.Info().current_w, pg.display.Info().current_h)
            self.layers.GUI.add(menu)
            self.menu_object = menu
        self.layers.GUI.add(self.screen)

    def update(self, events, screen):
        if self.player is not None:
            self.player.update(events, self.layers.get_tiles(self.player.rect.center))
        self.camera.update()
        self.layers.GUI.update(events)
        self.layers.draw(screen, self.camera)
        if self.menu_object.state == "out":
            alpha = self.screen.image.get_alpha()
            self.screen.image = pg.Surface((pg.display.Info().current_w, pg.display.Info().current_h))
            self.screen.image.set_alpha(alpha + 5)
