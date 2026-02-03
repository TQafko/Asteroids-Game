import pygame
import random
from asteroid import Asteroid
from constants import *


class GameStats(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.playerscore = 0
        self.playerlife = PLAYER_LIFE
        self.time = 0

    def draw(self, screen):
        pygame.font.init()
        font = pygame.font.Font(None, 50)
        score_text = font.render(f"Score: {self.playerscore}", True, (255, 255, 255)) # White color
        life_text = font.render(f"Life: {self.playerlife}", True, (255, 255, 255)) # White color
        screen.blit(score_text, (10, 10)) # Top-left corner
        screen.blit(life_text, (SCREEN_WIDTH-(SCREEN_WIDTH/12), 10)) # Top-left corner

    def update(self, score, life, dt):
        self.playerscore = score
        self.playerlife = life
        self.time += dt
