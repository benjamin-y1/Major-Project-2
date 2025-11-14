import pygame

class Cell:
    def __init__(self, value, colour, x, y, number):
        self.value = value
        self.colour = colour
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.rect = ""
        self.num_clicks = 0
        self.number = number

        self.mousedown = False

    def draw(self, win, font, corner_font):
        border = pygame.Surface((52, 52))
        border.fill((0, 0, 0))

        surface = pygame.Surface((50, 50))
        surface.fill(self.colour)

        text_surface = font.render(self.value, False, (0, 0, 0))
        surface.blit(text_surface, (14, 27))

        if self.number:
            text_surface = corner_font.render(str(self.number), False, (0, 0, 0))
            surface.blit(text_surface, (0, 0))

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

        if rect.collidepoint(pygame.mouse.get_pos()) and self.num_clicks == 0:
            self.num_clicks = 1
            return 1

        elif rect.collidepoint(pygame.mouse.get_pos()) and self.num_clicks == 1:
            self.num_clicks = 2
            return 2

        elif rect.collidepoint(pygame.mouse.get_pos()) and self.num_clicks == 2:
            self.num_clicks = 1
            return 1

        return False

    def highlight(self, win, font, corner_font):
        yellow = (253, 217, 3)
        self.colour = yellow
        self.draw(win, font, corner_font)

    def highlight_line(self, win, font, corner_font):
        blue = (167, 216, 255)
        self.colour = blue
        self.draw(win, font, corner_font)

class Board:
    def __init__(self, height, width, start_x ,start_y, grid_access, grid_numbers):
        self.cells = [[] for i in range(height)]
        self.height = height
        self.width = width
        self.start_x = start_x
        self.start_y = start_y
        self.grid_access = grid_access
        self.grid_numbers = grid_numbers
        self.direction = "horizontal"

        for i in range(self.height):
            for j in range(self.width):
                if self.grid_access[i][j] == "-":
                    self.cells[i].append(Cell("", (255, 255, 255), self.start_x + j * 52, self.start_y + i * 52, grid_numbers[i][j]))
                else:
                    self.cells[i].append(Cell("", (0, 0, 0), self.start_x + j * 52, self.start_y + i * 52, grid_numbers[i][j]))

    def draw(self, win, font, corner_font):
        for lines in range(self.height):
            for cells in range(self.width):
                self.cells[lines][cells].draw(win, font, corner_font)

    def whiten(self, win, font, corner_font):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
               if self.grid_access[i][j] == "-":
                    self.cells[i][j].colour = (255, 255, 255)
                    self.cells[i][j].draw(win, font, corner_font)

    def change_click_value(self, x):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
               if self.grid_access[i][j] == "-":
                    self.cells[i][j].num_clicks = x

    def check_highlight(self, win, font, corner_font):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                if self.grid_access[i][j] == "-":

                    temp = self.cells[i][j].check_if_highlighted()
                    if temp:
                        print(temp)

                    if temp == 2:
                        if self.direction == "horizontal":
                            self.direction = "vertical"
                        else:
                            self.direction = "horizontal"

                    if temp:
                        if self.direction == "horizontal":
                            self.whiten(win, font, corner_font)

                            for k in range(j, len(self.cells[i])):
                               if self.grid_access[i][k] == "-":
                                   self.cells[i][k].highlight_line(win, font, corner_font)

                               elif self.grid_access[i][k] == ".":
                                   break

                            for k in range(0, j)[::-1]:
                               if self.grid_access[i][k] == "-":
                                   self.cells[i][k].highlight_line(win, font, corner_font)

                               elif self.grid_access[i][k] == ".":
                                   break

                            self.cells[i][j].highlight(win, font, corner_font)

                        elif self.direction == "vertical":
                            self.whiten(win, font, corner_font)

                            for l in range(i, len(self.cells)):
                                if self.grid_access[l][j] == "-":
                                    self.cells[l][j].highlight_line(win, font, corner_font)

                                elif self.grid_access[l][j] == ".":
                                    break

                            for l in range(0, i)[::-1]:
                                if self.grid_access[l][j] == "-":
                                    self.cells[l][j].highlight_line(win, font, corner_font)

                                elif self.grid_access[l][j] == ".":
                                    break

                            self.cells[i][j].highlight(win, font, corner_font)

        pygame.display.update()

    def move_to_the_next(self, collum, row, win, font, corner_font):
        self.cells[row][collum].highlight_line(win, font, corner_font)
        print(collum, row)

        if self.direction == "horizontal":
            if self.grid_access[row][collum + 1] == "-":
                self.cells[row][collum + 1].highlight(win, font, corner_font)
        else:
            if self.grid_access[row + 1][collum] == "-":
                self.cells[row + 1][collum].highlight(win, font, corner_font)

