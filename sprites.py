from setting import HIGHT, WIDTH
import pygame as pg
from pygame.color import THECOLORS
class Player(pg.Sprite.sprite):
    def __init__(self,x,y):
        pg.Sprite.sprite.__init__()
        self.x = x
        self.y = y
        self.image = pg.Surafe((50,50))
        self.image.fill(THECOLORS['green'])
        self.rect = self.image.get_rect()
        self.rect.center = ((x,y))
    def move(self):
        key = pg.get_pressed()
        if key[pg.K_UP]:
            self.y += -5
        if key[pg.K_DOWN]:
            self.y += 5
        if key[pg.K_RIGHT]:
            self.x += 5
        if key[pg.K_LEFT]:
            self.x -= 5
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = HIGHT
        if self.rect.top > HIGHT:
            self.rect.bottom = 0 

