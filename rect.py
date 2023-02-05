import pygame

import constants


# прямоугольник, который будет двигаться по окружности
class Rect(object):

    color = constants.WHITE     #цвет
    screen = None               #экран, на который выводится прямоугольник

    # координаты центра окружности относительно окна pygam
    center_x = None
    center_y = None

    height = None               #высота прямоугольника
    width = None                #ширина прямоугольника
    pygame_rect = None          #прямоугольник


    def __init__(self, screen: pygame.Surface, center_x, center_y):
        self.screen = screen
        self.center_x = center_x
        self.center_y = center_y
        self.height = 30
        self.width = 30
        self.create_pygame_rect()


    def draw(self):
        pygame.draw.rect(self.screen, constants.RED, self.pygame_rect)

    # создает квадрат
    def create_pygame_rect(self):
        left = self.center_x - self.width/2
        top = self.center_y - self.height/2
        self.pygame_rect = pygame.Rect(left, top, self.width, self.height)


    # меняет координаты центра квадрата и рисует его
    def change_center_and_draw(self, point):
        self.center_x = point[0]
        self.center_y = point[1]
        self.draw()

    # меняет координаты центра квадрата
    def change_center(self, point):
        self.center_x = point[0]
        self.center_y = point[1]


    # двигает прямоугольник вправво
    def move_right(self):
        self.center_x += 3

    def move_and_draw(self):
        self.move_right()
        self.create_pygame_rect()
        self.draw()