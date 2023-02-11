

# Pygame шаблон - скелет для нового проекта Pygame
import pygame

import constants
from rect import Rect

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


rect = Rect(screen, 500, 500)


# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(constants.FPS)

    #заливаем экран черным цветом
    screen.fill(constants.BLACK)

    # двигаем прямоугольник и рисуем его
    rect.move_and_draw()


    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()


pygame.quit()