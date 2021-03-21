import pygame as pg


# [("ground", (256, 128, 128, 128))]
class LevelSpriteSheet(object):
    def __init__(self):
        self.sprite_sheet = pg.image.load("img/level_sprite_sheet.png").convert_alpha()
        self.states = {
            "0": (False, False),
            "1": (True, False),
            "2": (False, True),
            "3": (True, True)
        }

        self.objects = [
            ("Air", (0, 0, 64, 64), 0, ""),
            ("Ground left up corner", (640, 320, 64, 64), 1, "block"),
            ("Ground up 1", (64, 0, 64, 64), 2, "block"),
            ("Ground up 2", (128, 0, 64, 64), 3, "block"),
            ("Ground right up corner", (192, 0, 64, 64), 4, "block"),
            ("Ground left ", (0, 64, 64, 64), 5, "block"),
            ("Ground ", (64, 64, 64, 64), 6, "background"),
            ("Background", (128, 64, 64, 64), 7, "background"),
            ("Ground right", (192, 64, 64, 64), 8, "block"),
            ("Ground left down corner", (0, 128, 64, 64), 9, "block"),
            ("Ground down 1", (64, 128, 64, 64), 10, "block"),
            ("Ground down 2", (128, 128, 64, 64), 11, "block"),
            ("Ground right down corner", (192, 128, 64, 64), 12, "block"),
            ("Ground inside corner", (256, 0, 64, 64), 13, ""),
            ("Ladder", (256, 64, 64, 64), 14, "block"),
            ("Ice block", (256, 128, 64, 64), 15, "block"),
            ("Left stone edge", (0, 192, 64, 64), 16, "background"),
            ("Right stone edge", (0, 256, 64, 64), 17, "background"),
            ("Stone 1", (128, 192, 64, 64), 18, "background"),
            ("Stone 2", (64, 192, 64, 64), 19, "background"),
            ("Stone 3", (64, 256, 64, 64), 20, "background"),
            ("Stone 4", (128, 256, 64, 64), 21, "background"),
            ("Ice platform 1 left", (0, 320, 64, 64), 22, "block"),
            ("Ice platform 1 middle", (64, 320, 64, 64), 23, "block"),
            ("Ice platform 1 right", (128, 320, 64, 64), 24, "block"),
            ("Ice platform 2 left", (0, 384, 64, 64), 25, "block"),
            ("Ice platform 2 middle", (64, 384, 64, 64), 26, "block"),
            ("Ice platform 2 right", (128, 384, 64, 64), 27, "block"),
            ("Stone 1", (320, 0, 64, 64), 28, "decoration"),
            ("Stone 2", (320, 64, 64, 64), 29, "decoration"),
            ("Stone 3", (448, 0, 128, 64), 30, "decoration"),
            ("Stone 4", (448, 64, 128, 64), 31, "decoration"),
            ("Stalactite 1", (384, 0, 64, 128), 32, "decoration"),
            ("Stalactite 2", (576, 0, 64, 128), 33, "decoration"),
            ("Tree 1", (192, 192, 192, 256), 34, "decoration"),
            ("Tree 2", (384, 192, 192, 256), 35, "decoration"),
            ("Grass 1", (320, 128, 64, 64), 36, "decoration"),
            ("Grass 2", (384, 128, 64, 64), 37, "decoration"),
            ("Grass 3", (448, 128, 64, 64), 38, "decoration"),
            ("Grass 4", (512, 128, 64, 64), 39, "decoration"),
            ("Grass 5", (576, 128, 64, 64), 40, "decoration"),
            ("Grass 6", (640, 128, 64, 64), 41, "decoration"),
            ("Grass 7", (640, 64, 64, 64), 42, "decoration"),
            ("Grass 8", (640, 0, 64, 64), 43, "decoration"),
            ("Grass 9", (576, 320, 64, 64), 44, "decoration"),
            ("Grass 10", (576, 384, 64, 64), 45, "decoration"),
            ("Grass 11", (640, 384, 64, 64), 46, "decoration"),
            ("Liana 1", (576, 192, 64, 64), 47, "top"),
            ("Liana 2", (576, 256, 64, 64), 48, "top"),
            ("Liana 3", (704, 0, 64, 64), 49, "top"),
            ("Liana 4", (704, 64, 64, 64), 50, "top"),
            ("Liana 5", (640, 192, 64, 64), 51, "top"),
            ("Liana 6", (640, 256, 64, 64), 52, "top"),
            ("Flower 1", (704, 128, 64, 64), 53, "decoration"),
            ("Flower 2", (704, 192, 64, 64), 54, "decoration"),
            ("Flower 3", (704, 256, 64, 64), 55, "decoration"),
            ("Flower 4", (704, 320, 64, 64), 56, "decoration")
        ]
        self.block = [
            self.objects[1],
            self.objects[2],
            self.objects[3],
            self.objects[4],
            self.objects[5],
            self.objects[8],
            self.objects[9],
            self.objects[10],
            self.objects[11],
            self.objects[12],
            self.objects[14],
            self.objects[15],
            self.objects[22],
            self.objects[23],
            self.objects[24],
            self.objects[25],
            self.objects[26],
            self.objects[27],
        ]
        self.background = [
            self.objects[6],
            self.objects[7],
            self.objects[16],
            self.objects[17],
            self.objects[18],
            self.objects[19],
            self.objects[20],
            self.objects[21]
        ]
        self.decoration = [
            self.objects[28],
            self.objects[29],
            self.objects[30],
            self.objects[31],
            self.objects[32],
            self.objects[33],
            self.objects[34],
            self.objects[35],
            self.objects[36],
            self.objects[37],
            self.objects[38],
            self.objects[39],
            self.objects[40],
            self.objects[41],
            self.objects[42],
            self.objects[43],
            self.objects[44],
            self.objects[45],
            self.objects[46],
            self.objects[53],
            self.objects[54],
            self.objects[55],
            self.objects[56]
        ]

        self.top = [
            self.objects[47],
            self.objects[48],
            self.objects[49],
            self.objects[50],
            self.objects[51],
            self.objects[52]
        ]

        self.toolbars = {
            "top": Toolbar(self.top, 0),
            "decoration": Toolbar(self.decoration, 1),
            "block": Toolbar(self.block, 2),
            "background": Toolbar(self.background, 3)
        }

    def get_sprite(self, num):
        img = self.sprite_sheet.subsurface(self.objects[num][1])
        return img


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
