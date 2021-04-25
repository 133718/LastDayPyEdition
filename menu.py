from tools import *
import pygame as pg


class StartMenu(UObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pg.Surface((width, height), pg.SRCALPHA)
        self.state = "logo"
        self.logo = Text(150, 0, 0, "")
        self.press = Text(36, 0, 0, "Press any button")
        self.image.blit(self.logo.image, (0, 0))
        self.timer = 0

    def update(self, events, *args, **kwargs) -> None:
        if self.state == "logo":
            self.timer += 1
            self.logo.update_text("LustPy"[0: self.timer // 10])
            self.image = pg.Surface((self.rect.width, self.rect.height), pg.SRCALPHA)
            self.image.blit(self.logo.image, (self.rect.width // 2 - self.logo.image.get_width() // 2, 370))
            if self.timer > len("LustPy") * 10:
                self.state = "press"
                self.timer = 0
        elif self.state == "press":
            self.timer += 5
            self.image = pg.Surface((self.rect.width, self.rect.height), pg.SRCALPHA)
            self.image.blit(self.logo.image, (self.rect.width // 2 - self.logo.image.get_width() // 2, 370))
            self.press.update_text("Press any button")
            self.press.image.set_alpha(self.timer)
            self.image.blit(self.press.image, (self.rect.width // 2 - self.press.image.get_width() // 2, 500))
            if self.timer > 255:
                self.state = "idle"

        if self.state == "press" or self.state == "idle":
            for event in events:
                if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
                    self.state = "out"
                    self.timer = 255
        if self.state == "out":
            self.timer -= 4
            self.image = pg.Surface((self.rect.width, self.rect.height), pg.SRCALPHA)
            self.image.blit(self.logo.image, (self.rect.width // 2 - self.logo.image.get_width() // 2, 370))
            self.image.blit(self.press.image, (self.rect.width // 2 - self.press.image.get_width() // 2, 500))
            self.image.set_alpha(self.timer)
            if self.timer <= 0:
                self.state = "exit"


class Menu(UObject):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pg.Surface((width, height), pg.SRCALPHA)
        self.state = "idle"


class PauseMenu(object):
    def __init__(self, screen):
        self.screen = screen
        self.img = self.screen.copy()
        self.running = True
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.state = "in"
        self.alpha = 0

    def run(self):
        while self.running:
            events = pg.event.get()

            for event in events:
                if event.type == pg.QUIT:
                    self.running = False
                    exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                        return
            self.screen.fill((0, 0, 0))
            if self.state == "in":
                self.alpha += 10
                if self.alpha >= 200:
                    self.state = "middle"
                self.screen.blit(self.img, (0, 0))
                surf = pg.Surface(self.screen.get_size())
                surf.set_alpha(self.alpha)
                self.screen.blit(surf, (0, 0))
            elif self.state == "middle":
                self.screen.blit(self.img, (0, 0))
                surf = pg.Surface(self.screen.get_size())
                surf.set_alpha(self.alpha)
                self.screen.blit(surf, (0, 0))
            pg.display.update()
            self.clock.tick(self.FPS)
