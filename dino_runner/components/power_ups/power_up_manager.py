import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        contador = random.randint(0, 2)
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300) 
            if contador == 0:
                self.power_ups.append(Shield())
            elif contador == 1:
                self.power_ups.append(Hammer())
            else:
                self.power_ups.append(Heart())

    def update(self, score, game_speed, player):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                player.has_power_up = True       
                power_up.start_time = pygame.time.get_ticks()                                           
                if power_up.type == "heart": 
                    player.has_power_up_heart = True 
                else:         
                    player.type = power_up.type
                    if power_up.type == "hammer":
                        player.has_power_up_hammer = True          
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
