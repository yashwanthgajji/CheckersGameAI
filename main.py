import pygame
from checkers.constants import *
from checkers.board import *
from checkers.game import Game
from minimax.algorithm import *
pygame.font.init()

FPS=60

WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Checkers")

def get_row_col_from_mouse(pos):
    x,y=pos
    row=y//SQUARE_SIZE
    col=x//SQUARE_SIZE
    return row,col

def main():
    run=True
    cloak=pygame.time.Clock()
    game=Game(WIN)

    while run:
        cloak.tick(FPS)

        if game.turn==WHITE:
            value,new_board=minimax(game.get_board(),AI_ALGO_DEPTH,WHITE,game)
            game.ai_move(new_board)

        if game.winner()!=None:
            print(game.winner())
            f = pygame.font.SysFont('freesansbold.ttf', 32)
            text = f.render('Winner!!!', True, WHITE, BLUE)
            textRect = text.get_rect()
            textRect.center = (WIDTH // 2, HEIGHT // 2)
            WIN.blit(text, textRect)
            pygame.time.delay(1000)
            run=False

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                row,col=get_row_col_from_mouse(pos)
                game.select(row,col)

        game.update()

    pygame.quit()

main()