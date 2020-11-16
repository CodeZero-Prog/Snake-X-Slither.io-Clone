import pygame


class Snake:
    def __init__(self, x_index, y_index, cell_size, color):
        self.x_index = x_index
        self.y_index = y_index
        self.color = color
        self.cell_size = cell_size
        self.bodies = [(x_index, y_index), (x_index-1, y_index), (x_index-2, y_index)]
        self.direction = (1, 0)

    def draw(self, win):
        for body in self.bodies:
            pygame.draw.rect(win, self.color, (body[0]*self.cell_size, body[1]*self.cell_size, self.cell_size, self.cell_size))

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.direction[1] != 1:
            self.direction = (0, -1)
        elif key[pygame.K_DOWN] and self.direction[1] != -1:
            self.direction = (0, 1)
        elif key[pygame.K_RIGHT] and self.direction[0] != -1:
            self.direction = (1, 0)
        elif key[pygame.K_LEFT] and self.direction[0] != 1:
            self.direction = (-1, 0)
        copy = self.bodies[:-1]
        copy.insert(0, (copy[0][0] + self.direction[0], copy[0][1] + self.direction[1]))
        self.bodies = copy

    def eat(self):
        previous_body = self.bodies[-1]
        self.bodies.append((previous_body[0] - (1 * self.direction[0]), previous_body[1] - (1 * self.direction[1])))
        return True
