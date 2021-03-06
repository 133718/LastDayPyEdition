import pygame as pg
import json


class LevelSpriteSheet(object):
    def __init__(self):
        self.sprite_sheet = pg.image.load("img/level_sprite_sheet.png").convert_alpha()
        self.js = json.loads(open("tiles.json").read())
        self.tiles = self.js["tiles"]
        self.objects = self.js["objects"]
        self.index = self.js["index"]
        self.states = {
            "0": (False, False),
            "1": (True, False),
            "2": (False, True),
            "3": (True, True)
        }

        self.block = [
            self.tiles[40],
            self.tiles[41],
            self.tiles[42],
            self.tiles[43],
            self.tiles[46],
            self.tiles[49],
            self.tiles[52],
            self.tiles[53],
            self.tiles[54],
            self.tiles[55],
            self.tiles[11],
            self.tiles[33],
            self.tiles[34],
            self.tiles[35],
            self.tiles[21],
            self.tiles[22],
            self.tiles[23],
            self.tiles[32],
            self.tiles[20],
        ]
        self.background = [
            self.tiles[47],
            self.tiles[48],
            self.tiles[2],
            self.tiles[3],
            self.tiles[13],
            self.tiles[14],
            self.tiles[1],
            self.tiles[12]
        ]
        self.decoration = [
            self.tiles[4],
            self.tiles[5],
            self.tiles[6],
            self.tiles[7],
            self.tiles[15],
            self.tiles[16],
            self.tiles[9],
            self.tiles[18],
            self.tiles[24],
            self.tiles[25],
            self.tiles[26],
            self.tiles[27],
            self.tiles[28],
            self.tiles[29],
            self.tiles[30],
            self.tiles[38],
            self.tiles[31],
            self.tiles[39],
            self.tiles[44],
            self.tiles[45],
            self.tiles[36],
            self.tiles[37]
        ]

        self.top = [
            self.tiles[8],
            self.tiles[17],
            self.tiles[10],
            self.tiles[19],
        ]

        self.toolbars = {
            "top": Toolbar(self.top, 0),
            "decoration": Toolbar(self.decoration, 1),
            "block": Toolbar(self.block, 2),
            "background": Toolbar(self.background, 3),
            "select": Select([self.tiles[0]], 0)
        }

    def get_tile(self, num):
        img = self.sprite_sheet.subsurface((self.tiles[num]["cords"][0], self.tiles[num]["cords"][1],
                                            self.tiles[num]["size"][0] * 64, self.tiles[num]["size"][1] * 64))
        return img

    def get_object(self, num):
        img = self.sprite_sheet.subsurface((self.objects[num][0], self.objects[num][1], 64, 64))
        return img

    def to_tile(self, num):
        array = []
        for i in num:
            array.append(self.tiles[self.index[i]])
        return array


class Toolbar(object):
    def __init__(self, toolbar_array, layer_num):
        self.toolbar = toolbar_array
        self.item = 0
        self.layer_num = layer_num

    def get_item(self):
        return self.toolbar[self.item]

    def next(self):
        self.item += 1
        if self.item > len(self.toolbar) - 1:
            self.item = 0

    def previous(self):
        self.item -= 1
        if self.item < 0:
            self.item = len(self.toolbar) - 1


class Select(Toolbar):
    def __init__(self, toolbar_array, layer_num):
        super().__init__(toolbar_array, layer_num)
        self.layer_num = self.item

    def set_item(self, items, layer):
        self.toolbar = items
        self.layer_num = layer

    def next(self):
        self.item += 1
        if self.item > len(self.toolbar) - 1:
            self.item = 0
        self.layer_num = self.item

    def previous(self):
        self.item -= 1
        if self.item < 0:
            self.item = len(self.toolbar) - 1
        self.layer_num = self.item
