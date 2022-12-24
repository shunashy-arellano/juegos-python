import pygame
import sys
import random

#Constantes
ANCHO = 800
ALTO = 600
color_lila = (187, 143, 206)
color_negro =(0, 0, 0)
color_naranja = (245, 176, 65)

#Jugador
jugador_size = 50
jugador_posicion = [ANCHO / 2, ALTO - jugador_size * 2]

#Enemigos
enemigo_size = 50
enemigo_posicion = [random.randint(0, ANCHO - enemigo_size), 0]

#Crear ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))

game_over = False
clock = pygame.time.Clock()

#Funciones
def detectar_colision(jugador_posicion, enemigo_posicion):
    jx = jugador_posicion[0]
    jy = jugador_posicion[1]
    ex = enemigo_posicion[0]
    ey = enemigo_posicion[1]

    if (ex >= jx and ex < (jx + jugador_size)) or (jx >= ex and jx < (ex + enemigo_size)):
        if (ey >= jy and ey < (jy + jugador_size)) or (jy >= ey and jy < (ey + enemigo_size)):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = jugador_posicion[0]
            if event.key == pygame.K_LEFT:
                x -= jugador_size
            if event.key == pygame.K_RIGHT:
                x += jugador_size

            jugador_posicion[0] = x

    ventana.fill(color_negro)

    if enemigo_posicion[1] >= 0 and enemigo_posicion[1] < ALTO:
        enemigo_posicion[1] += 20
    else:
        enemigo_posicion[0] = random.randint(0, ANCHO - enemigo_size)
        enemigo_posicion[1] = 0

    #Colision
    if detectar_colision(jugador_posicion, enemigo_posicion):
        game_over = True

    #Dibujar enemigo
    pygame.draw.rect(ventana, color_naranja, 
                    (enemigo_posicion[0], enemigo_posicion[1], 
                    enemigo_size, enemigo_size))


    #Dibujar jugador (donde se muestra, color (RGB),  posicion en pantalla y tamaño del cuadrado)
    pygame.draw.rect(ventana, color_lila, 
                    (jugador_posicion[0], jugador_posicion[1], 
                    jugador_size, jugador_size))

    
    clock.tick(30)
    pygame.display.update()