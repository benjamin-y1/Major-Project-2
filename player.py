import pygame

class Player:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect( win, self.colour,self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

class Cell:
    def __init__(self, value, colour, x, y, surface):
        self.value = value
        self.colour = colour
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.rect = (self.x, self.y, 50, 50)
        self.surface = surface

    def draw(self, win):
        self.surface = pygame.Surface((50, 50))
        self.surface.fill(self.colour)
        win.blit(self.surface, self.pos)

    def update_text(self, font):
        text_surface = font.render(self.value, False, (0, 0, 0))
        self.surface.blit(text_surface, (0, 0))

class Board:
    def __init__(self, dimension):
        self.cells = [[] for i in range(dimension)]
        self.dimension = dimension

    def initiate(self, win):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.cells[i].append(Cell("", (255, 255, 255), 0 + j * 50, 0 + i * 50, win))
                self.cells[i][j].draw(win)

    def draw(self, font):
        for i in range(self.dimension):
            for j in range(self.dimension):
                self.cells[i][j].update_text(font)



