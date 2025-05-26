from typing import get_origin
import pygame
from random import randint
from assets import *
from config import *
from player import *

pygame.init()
pygame.mixer.init()








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


font = pygame.font.SysFont(None, 48)
keys_down = {}
pla = ''
with open('../data/leaderboard.txt', 'rt') as placar:
    pla = placar.readline()
tempo_vivo = 0
tempo_em_s = 0
dificuldade = 1
mort = 151

pit = '../assets/sounds/mus.mp3'
mixer.music.load(pit)
mixer.music.set_volume(0.3)
mixer.music.play(-1)





while game:
    tempo_v = font.render('{0}s'.format(tempo_em_s), True, (255, 255, 0))
    nivel = font.render('Fase {0}'.format(nivel1), True, (0,0,255))
    tem_m = font.render('Espere: {0}s'.format(round(mort/30),2), True, (255,0,0))
    if len(pla) > 0:
        melhor_temp = font.render('Melhor tempo: {0}s'.format(pla), True, (255,0,0))
    fim = font.render('Você levou {0} segundos!'.format(tempo_em_s), True, (255,0,0))
    if tempo_vivo == FPS and nivel1 != 0:
        tempo_em_s += 1
        tempo_vivo = 0
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_RETURN:
                nivel1 = 1
                tempo_vivo = 0
                tempo_em_s = 0
            if event.key == pygame.K_LEFT and nivel1 > 0:
                player.vx -= sapo_width/2
            if event.key == pygame.K_RIGHT and nivel1 > 0:
                player.vx += sapo_width/2
            if event.key == pygame.K_UP and nivel1 > 0:
                player.vy -= sapo_height/2
            if event.key == pygame.K_DOWN and nivel1 > 0:
                player.vy += sapo_height/2
            if event.key == pygame.K_r and nivel1 > 0:
                tempo_vivo = 0
                tempo_em_s = 0
                nivel1 = 1
                dificuldade = 1
                mort = 151
                player.rect.centerx = WIDTH / 2
                player.rect.bottom = HEIGHT - 10
                pla = ''
                with open('../data/leaderboard.txt', 'rt') as placar:
                    pla = placar.readline()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and nivel1 > 0:
                player.vx = 0
            if event.key == pygame.K_RIGHT and nivel1 > 0:
                player.vx = 0
            if event.key == pygame.K_UP and nivel1 > 0:
                player.vy = 0
            if event.key == pygame.K_DOWN and nivel1 > 0:
                player.vy = 0
    if dificuldade == 1:
        difc = 5
    else:
        difc = 5 + dificuldade * 5
    if difc > 25:
        difc = 25
    if nivel1 != 6 and nivel1 != 0:
        while len(all_carros) < difc:
            carrinho = Carros(assets,nivel1)
            all_carros.add(carrinho)
            all_sprites.add(carrinho)
        if nivel1 > 1:
            while len(all_barcos) < 2 * dificuldade:
                barcin = Barcos(assets,nivel1)
                all_barcos.add(barcin)
                all_sprites.add(barcin)
    if player.rect.top <= 0:
        dificuldade += 1
        nivel1 += 1
        player.rect.centerx = WIDTH / 2
        player.rect.bottom = HEIGHT - 10
        for carro in all_carros.sprites():
            carro.kill()
        if len(all_barcos) > 1:
            for barco in all_barcos.sprites():
                barco.kill()

    window.fill((0, 0, 0))  
    if nivel1 == 0:
        window.blit(assets['Background'][0], (0, 0))
    else:
        window.blit(assets['Background'][nivel1], (0, 0))
    all_sprites.update()
    hit = pygame.sprite.spritecollide(player, all_carros, True)
    if len(hit) > 0:
        mort = 150
        player.matar()
        ms = pygame.mixer.Sound('../assets/sounds/mf.mp3')
        ms.set_volume(0.3)
        ms.play()
    hit = pygame.sprite.spritecollide(player, all_barcos, True)
    if len(hit) > 0:
        mort = 150
        player.matar()
        ms = pygame.mixer.Sound('../assets/sounds/mf.mp3')
        ms.set_volume(0.3)
        ms.play() 

    if nivel1 == 5 and player.rect.top <= 0:
        with open('../data/leaderboard.txt', 'wt') as placar:
            if len(pla) > 0:
                if tempo_em_s < int(pla):  
                    pla = str(tempo_em_s)
            else:
                pla = str(tempo_em_s)
            placar.write(pla)

        if len(pla) > 0:
            melhor_temp = font.render('Melhor tempo: {0}s'.format(pla), True, (255,0,0))

        window.blit(assets['Background'][5], (0, 0))
        window.blit(fim,(0,HEIGHT/2))
    all_sprites.draw(window)
    window.blit(tempo_v, (0,0))
    if nivel1 != 6:
        window.blit(nivel, (0,30))
    else:
        window.blit(fim,(50,HEIGHT/2))
    if len(pla) > 0:
        window.blit(melhor_temp, (0,60))
    if mort <= 150 and mort != 0:
        window.blit(tem_m, (10,HEIGHT/2))
        mort -= 1
    pygame.display.update()
    tempo_vivo += 1
    if nivel1 == 6:
        tempo_vivo -= 1
    if sapo_y == 0:
        sapo_y = sapo_y_initial
pygame.quit()