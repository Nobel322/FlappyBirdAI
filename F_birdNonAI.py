import pygame
import sys

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,900))
    screen.blit(floor_surface,(floor_x_pos + 576,900))

pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

#Game variables
gravity = 0.25
bird_movement = 0

bg_surface = pygame.image.load('imgs/bg.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('imgs/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('imgs/bird2.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)      
bird_rect = bird_surface.get_rect(center = (100,512))

pipe_surface = pygame.image.load('imgs/pipe.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface,(0,0))
    bird_movement += gravity

    screen.blit(bird_surface,bird_rect)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= 576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)