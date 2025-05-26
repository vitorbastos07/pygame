import pygame
import os
from config import *
from pygame import mixer

def assets():
    assets = {}
    
    carro_verm = pygame.image.load('../assets/images/carro_verm.png').convert_alpha()
    carro_verd = pygame.image.load('../assets/images/carro_verd.png').convert_alpha()
    carro_azul = pygame.image.load('../assets/images/carro_azul.png').convert_alpha()
    batmovel = pygame.image.load('../assets/images/batmovel.png').convert_alpha()
    barco = pygame.image.load('../assets/images/barquinho.png').convert_alpha()
    sapo_img = pygame.image.load('../assets/images/galinha.png').convert_alpha()
    sapo_img_small = pygame.transform.scale(sapo_img, (sapo_width, sapo_height))
    
    #png pequena
    carro_verm_small = pygame.transform.scale(carro_verm, (carro_width, carro_height))   
    carro_verd_small = pygame.transform.scale(carro_verd, (carro_width, carro_height))
    carro_azul_small = pygame.transform.scale(carro_azul, (carro_width, carro_height))
    batmovel_small = pygame.transform.scale(batmovel, (carro_width, carro_height))
    barco_small = pygame.transform.scale(barco, (barco_width, barco_height))
    
    assets['Carros'] = [
    carro_verm_small,
    carro_verd_small,
    carro_azul_small,
    batmovel_small
    ]

    assets['Barco'] = [
    barco_small   
    ]

    botao_img = pygame.image.load('../assets/images/tela_de_inicio.png').convert()
    background1 = pygame.image.load('../assets/images/background_nivel1.png').convert()
    background2 = pygame.image.load('../assets/images/background_nivel2.png').convert()
    background3 = pygame.image.load('../assets/images/background_nivel3.png').convert()
    background4 = pygame.image.load('../assets/images/background_nivel4.png').convert()
    background5 = pygame.image.load('../assets/images/background_nivel5.png').convert()
    backgroundfinal = pygame.image.load('../assets/images/backf1.png').convert()
    
    assets['Galinha'] = [ 
    sapo_img_small
    ]

    assets['Background'] = [
    botao_img,
    background1,
    background2,
    background3,
    background4,
    background5,
    backgroundfinal    
    ]

    assets['Spawnybarc'] = [
    750,
    450,
    300    
    ]

    assets['Spawny'] = [
    300,
    160,
    15,
    600,
    750,
    450
    ]

    assets['Spawnx'] = [
    -50,
    800    
    ]
    return assets

