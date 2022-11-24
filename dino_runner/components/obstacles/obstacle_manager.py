import pygame

import random ##import

from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS ##import
from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus import Large_Cactus ##import
from dino_runner.components.obstacles.bird import bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        contador = random.randint(0, 2)
        if len(self.obstacles) == 0:
            if contador == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))  
            elif contador == 1:
                self.obstacles.append(Large_Cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(bird(BIRD))
                            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
