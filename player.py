import pygame

class Cell:
    def __init__(self, value, colour, x, y):
        self.value = value
        self.colour = colour
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.rect = ""

        self.mousedown = False

    def draw(self, win, font):
        border = pygame.Surface((52, 52))
        border.fill((0, 0, 0))

        surface = pygame.Surface((50, 50))
        surface.fill(self.colour)

        text_surface = font.render(self.value, False, (0, 0, 0))
        surface.blit(text_surface, (14, 27))

        border.blit(surface, (1, 1))

        win.blit(border, self.pos)

    def check_if_highlighted(self):
        rect = pygame.Rect(self.pos[0], self.pos[1], 50, 50)

        if pygame.mouse.get_pressed()[0]:
            if self.mousedown:
                return False

            self.mousedown = True

        else:
            self.mousedown = False
            return False

        if rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def highlight(self, win, font):
        yellow = (253, 217, 3)
        self.colour = yellow
        self.draw(win, font)

    def highlight_line(self, win, font):
        blue = (167, 216, 255)
        self.colour = blue
        self.draw(win, font)

class Board:
    def __init__(self, height, width, start_x ,start_y, grid_access):
        self.cells = [[] for i in range(height)]
        self.height = height
        self.width = width
        self.start_x = start_x
        self.start_y = start_y
        self.grid_access = grid_access

        for i in range(self.height):
            for j in range(self.width):
                if self.grid_access[i][j] == "-":
                    self.cells[i].append(Cell("", (255, 255, 255), self.start_x + j * 52, self.start_y + i * 52))
                else:
                    self.cells[i].append(Cell("", (0, 0, 0), self.start_x + j * 52, self.start_y + i * 52))

    def draw(self, win, font):
        for lines in range(self.height):
            for cells in range(self.width):
                self.cells[lines][cells].draw(win, font)

    def whiten(self, win, font):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
               if self.grid_access[i][j] == "-":
                    print(self.grid_access)
                    self.cells[i][j].colour = (255, 255, 255)
                    self.cells[i][j].draw(win, font)

    def check_highlight(self, win, font):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.grid_access[i][j] == "-":
                    if self.cells[i][j].check_if_highlighted():
                        self.whiten(win, font)
                        for k in range(len(self.cells[i])):
                           if self.grid_access[i][k] == "-":
                               print(self.grid_access)
                               self.cells[i][k].highlight_line(win, font)
                           elif self.grid_access[i][k] == ".":
                               break
                        self.cells[i][j].highlight(win, font)

        pygame.display.update()

