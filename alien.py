#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import pygame
from random import randint
from pygame.sprite import Sprite

class Alien():
    def __init__(self,screen,ai_var):
        super(Alien,self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = randint(0,ai_var.screen_width)
        self.rect.y = randint(0,ai_var.screen_height)
    
    def blit_me(self):
        self.screen.blit(self.image,self.rect)