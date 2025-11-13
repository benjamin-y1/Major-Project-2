import pygame
from player import Cell, Board, check_highlight
from network import Network

pygame.font.init()
font = pygame.font.SysFont('Ariel', 35)

width = 1500
height = 700
win = pygame.display.set_mode((width, height))
win.fill((255, 255, 255))

def update(my_board, op_board):
    check_highlight(my_board, win, font)
    my_board.draw(win, font)
    op_board.draw(win, font)
    pygame.display.update()

def main():
    global my_board, op_board
    run = True
    clock = pygame.time.Clock()
    n = Network()
    try:
        my_board = n.connect()
        my_board.initiate(win, font)
    except:
        print("bad, don't work because of this thing")

    while run:
        clock.tick(60)

        try:
            op_board = n.receive_board()
        except:
            print("okay, like stop")

        try:
            n.send_board(my_board)
        except:
            print("lol, bad, like actually bad")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        try:
            update(my_board, op_board)
        except:
            print("this is whats not working")

main()