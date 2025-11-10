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

class Board:
    def __init__(self, x, y):
        self.x = x
        self. y = y
        self.values = [[0, 0], [0, 0]]

    def drawBoard(self, win, font):
        for i in range(2):
            for j in range(2):
                if j == i:
                    colour = (255, 0, 0)
                else:
                    colour = (0, 255, 0)

                n = pygame.draw.rect(win, colour, (self.x + j * 50, self.y + i * 50, 50, 50))

                self.drawValues(win, n, font, self.values[j][i])

    def drawValues(self, win, rect, font, value):
        text_surface = font.render(value, False, (0, 0, 0))
        rect.blit(text_surface, (0, 0))

    def change(self, x, y):
        self.values[x][y] += 1