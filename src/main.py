from typing import get_origin
import pygame
from random import randint
from assets import *
from config import *
from player import *

pygame.init()
pygame.mixer.init()




#Classes



font = pygame.font.SysFont(None, 48)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('JumpRoad')

nivel1 = 0
assets = assets()

player = Galinha(assets['Galinha'][0],nivel1,assets)
clock = pygame.time.Clock()
FPS = 30
all_sprites = pygame.sprite.Group()
all_carros = pygame.sprite.Group()
all_barcos = pygame.sprite.Group()
all_players = pygame.sprite.Group()
all_moedas = pygame.sprite.Group()
all_sprites.add(player)
groups = {}
groups['all_sprites'] = all_sprites
groups['all_carros'] = all_carros
groups['all_barcos'] = all_barcos
groups['all_players'] = all_players
groups['all_moedas'] = all_moedas
game = True


