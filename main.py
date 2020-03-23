from settings import Settings
import pygame as pg
from gun import Gun
import math as m
import os

# Pygame initialisation
pg.init()

# Set window position
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (100, 100)

# Create settings object
settings = Settings()

# Screen settings
screen = pg.display.set_mode(
    (settings.screen_size, settings.screen_size), flags=pg.DOUBLEBUF | pg.NOFRAME)

settings.screen = screen

settings.surf = pg.Surface(
    (settings.screen_size, settings.screen_size))

settings.surf.set_alpha(100)
clock = pg.time.Clock()

gun = Gun(settings)


# Main loop
while True:

    settings.surf.fill((15, 15, 15))
    clock.tick(settings.fps)

    # Text settings
    myfont = pg.font.SysFont('System', int(settings.text_size))

    text = myfont.render("Rate is {}".format(
        gun.fire_rate), True, (255, 255, 255))

    text_surf = pg.Surface(text.get_size(), pg.SRCALPHA)
    text_surf.fill((255, 255, 255, settings.text_alpha))

    for ball in settings.balls:
        ball.move()

        if ball.y < -50:
            settings.balls.pop(settings.balls.index(ball))
        ball.draw()

    gun.draw()

    if gun.go_fire:
        gun.fire_counter += 1
        if gun.fire_counter % gun.fire_rate == 0:
            gun.fire()
            gun.fire_counter = 0

    if settings.text_alpha >= 10:
        settings.text_alpha -= 10
    else:
        settings.text_alpha = 0

    if settings.text_size >= 61:
        settings.text_size -= 1

    # Screen bliting
    settings.screen.blit(settings.surf, (0, 0))
    text.blit(text_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

    text_rect = text.get_rect(center=(450, 450))
    settings.screen.blit(text, text_rect)

    # Events checking
    for i in pg.event.get():
        if i.type == pg.KEYUP:
            if i.key == 32:
                gun.go_fire = False
        elif i.type == pg.KEYDOWN:
            if i.key == 113:
                exit()
            elif i.key == 32:
                gun.go_fire = True
            else:
                print("KEY CODE IS", i.key)
        elif i.type == pg.MOUSEBUTTONUP:
            if i.button == 1:
                gun.go_fire = False

        elif i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                gun.go_fire = True

            if i.button == 4:
                gun.fire_rate -= 1
                settings.text_alpha = 155
                settings.text_size = 70

                if gun.fire_rate <= 0:
                    gun.fire_rate = 1

                print("FIRE RATE CHANGED TO", gun.fire_rate)

            elif i.button == 5:
                gun.fire_rate += 1
                settings.text_alpha = 155
                settings.text_size = 70

                print("FIRE RATE CHANGED TO", gun.fire_rate)

        elif i.type == pg.MOUSEMOTION:
            settings.mouse_pos = pg.mouse.get_pos()

            if settings.mouse_pos[0] > 10 and (settings.screen_size - settings.mouse_pos[1] - settings.gun_y_pos) != 0:
                settings.mouse_agnle = m.degrees(
                    m.atan((settings.mouse_pos[0]) / (settings.screen_size - settings.mouse_pos[1] - settings.gun_y_pos)))

                if settings.mouse_agnle <= 0:
                    settings.mouse_agnle *= -1
                else:
                    settings.mouse_agnle = 180 - settings.mouse_agnle

            if settings.mouse_agnle <= 20:
                settings.mouse_agnle = 20
            elif settings.mouse_agnle >= 160:
                settings.mouse_agnle = 160

    pg.display.update()
