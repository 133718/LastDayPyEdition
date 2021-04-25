from pygame import *


class SpriteSheet:
    def __init__(self, filename):
        self.sheet = image.load(filename).convert_alpha()
        self.idle = [(768, 0, 128, 128), (896, 0, 128, 128), (0, 128, 128, 128), (128, 128, 128, 128)]
        self.run = [(256, 128, 128, 128), (384, 128, 128, 128), (512, 128, 128, 128), (640, 128, 128, 128),
                    (768, 128, 128, 128), (896, 128, 128, 128), (0, 256, 128, 128), (128, 256, 128, 128)]
        self.attack = [(0, 0, 128, 128), (128, 0, 128, 128), (256, 0, 128, 128), (384, 0, 128, 128), (512, 0, 128, 128),
                       (640, 0, 128, 128)]
        self.jump_up = [(256, 256, 128, 128)]
        self.jump_down = [(384, 256, 128, 128), (512, 256, 128, 128), (640, 256, 128, 128)]
        self.frame = 0
        self.sub_frame = 0
        self.animation = None

    def Idle(self, flip):
        if self.animation == 'Idle':
            if self.sub_frame > 2:
                self.frame += 1
                self.sub_frame = 0
            else:
                self.sub_frame += 1
        else:
            self.frame = 0
            self.sub_frame = 0
        if self.frame > len(self.idle) - 1:
            self.frame = 0
        self.animation = 'Idle'
        return transform.flip(self.sheet.subsurface(self.idle[self.frame]), flip, False)

    def Run(self, flip):
        if self.animation == 'Run':
            if self.sub_frame > 1:
                self.frame += 1
                self.sub_frame = 0
            else:
                self.sub_frame += 1
        else:
            self.frame = 0
            self.sub_frame = 0
        if self.frame > len(self.run) - 1:
            self.frame = 0
        self.animation = 'Run'
        return transform.flip(self.sheet.subsurface(self.run[self.frame]), flip, False)

    def JumpUp(self, flip):
        self.animation = 'JumpUp'
        return transform.flip(self.sheet.subsurface(self.jump_up[0]), flip, False)

    def JumpDown(self, flip):
        if self.animation == 'JumpDown':
            if self.sub_frame > 1:
                self.frame += 1
                self.sub_frame = 0
            else:
                self.sub_frame += 1
        else:
            self.frame = 0
            self.sub_frame = 0
        if self.frame > len(self.jump_down) - 1:
            self.frame = 2
        self.animation = 'JumpDown'
        return transform.flip(self.sheet.subsurface(self.jump_down[self.frame]), flip, False)

    def Attack(self, flip):
        if self.animation == 'Attack':
            if self.sub_frame > 1:
                self.frame += 1
                self.sub_frame = 0
            else:
                self.sub_frame += 1
        else:
            self.frame = 0
            self.sub_frame = 0
        if self.frame > len(self.attack) - 1:
            self.frame = 5
        self.animation = 'Attack'
        return transform.flip(self.sheet.subsurface(self.attack[self.frame]), flip, False)


class Texture:
    def __init__(self, handle):
        self.img = None
        self.handle = handle
        self.sheet = SpriteSheet('img\ss.png')
        self.img = self.sheet.Idle(False)
        self.left = False
        self.attack = False
        self.cooldown = False
        self.timer = 0

    def update(self, player):
        # if left_button:
        #     if left_button and not self.cooldown:
        #         self.cooldown = True
        #         self.attack = True
        # else:
        #     self.cooldown = False

        # if self.attack:
        #     if self.sheet.animation == "Attack":
        #         self.timer += 1
        #     else:
        #         self.timer = 0
        #
        #     if self.timer >= len(self.sheet.attack):
        #         self.attack = False
        #         # player.state = 'Move'
        #     else:
        #         pass
        #         # player.state = 'Attack'
        #     if self.timer == 5:
        #         player.attack(self.left)
        #     self.img = self.sheet.Attack(self.left)

        if player.on_ground_trigger:
            if player.x_vector > 0:
                self.img = self.sheet.Run(False)
                self.left = False
            elif player.x_vector < 0:
                self.img = self.sheet.Run(True)
                self.left = True
            else:
                self.img = self.sheet.Idle(self.left)

        else:
            if player.x_vector > 0:
                self.left = False
            elif player.x_vector < 0:
                self.left = True
            if player.y_vector <= 1:
                self.img = self.sheet.JumpUp(self.left)
            elif player.y_vector > 1:
                self.img = self.sheet.JumpDown(self.left)
