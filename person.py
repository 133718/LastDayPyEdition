from tools import _Object
import pygame as pg


class Creator(_Object):
    def __init__(self, x, y, width, height, player_layer, state='Move'):
        super().__init__(x, y, width, height)
        player_layer.add(_Object(x, y, width, height, alpha=150))
        player_layer.add(self)
        self.image.fill(pg.Color(230, 180, 10))

        self.start_x = x
        self.start_y = y
        self.x_vector = 0
        self.y_vector = 0
        self.max_move_speed = 10
        self.move_speed = 5

        self.state = state
        self.keys = {"left": False,
                     "right": False,
                     "up": False,
                     "down": False,
                     "space": False,
                     "left_btn": False,
                     "right_btn": False,
                     "shift": False}

    def update(self, events, *args, **kwargs):
        self.update_keys(events)
        if self.state == 'Fly':
            if self.keys["shift"]:
                if self.keys["up"]:
                    self.y_vector = -16
                if self.keys["down"]:
                    self.y_vector = 16
                if not (self.keys["up"] or self.keys["down"]):
                    self.y_vector = 0

                if self.keys["left"]:
                    self.x_vector = -16
                if self.keys["right"]:
                    self.x_vector = 16
                if not (self.keys["left"] or self.keys["right"]):
                    self.x_vector = 0
            else:
                if self.keys["up"]:
                    self.y_vector = -4
                if self.keys["down"]:
                    self.y_vector = 4
                if not (self.keys["up"] or self.keys["down"]):
                    self.y_vector = 0

                if self.keys["left"]:
                    self.x_vector = -4
                if self.keys["right"]:
                    self.x_vector = 4
                if not (self.keys["left"] or self.keys["right"]):
                    self.x_vector = 0

            self.rect.x += self.x_vector
            self.rect.y += self.y_vector

            # if self.rect.x > 14144:
            #     self.rect.x = 14144
            # if self.rect.x < 0:
            #     self.rect.x = 0
            # if self.rect.y > 9152:
            #     self.rect.y = 9152
            # if self.rect.y < 0:
            #     self.rect.y = 0

    def update_keys(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_a:
                self.keys["left"] = True
            if event.type == pg.KEYDOWN and event.key == pg.K_d:
                self.keys["right"] = True
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.keys["space"] = True
            if event.type == pg.KEYDOWN and event.key == pg.K_w:
                self.keys["up"] = True
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                self.keys["down"] = True
            if event.type == pg.KEYDOWN and event.key == pg.K_LSHIFT:
                self.keys["shift"] = True

            if event.type == pg.KEYUP and event.key == pg.K_d:
                self.keys["right"] = False
            if event.type == pg.KEYUP and event.key == pg.K_a:
                self.keys["left"] = False
            if event.type == pg.KEYUP and event.key == pg.K_SPACE:
                self.keys["space"] = False
            if event.type == pg.KEYUP and event.key == pg.K_w:
                self.keys["up"] = False
            if event.type == pg.KEYUP and event.key == pg.K_s:
                self.keys["down"] = False
            if event.type == pg.KEYUP and event.key == pg.K_LSHIFT:
                self.keys["shift"] = False

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.keys["left_btn"] = True
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                self.keys["right_btn"] = True

            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                self.keys["left_btn"] = False
            if event.type == pg.MOUSEBUTTONUP and event.button == 3:
                self.keys["right_btn"] = False
