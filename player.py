import pygame

class Cell:
    def __init__(self, value, colour, x, y, surface, border):
        self.value = value
        self.colour = colour
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.rect = (self.x, self.y, 50, 50)
        self.surface = surface
        self.border = border

    def draw(self, win, font):
        self.border = pygame.Surface((52, 52))
        self.border.fill((0, 0, 0))

        self.surface = pygame.Surface((50, 50))
        self.surface.fill(self.colour)

        text_surface = font.render(self.value, False, (0, 0, 0))
        self.surface.blit(text_surface, (14, 27))

        self.border.blit(self.surface, (1, 1))

        win.blit(self.border, self.pos)

class Board:
    def __init__(self, dimension):
        self.cells = [[] for i in range(dimension)]
        self.dimension = dimension

    def initiate(self, win, font):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.cells[i].append(Cell("A", (255, 255, 255), j * 52, i * 52, win, win))
                self.cells[i][j].draw(win, font)

    def draw(self, win, font):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.cells[i][j].draw(win, font)



