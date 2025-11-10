from player import Board
import pygame

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 50)

width = 500
height = 500
win = pygame.display.set_mode((width, height))

b = Board(0, 0)

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    pygame.display.update()

    win.fill((255, 255, 255))
    b.drawBoard(win)