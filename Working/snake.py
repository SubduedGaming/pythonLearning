#start
import pygame

#variables
game_over = 0 #0=no 1=yes


def start_window():
    pygame.init()
    dis=pygame.display.set_mode((500, 400))
    pygame.display.update()
    pygame.display.set_caption("My Snake Game!")


while game_over == 0:
    start_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = 1


pygame.quit()
quit()