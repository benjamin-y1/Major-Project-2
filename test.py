import pygame
from player import Cell, Board

pygame.font.init()
font = pygame.font.SysFont('Ariel', 35)

width = 700
height = 700
win = pygame.display.set_mode((width, height))

board = Board(5)

def main():
    run = True
    clock = pygame.time.Clock()
    board.initiate(win, font)
    win.fill((255,255,255))

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            board.draw(win, font)

            pygame.display.update()

main()