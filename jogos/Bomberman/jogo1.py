import pygame
from pygame.locals import *
from sys import exit
import os
import random
from random import randint

#começo

pygame.init()

largura = 640
altura = 480
x = largura/2  - 20/2
y = altura/2 - 20/2

fonte = pygame.font.SysFont('arial', '40', True, True)
pontos = 0

x_azul = randint(40, 600)
y_azul = randint(50, 430)
clock = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("BomberMan, by Caio")

while True:
    clock.tick(60)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    text_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if y >= altura:
        y = -1
    if x >= largura:
        x = -1
    '''            
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 10
            if event.key == K_d:
                x += 10
            if event.key == K_s:
                y += 10
            if event.key == K_w:
                y -= 10
'''
    if pygame.key.get_pressed()[K_a]:
        x -= 10
    if pygame.key.get_pressed()[K_d]:
        x += 10
    if pygame.key.get_pressed()[K_w]:
        y -= 10
    if pygame.key.get_pressed()[K_s]:
        y += 10
    retângulo_vermelho = pygame.draw.rect(tela, (255,0,0), (x, y,20,20))
    retângulo_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul, 20, 20))

    if retângulo_vermelho.colliderect(retângulo_azul):
        x_azul = randint(40,600)
        y_azul = randint(50, 430)
        pontos += 1
    tela.blit(text_formatado, (450, 400))
    pygame.display.update()