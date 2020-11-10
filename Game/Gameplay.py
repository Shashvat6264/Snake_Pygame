import pygame
import os
import sys
import random

GAME_FOLDER = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(1, GAME_FOLDER)
import ENV_Variables as env
import Sprites as sp


class Gameplay:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((env.WIDTH, env.HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.background = pygame.Surface((env.WIDTH, env.HEIGHT))
        self.background.fill(env.BLUE)
        self.background_rect = self.background.get_rect()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.foods = pygame.sprite.Group()
        self.score = 0

    def update(self, snake):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        if snake.bitten():
            self.running = False

        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(snake, self.foods, True)
        for hit in hits:
            self.score += 1
            snake.increaselength()
            if self.score % 5 == 0:
                snake.linearspeed += 1
            f = sp.Food()
            self.all_sprites.add(f)
            self.foods.add(f)

    def draw(self, snake):
        self.screen.fill(env.BLUE)
        self.screen.blit(self.background, self.background_rect)
        self.all_sprites.draw(self.screen)
        for i in snake.snakebits:
            pygame.draw.rect(self.screen, env.WHITE, (i[0], i[1], env.SIDE, env.SIDE))
        pygame.display.flip()

    def run(self):
        s = sp.Snake(env.INITLENGTH)
        self.all_sprites.add(s)
        f = sp.Food()
        self.foods.add(f)
        self.all_sprites.add(f)
        while self.running:
            self.clock.tick(env.FPS)
            self.update(s)
            self.draw(s)
        pygame.quit()
