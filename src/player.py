#Classes
from typing import get_origin
import pygame
from random import randint
from pygame import mixer
from config import *



class Carros(pygame.sprite.Sprite):
    def __init__(self, assets, nivel1):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        assets['Spawny'] = [
        300,
        160,
        15,
        600,
        750,
        450
        ]
        self.image = assets['Carros'] [randint(0,len(assets['Carros'])-1)]
        self.id = randint(1,100000)
        self.rect = self.image.get_rect()
        if nivel1 == 2:
            assets['Spawny'] = [
            160,
            15,
            600,
            ]
        elif nivel1 == 3:
            assets['Spawny'] = [
            600,
            450,
            300,
            15
            ]
        elif nivel1 == 4:
            assets['Spawny'] = [
            750,
            600,
            300,
            15
            ]
        elif nivel1 ==5:
            assets["Spawny"] = [ 
            600,
            160
            ]
        self.rect.x = assets['Spawnx'] [randint(0,len(assets["Spawnx"])-1)]
        self.rect.y = assets['Spawny'] [randint(0,len(assets["Spawny"])-1)]
        if self.rect.y == 750 or self.rect.y == 300 or self.rect.y == 160:
            self.speedx = randint(3, nivel1+10)
        else:
            self.speedx = randint(-10,-3)
            self.image = pygame.transform.flip(self.image, True, False)
        self.speedy = 0
    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH + 80:
            self.kill()