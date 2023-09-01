import pygame

class Player:
    def __init__(self, game):
        self.screen = game.screen
        
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load("images/spaceship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        
    def blit_me(self):
        self.screen.blit(self.image, self.rect)
