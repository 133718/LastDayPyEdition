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

    def update_text(self, layer):
        self.text = "L:{0}".format(layer + 1)
        self.image = self.font.render(self.text, False, pg.Color(255, 255, 255))