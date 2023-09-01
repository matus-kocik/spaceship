import pygame
import sys
from settings import Settings
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.player = Player(self)
        pygame.display.set_caption("Spaceship")
        self.clock = pygame.time.Clock()

    def run(self):
        
     
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            self.player.blit_me()
            pygame.display.flip()
            self.clock.tick(60)
            
            
            
if __name__ == "__main__":
    game = Game()
    game.run()


