import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Spaceship")
        self.clock = pygame.time.Clock()

    def run(self):
        
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(60)
            
            
            
if __name__ == "__main__":
    game = Game()
    game.run()


