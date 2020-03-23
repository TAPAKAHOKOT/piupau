import pygame as pg
import math as m
from ball import Ball


class Gun:
    def __init__(self, settings):
        self.settings = settings

        self.x = -10
        self.y = self.settings.gun_y_pos

        self.go_fire = False
        self.fire_rate = 3
        self.fire_counter = 0

        self.lenght = 50
        self.height = 14

    def draw(self):
        rect = (self.x, self.settings.screen_size -
                self.y, self.lenght, self.height)

        angle = m.radians(self.settings.mouse_agnle - 90)

        # Creating tilted rect
        self.rect = pg.draw.polygon(self.settings.surf, (150, 100, 0),
                                    [
            [self.x + self.height // 2 * m.cos(m.radians(self.settings.mouse_agnle)),
             self.settings.screen_size - self.y - self.height // 2 * m.sin(m.radians(self.settings.mouse_agnle))],

            [self.x - self.height // 2 * m.cos(m.radians(self.settings.mouse_agnle)),
             self.settings.screen_size - self.y + self.height // 2 * m.sin(m.radians(self.settings.mouse_agnle))],

            [self.x + self.lenght * m.cos(angle) - self.height // 2 * m.cos(m.radians(self.settings.mouse_agnle)),
             self.settings.screen_size - self.lenght * m.sin(angle) - self.y + self.height // 2 * m.sin(m.radians(self.settings.mouse_agnle))],

            [self.x + self.lenght * m.cos(angle) + self.height // 2 * m.cos(m.radians(self.settings.mouse_agnle)),
             self.settings.screen_size - self.lenght * m.sin(angle) - self.y - self.height // 2 * m.sin(m.radians(self.settings.mouse_agnle))]

        ])

    def fire(self):

        # Creating new balls
        angle = m.radians(self.settings.mouse_agnle - 90)
        self.settings.balls.append(
            Ball(self.settings, self.x + self.lenght * m.cos(angle),
                 self.settings.screen_size - self.lenght * m.sin(angle) - self.y))
