import pygame as pg
import numpy as np
from cellgrid import Grid as g

screen_size = (800, 800)  # Size of the screen in pixels.
grid_size = (100, 100)  # Size of the grid of cells. Should be a divisor of screen_size.
num = 20  # Number of cells to randomly activate.
clr = (255, 255, 255)  # Color of active cells.
delay = 0  # Add milliseconds of delay if the simulation runs too fast.

pg.init()
pixel_size = (np.floor(screen_size[0] / grid_size[0]), np.floor(screen_size[1] / grid_size[1]))
screen = pg.display.set_mode(screen_size)
grid = g(grid_size[0], grid_size[1], 2)

# Add your rules here!!!
cells = []
for x in range(grid_size[0]):
    for y in range(grid_size[1]):
        if (x + y) % 2 == 0:
            cells.append((x, y))
grid.add_rule([3], [2, 3], cells)

cells = []
for x in range(grid_size[0]):
    for y in range(grid_size[1]):
        if (x + y) % 2 == 1:
            cells.append((x, y))
grid.add_rule([3, 4], [2, 3, 4], cells)


if num < (grid_size[0] * grid_size[1]):
    grid.randomize(num)


def check():
    clicked = False
    while not clicked:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    clicked = True
        mouse = pg.mouse.get_pressed()
        if mouse[0] or mouse[2]:
            x, y = pg.mouse.get_pos()
            u = int(np.floor(x / pixel_size[0]))
            v = int(np.floor(y / pixel_size[1]))
            if mouse[0]:
                grid.set_state(u, v, 1)
            elif mouse[2]:
                grid.set_state(u, v, 0)
            state = grid.get_state(u, v)
            a = 255 * state
            clr = (a, a, a)
            pg.draw.rect(screen, clr, (u * pixel_size[0], v * pixel_size[1], pixel_size[0], pixel_size[1]))
            pg.display.flip()


def run():
    running = True
    while running:
        screen.fill((0, 0, 0))
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    running = False
                elif event.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()

        for x in range(grid_size[0]):
            for y in range(grid_size[1]):
                state = grid.get_state(x, y)
                a = 255 * state
                clr = (a, a, a)
                pg.draw.rect(screen, clr, (x * pixel_size[0], y * pixel_size[1], pixel_size[0], pixel_size[1]))
        pg.display.flip()
        grid.evolve()
        if delay > 0:
            pg.time.delay(delay)

while 1:
    run()
    check()
