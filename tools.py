import pygame as pg


class _Object(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(255, 255, 255), alpha=255):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.image.fill(pg.Color(color))
        self.rect = pg.Rect(x, y, width, height)
        self.image.set_alpha(alpha)


class UObject(_Object):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def update(self, events, *args, **kwargs) -> None:
        pass


class Text(UObject):
    def __init__(self, size, x, y, text=""):
        self.text = text
        self.font = pg.font.Font("fonts/font.ttf", size)
        self.image = self.font.render(self.text, False, pg.Color(255, 255, 255))
        super().__init__(x, y, self.image.get_width(), self.image.get_height())
        self.image = self.font.render(self.text, False, pg.Color(255, 255, 255))

    def update_text(self, text):
        self.text = text
        self.image = self.font.render(self.text, False, pg.Color(255, 255, 255))


class Toolbar(object):
    def __init__(self, toolbar_array, layer_num):
        self.toolbar = toolbar_array
        self.item = 0
        self.layer_num = layer_num
        self.rotate = 0

    def get_item(self):
        return self.toolbar[self.item]

    def next(self):
        self.rotate = 0
        self.item += 1
        if self.item > len(self.toolbar) - 1:
            self.item = 0

    def previous(self):
        self.rotate = 0
        self.item -= 1
        if self.item < 0:
            self.item = len(self.toolbar) - 1

    def r_left(self):
        self.rotate -= 1
        if self.rotate < 0:
            self.rotate = len(self.get_item()["object"]) - 1

    def r_right(self):
        self.rotate += 1
        if self.rotate > len(self.get_item()["object"]) - 1:
            self.rotate = 0


class Select(Toolbar):
    def __init__(self, toolbar_array, layer_num):
        super().__init__(toolbar_array, layer_num)
        self.layer_num = self.item

    def set_item(self, items, layer):
        self.toolbar = items
        self.layer_num = layer

    def next(self):
        self.rotate = 0
        self.item += 1
        if self.item > len(self.toolbar) - 1:
            self.item = 0
        self.layer_num = self.item

    def previous(self):
        self.rotate = 0
        self.item -= 1
        if self.item < 0:
            self.item = len(self.toolbar) - 1
        self.layer_num = self.item


class Keys(object):
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.jump = False

    def update(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_a:
                self.left = True
            if event.type == pg.KEYDOWN and event.key == pg.K_d:
                self.right = True
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                self.jump = True
            if event.type == pg.KEYDOWN and event.key == pg.K_w:
                self.up = True
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                self.down = True

            if event.type == pg.KEYUP and event.key == pg.K_d:
                self.right = False
            if event.type == pg.KEYUP and event.key == pg.K_a:
                self.left = False
            if event.type == pg.KEYUP and event.key == pg.K_SPACE:
                self.jump = False
            if event.type == pg.KEYUP and event.key == pg.K_w:
                self.up = False
            if event.type == pg.KEYUP and event.key == pg.K_s:
                self.down = False


class Trigger(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.image.fill(pg.Color(0, 255, 255))
        self.image.set_alpha(127)
        self.rect = pg.Rect(x, y, width, height)
        self.collide = False

    def update(self, x, y, tiles):
        rects = []
        self.collide = False
        for collum in range(3):
            for row in range(3):
                x = (self.rect.centerx // 64 + (row - 1)) * 64
                y = (self.rect.centery // 64 + (collum - 1)) * 64
                rects.append(pg.Rect(x, y, 64, 64))

        self.rect.x = x
        self.rect.y = y
        if self.rect.x % 64 > 0:
            if rects[7].colliderect(self.rect) and tiles[1, 2].state == "block" or rects[8].colliderect(
                    self.rect) and tiles[2, 2].state == "block":
                self.rect.bottom = rects[7].top
                self.collide = False
        if self.rect.x % 64 < 0:
            if rects[7].colliderect(self.rect) and tiles[1, 2].state == "block" or rects[6].colliderect(
                    self.rect) and tiles[0, 2].state == "block":
                self.rect.bottom = rects[7].top
                self.collide = False
        else:
            if rects[7].colliderect(self.rect) and tiles[1, 2].state == "block":
                self.rect.bottom = rects[7].top
                self.collide = False
