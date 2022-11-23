import pygame

import random ##import

from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS ##import
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus import Large_Cactus ##import


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        contador = 0
        contador = random.randint(1, 2)
        if len(self.obstacles) == 0:
            if contador == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))   
            else:
                self.obstacles.append(Large_Cactus(LARGE_CACTUS))
        ##print(contador)
                         
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
