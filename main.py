import pygame, sys
from machine import *
from render import *

interp = Interpreter()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                interp.step()
            elif event.key == pygame.K_r:
                interp.load_file()
                interp.reset_registros()

    screen.fill(WHITE)
    render_registros(interp)
    render_instruccion(interp)
    render_consola(interp)
    render_botones()
    pygame.display.flip()

pygame.quit()
sys.exit()
