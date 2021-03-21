import pygame
import person
import gui
from gui import Camera
import time


def draw_fps():
    image = font.render(str(player.rect.x) + " " + str(camera.x), False, (255, 255, 255))
    screen.blit(image, (0, 0))


pygame.init()
WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h
FPS = 60
font = pygame.font.Font('fonts/font.ttf', 36)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
layers = gui.Layers()
player = person.Creator(0, 0, 64, 64, layers.entity, state="Fly")
camera = Camera(player.rect)
selected_box = gui.SelectedBox(player.rect, layers)
clock = pygame.time.Clock()
running = True

while running:
    start_time = time.time()
    events = pygame.event.get()
    player.update(events)
    selected_box.update(events)
    camera.update()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    layers.draw(screen, camera)
    draw_fps()
    pygame.display.update()
    # print("--- %s seconds ---" % (time.time() - start_time))
    clock.tick(FPS)

pygame.quit()
