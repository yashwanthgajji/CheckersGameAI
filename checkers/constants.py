import pygame

#window consts
WIDTH,HEIGHT=800,800
ROWS,COLS=8,8
SQUARE_SIZE=WIDTH//COLS

#RGB
RED=(255,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
BLACK=(0,0,0)
GREY=(128,128,128)

CROWN=pygame.transform.scale(pygame.image.load('assets/crown.png'),(44,25))

AI_ALGO_DEPTH=2