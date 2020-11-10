import pygame
import os
import sys

GAME_FOLDER = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(1, GAME_FOLDER)
import ENV_Variables as env


class Snake(pygame.sprite.Sprite):
    def __init__(self, n):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((env.SIDE, env.SIDE))
        self.image.fill(env.WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = env.WIDTH / 2
        self.rect.centery = env.HEIGHT / 2
        self.linearspeed = 3
        self.speedx = 3
        self.speedy = 0
        self.snakebits = []
        self.snakebits.append([self.rect.centerx, self.rect.centery])
        for i in range(0, n - 1):
            self.snakebits.append([self.snakebits[i][0] - env.SIDE, self.snakebits[i][1]])
        self.length = n

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        for i in range(self.length - 1, 0, -1):
            self.snakebits[i][0] = self.snakebits[i - 1][0]
            self.snakebits[i][1] = self.snakebits[i - 1][1]
        self.snakebits[0] = [self.rect.x, self.rect.y]
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_DOWN]:
            self.speedy = self.linearspeed
            self.speedx = 0
        if keystate[pygame.K_UP]:
            self.speedy = -1*self.linearspeed
            self.speedx = 0
        if keystate[pygame.K_LEFT]:
            self.speedx = -1*self.linearspeed
            self.speedy = 0
        if keystate[pygame.K_RIGHT]:
            self.speedx = self.linearspeed
            self.speedy = 0
        if self.rect.x > env.WIDTH:
            self.rect.x = 0
        if self.rect.x < -50:
            self.rect.x = env.WIDTH
        if self.rect.y > env.HEIGHT:
            self.rect.y = 0
        if self.rect.y < -50:
            self.rect.y = env.HEIGHT

    def increaselength(self):
        self.snakebits.append([self.snakebits[-1][0], self.snakebits[-1][0]])
        self.length += 1

    def bitten(self):
        if self.snakebits[0] in self.snakebits[1:]:
            return True
        else:
            return False
