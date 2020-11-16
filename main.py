import pygame
from network import Network


class Game:
    def __init__(self, title, cell_no, cell_size):
        pygame.init()
        self.win = pygame.display.set_mode((cell_no*cell_size, cell_no*cell_size))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def draw(self):
        self.win.fill((255, 255, 255))
        pygame.draw.rect(self.win, (255, 0, 0), (food[0] * 20, food[1] * 20, 20, 20))
        for addr in players:
            players[addr].draw(self.win)
        pygame.display.update()


if __name__ == "__main__":
    game = Game("Snake", 25, 20)
    n = Network()
    player, addr = n.player
    run = True
    while run:
        players, food = n.send(player)
        player = players[addr]

        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        if player.bodies[0][0] < 1:
            y = player.bodies[0][1]
            player.bodies[0] = (25, y)
        elif player.bodies[0][0] > 24:
            y = player.bodies[0][1]
            player.bodies[0] = (0, y)
        elif player.bodies[0][1] < 1:
            x = player.bodies[0][0]
            player.bodies[0] = (x, 25)
        elif player.bodies[0][1] > 24:
            x = player.bodies[0][0]
            player.bodies[0] = (x, 0)

        player.move()
        game.draw()
        game.clock.tick(15)
