import pygame as pg
import numpy as np
from tools import UObject
from spitesheets import LevelSpriteSheet
import time


class Camera(object):
    def __init__(self, player_rect):
        self.width = pg.display.Info().current_w
        self.height = pg.display.Info().current_h
        self.h_width = int(self.width / 2)
        self.h_height = int(self.height / 2)
        self.q_width = int(self.width / 4)
        self.q_height = int(self.height / 4)
        self.player_rect = player_rect
        self.x = -(self.player_rect.x - self.h_width + self.player_rect.width // 2)
        self.y = -(self.player_rect.y - self.h_height + self.player_rect.height // 2)

    def update(self):
        if self.width - self.x - self.player_rect.x + 64 < self.q_width:
            self.x = (self.h_width + self.q_width) - self.player_rect.x + 64

        if self.x + self.player_rect.x + 64 < self.q_width:
            self.x = self.q_width - self.player_rect.x - 64

        if self.height - self.y - self.player_rect.y - 64 < self.q_height:
            self.y = (self.h_height + self.q_height) - self.player_rect.y - 64

        if self.y + self.player_rect.y < self.q_height:
            self.y = self.q_height - self.player_rect.y

        if self.x <= -12288:
            self.x = -12288

        if self.y <= -8192:
            self.y = -8192

        if self.x >= 0:
            self.x = 0

        if self.y >= 0:
            self.y = 0


class SelectedBox(UObject):
    def __init__(self, player_rect, layers):
        self.player_rect = player_rect
        self.width = player_rect.width
        self.height = self.player_rect.height
        super().__init__((self.player_rect.x + self.width / 2) // self.width * self.width,
                         (self.player_rect.y + self.height / 2) // self.height * self.height,
                         self.width, self.height)

        self.layers = layers
        self.layers.GUI.add(self)
        self.image.fill(pg.Color(170, 170, 170))
        self.image.set_alpha(70)
        self.sprite = UObject(self.rect.x, self.rect.y, 64, 64)
        self.layers.GUI2.add(self.sprite)
        self.state = True

        self.keys = None
        self.toolbars = layers.sprite_sheet.toolbars
        self.toolbar = self.toolbars["block"]
        self.update_sprite(self.toolbar.get_item())

    def update(self, events, *args, **kwargs) -> None:
        self.update_img()
        self.keys = {"left_btn": False,
                     "right_btn": False,
                     "up": False,
                     "down": False,
                     "block": False,
                     "decoration": False,
                     "top": False,
                     "background": False
                     }
        self.update_keys(events)
        self.rect.x = (self.player_rect.x + self.width / 2) // self.width * self.width
        self.rect.y = (self.player_rect.y + self.height / 2) // self.height * self.height

        if self.keys["up"]:
            self.toolbar.previous()

        if self.keys["down"]:
            self.toolbar.next()

        if self.keys["block"]:
            self.toolbar = self.toolbars["block"]

        if self.keys["decoration"]:
            self.toolbar = self.toolbars["decoration"]

        if self.keys["top"]:
            self.toolbar = self.toolbars["top"]

        if self.keys["background"]:
            self.toolbar = self.toolbars["background"]

        if self.keys["left_btn"]:
            self.layers.update_tile(self.rect.x // 64, self.rect.y // 64,
                                    self.toolbar.layer_num, self.toolbar.get_item()[2])

        if self.keys["right_btn"]:
            pass

        self.update_sprite(self.toolbar.get_item())

    def update_keys(self, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.keys["left_btn"] = True
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                self.keys["right_btn"] = True
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 4:
                self.keys["up"] = True
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 5:
                self.keys["down"] = True
            if event.type == pg.KEYDOWN and event.key == pg.K_1:
                self.keys["block"] = True
            if event.type == pg.KEYDOWN and event.key == pg.K_2:
                self.keys["decoration"] = True
            if event.type == pg.KEYDOWN and event.key == pg.K_3:
                self.keys["top"] = True
            if event.type == pg.KEYDOWN and event.key == pg.K_4:
                self.keys["background"] = True

    def update_img(self):
        surface = pg.Surface((self.width, self.height))
        surface.fill(pg.Color(170, 170, 170))
        if self.state:
            surface.set_alpha(self.image.get_alpha() - 1)
            self.image = surface
            if self.image.get_alpha() <= 70:
                self.state = False
        else:
            surface.set_alpha(self.image.get_alpha() + 1)
            self.image = surface
            if self.image.get_alpha() >= 100:
                self.state = True

    def update_sprite(self, item):
        self.sprite.rect.x = self.rect.x
        self.sprite.rect.y = self.rect.y
        self.sprite.image = self.layers.sprite_sheet.get_sprite(item[2])


class Layers(object):
    def __init__(self, file="None"):
        self.width = pg.display.Info().current_w
        self.height = pg.display.Info().current_h
        self.sprite_sheet = LevelSpriteSheet()
        self.active_tile = []
        if file == "None":
            self.array = np.array(
                [[Tile(sprites=(0, 0, 0, 55)) for _ in range(128)] for _ in range(192)], dtype=object)
        else:
            self.array = self.array = self.open_level(file)

        self.GUI = pg.sprite.Group()
        self.entity = pg.sprite.Group()
        self.GUI2 = pg.sprite.Group()
        self.all_group = [self.entity, self.GUI2, self.GUI]

    def update_tile(self, x, y, num_layer, num):
        self.array[x, y].update_tile(num_layer, num, self.sprite_sheet)
        # pg.image.save(self.array[x, y].get_tile(self.sprite_sheet), 'tile.png')

    def get_tile(self, x, y):
        return self.array[x, y]

    def draw(self, screen, camera):
        # start_time = time.time()
        x = (-camera.x) // 64
        y = (-camera.y) // 64
        for row in range(int(self.width / 64) + 2):
            for collum in range((int(self.height / 64) + 2)):
                screen.blit(self.array[row + abs(x), collum + abs(y)].get_tile(self.sprite_sheet),
                            ((row * 64 - abs(camera.x) % 64), (collum * 64 - abs(camera.y) % 64)))
                self.array[row + x, collum + y].activate(self.active_tile)
        for group in self.all_group:
            for sprite in group:
                screen.blit(sprite.image, (sprite.rect.x + camera.x, sprite.rect.y + camera.y))
        self.update_array()
        # print("--- %s seconds ---" % (time.time() - start_time))

    def save_level(self):
        array = np.empty((192, 128, 4), int)
        x = 0
        y = 0
        for row in self.array:
            for tile in row:
                array[x, y, 0] = tile.top
                array[x, y, 1] = tile.decoration
                array[x, y, 2] = tile.block
                array[x, y, 3] = tile.background
                y += 1
            y = 0
            x += 1
            np.save('level', array)

    @staticmethod
    def open_level(name):
        start_time = time.time()
        level_array = np.load(name)
        array = np.array([[Tile(sprites=level_array[j, i]) for i in range(128)] for j in range(192)],
                         dtype=object)
        print("--- %s seconds ---" % (time.time() - start_time))
        return array

    def update_array(self):
        # start_time = time.time()
        for tile in self.active_tile:
            tile.update()
            if tile.active <= 0:
                tile.tile = None
                self.active_tile.remove(tile)
        # print("--- %s seconds ---" % (time.time() - start_time))


class Tile(object):
    def __init__(self, sprites=()):
        self.state = "Air"
        self.active = 0
        self.layers = [0, 0, 0, 0]
        if len(sprites) == 0:
            pass
        elif len(sprites) == 4:
            self.layers[3] = sprites[3]
            self.layers[2] = sprites[2]
            self.layers[1] = sprites[1]
            self.layers[0] = sprites[0]
        else:
            raise Exception("Incorrect num of sprites")
        self.block_chek()
        self.tile = None

    def update_tile(self, num_layer, num, sprite_sheet):
        self.layers[num_layer] = num
        self.block_chek()
        self.update_sprite(sprite_sheet)

    def get_tile(self, sprite_sheet):
        if self.tile is None:
            self.update_sprite(sprite_sheet)
        return self.tile

    def get_nums(self):
        return self.layers

    def block_chek(self):
        if self.layers[2] != 0:
            self.state = "block"
        else:
            self.state = "Air"

    def update_sprite(self, sprite_sheet):
        tile = pg.Surface((64, 64), pg.SRCALPHA)
        if self.layers[3] != 0:
            tile.blit(sprite_sheet.get_sprite(self.layers[3]), (0, 0))
        if self.layers[2] != 0:
            tile.blit(sprite_sheet.get_sprite(self.layers[2]), (0, 0))
        if self.layers[1] != 0:
            tile.blit(sprite_sheet.get_sprite(self.layers[1]), (0, 0))
        if self.layers[0] != 0:
            tile.blit(sprite_sheet.get_sprite(self.layers[0]), (0, 0))
        self.tile = tile

    def activate(self, array):
        if self.active == 0:
            self.active = 2
            array.append(self)
        else:
            self.active = 2

    def update(self):
        self.active -= 1
