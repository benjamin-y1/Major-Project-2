import pygame
from player import Cell, Board
from network import Network

pygame.font.init()
cell_font = pygame.font.SysFont('Ariel', 35)
cell_corner_font = pygame.font.SysFont("Ariel", 20)

width = 2000
height = 900
win = pygame.display.set_mode((width, height))
win.fill((255, 255, 255))

def update(my_board, op_board):
    my_board.check_highlight(win, cell_font, cell_corner_font)
    my_board.draw(win, cell_font, cell_corner_font)
    op_board.draw(win, cell_font, cell_corner_font)
    pygame.display.update()

#my_board = Board(10, 10, 10)

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    my_board = n.connect()
    if isinstance(my_board, Board):
        print("Connected")
    my_board.draw(win, cell_font, cell_corner_font)

    while run:
        clock.tick(60)

        n.send_board(my_board)
        op_board = n.receive_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                letter = pygame.key.name(event.key).upper()

                for i in range(len(my_board.cells)):
                    for j in range(len(my_board.cells[i])):
                        if my_board.cells[i][j].colour == (253, 217, 3):
                            my_board.cells[i][j].value = letter
                            my_board.draw(win, cell_font, cell_corner_font)
                            my_board.move_to_the_next(j, i, win, cell_font, cell_corner_font)
                            break
                    else:
                        continue
                    break

        #check_highlight(my_board, win, font)
        #my_board.draw(win, font)
        #pygame.display.update()

        update(my_board, op_board)


main()