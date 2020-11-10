import pygame
import os
import sys
import random

GAME_FOLDER = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(1, GAME_FOLDER)
import ENV_Variables as env


class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((env.SIDE, env.SIDE))
        self.image.fill(env.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(2*env.SIDE, env.WIDTH - 2*env.SIDE)
        self.rect.y = random.randint(2*env.SIDE, env.HEIGHT - 2*env.SIDE)

    def update(self):
        pass
