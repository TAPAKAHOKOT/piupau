from random import randint as rnd
import math as m
import pygame as pg


class Ball:
    def __init__(self, settings, x, y):
        self.settings = settings

        self.angle = self.settings.mouse_agnle

        self.go_forward = True
        self.go_down = True

        self.x = x
        self.y = y

        self.y_grav = 0.13

        self.color = (rnd(0, 255), rnd(0, 255), rnd(0, 255))

        self.start_v = rnd(50, 180) / 20
        self.size_growth = rnd(10, 50) / 100

        self.x_v = self.start_v * m.cos(m.radians(90 - self.angle))
        self.y_v = self.start_v * m.sin(m.radians(90 - self.angle))

        self.start_size = 1
        self.actual_size = rnd(5, 30)

        self.size = self.start_size

    def draw(self):
        self.rect = pg.draw.circle(self.settings.surf, self.color,
                                   (int(self.x), int(self.y)), int(self.size))

    def move(self):
        # Balls growthing up
        if self.size < self.actual_size:
            self.size += self.size_growth
        elif self.size > self.actual_size:
            self.size = self.actual_size

        self.x += self.x_v
        self.y += self.y_v

        self.y_v += self.y_grav

        # Gravitation lol
        self.x_v *= 0.9999
        self.y_v *= 0.9999

        if self.y >= self.settings.screen_size - self.size and self.go_down:
            self.y_v *= -1

            # Friction fore
            self.y_v *= 0.95
            self.x_v *= 0.96

            # Anctibag system
            self.go_down = False

        if rnd(0, 300) == 3:
            self.y_grav *= -1

        if self.y < self.settings.screen_size - self.size and not self.go_down:
            # Anctibag system
            self.go_down = True

        if self.x >= self.settings.screen_size - self.size and self.go_forward:
            self.x_v *= -1

            # Friction fore
            self.x_v *= 0.95

            # Anctibag system
            self.go_forward = False

        if not self.go_forward and self.x <= self.size:
            self.x_v *= -1

            # Friction fore
            self.x_v *= 0.95

            # Anctibag system
            self.go_forward = True
