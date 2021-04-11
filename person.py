from tools import UObject, Keys, _Object
import pygame as pg


class Creator(UObject):
    def __init__(self, x, y, width, height, player_layer, state='Move'):
        super().__init__(x, y, width, height)
        # player_layer.add(_Object(x, y, width, height, alpha=150))
        player_layer.add(self)
        self.image.fill(pg.Color(230, 180, 10))
        self.x_vector = 0
        self.y_vector = 0

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

            if self.rect.x > 12224:
                self.rect.x = 12224
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.y > 8128:
                self.rect.y = 8128
            if self.rect.y < 0:
                self.rect.y = 0

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


# TODO Сделать класс игрока
class Player(_Object):
    def __init__(self, x, y, width, height, layer):
        super().__init__(x, y, width, height)
        layer.add(self)
        self.image.fill(pg.Color(230, 180, 10))
        self.startX = x
        self.startY = y
        self.keys = Keys()

        self.x_vector = 0
        self.y_vector = 0
        self.move_speed = 8
        self.boost = 2
        self.gravity = 0.7
        self.jump_boost = 20
        self.state = "Move"
        self.on_ground = False
        self.speed_protect = 1
        self.max_move_speed = 8

    def update(self, events, tiles, *args, **kwargs) -> None:
        self.keys.update(events)
        if self.state == "Move":
            if self.keys.jump and self.on_ground:
                self.y_vector = -self.jump_boost

            if self.keys.left:
                self.x_vector -= self.move_speed

            if self.keys.right:
                self.x_vector += self.move_speed

            if not self.on_ground:
                self.y_vector += self.gravity

            if not (self.keys.left or self.keys.right):
                if self.x_vector > 0:
                    self.x_vector -= self.move_speed
                elif self.x_vector < 0:
                    self.x_vector += self.move_speed

            if self.speed_protect == 1:
                if self.x_vector > self.max_move_speed:
                    self.x_vector = self.max_move_speed
                elif self.x_vector < -self.max_move_speed:
                    self.x_vector = -self.max_move_speed

            self.on_ground = False
            self.rect.y += self.y_vector
            self.collide(0, self.y_vector, tiles)

            self.rect.x += self.x_vector
            self.collide(self.x_vector, 0, tiles)

    def collide(self, x_vector, y_vector, tiles):
        rects = []
        for collum in range(3):
            for row in range(3):
                x = (self.rect.centerx // 64 + (row - 1)) * 64
                y = (self.rect.centery // 64 + (collum - 1)) * 64
                rects.append(pg.Rect(x, y, 64, 64))

        if x_vector > 0:
            if self.rect.y % 64 < 0:
                if rects[5].colliderect(self.rect) and tiles[2, 1].state == "block" or rects[8].colliderect(
                        self.rect) and tiles[2, 2].state == "block":
                    self.rect.right = rects[5].left
                    self.x_vector = 0
            if self.rect.y % 64 > 0:
                if rects[5].colliderect(self.rect) and tiles[2, 1].state == "block" or rects[2].colliderect(
                        self.rect) and tiles[2, 0].state == "block":
                    self.rect.right = rects[5].left
                    self.x_vector = 0
            else:
                if rects[5].colliderect(self.rect) and tiles[2, 1].state == "block":
                    self.rect.right = rects[5].left
                    self.x_vector = 0

        if x_vector < 0:
            if self.rect.y % 64 < 0:
                if rects[3].colliderect(self.rect) and tiles[0, 1].state == "block" or rects[6].colliderect(
                        self.rect) and tiles[0, 2].state == "block":
                    self.rect.left = rects[3].right
                    self.x_vector = 0
            if self.rect.y % 64 > 0:
                if rects[3].colliderect(self.rect) and tiles[0, 1].state == "block" or rects[0].colliderect(
                        self.rect) and tiles[0, 0].state == "block":
                    self.rect.left = rects[3].right
                    self.x_vector = 0
            else:
                if rects[3].colliderect(self.rect) and tiles[0, 1].state == "block":
                    self.rect.left = rects[3].right
                    self.x_vector = 0

        if y_vector > 0:
            if self.rect.x % 64 > 0:
                if rects[7].colliderect(self.rect) and tiles[1, 2].state == "block" or rects[8].colliderect(
                        self.rect) and tiles[2, 2].state == "block":
                    self.rect.bottom = rects[7].top
                    self.on_ground = True
                    self.y_vector = 0
            if self.rect.x % 64 < 0:
                if rects[7].colliderect(self.rect) and tiles[1, 2].state == "block" or rects[6].colliderect(
                        self.rect) and tiles[0, 2].state == "block":
                    self.rect.bottom = rects[7].top
                    self.on_ground = True
                    self.y_vector = 0
            else:
                if rects[7].colliderect(self.rect) and tiles[1, 2].state == "block":
                    self.rect.bottom = rects[7].top
                    self.on_ground = True
                    self.y_vector = 0

        if y_vector < 0:
            if self.rect.x % 64 > 0:
                if rects[1].colliderect(self.rect) and tiles[1, 0].state == "block" or rects[2].colliderect(
                        self.rect) and tiles[2, 0].state == "block":
                    self.rect.top = rects[1].bottom
                    self.y_vector = 0
            if self.rect.x % 64 < 0:
                if rects[1].colliderect(self.rect) and tiles[1, 0].state == "block" or rects[0].colliderect(
                        self.rect) and tiles[0, 0].state == "block":
                    self.rect.top = rects[1].bottom
                    self.y_vector = 0
            else:
                if rects[7].colliderect(self.rect) and tiles[1, 0].state == "block":
                    self.rect.top = rects[1].bottom
                    self.y_vector = 0

