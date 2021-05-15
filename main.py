import pygame as pg
from setting import *
import sprites
from pygame.color import THECOLORS
pg.init()
screen = pg.display.set_mode((WIDTH,HIGHT))
pg.display.set_caption("my_game")
clock = pg.time.Clock()
screen.fill(THECOLORS['black'])
all_sprites = pg.sprite.Group()
player = sprites.Player(WIDTH/2,HIGHT/2)
all_sprites.add(player)
while True:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    player.move()
    all_sprites.update()
    all_sprites.draw()
    pg.display.filp()