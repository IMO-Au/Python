#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import pygame                             # pygame
from var import Var                       # for const
from ship import Ship                     # ship
import game_functions as gf               # Game functions
from pygame.sprite import Group

def main():
    pygame.init()
    ai_var = Var()
    screen = pygame.display.set_mode(
        [ai_var.screen_width,ai_var.screen_height])
    pygame.display.set_caption("Alien War")
    ship = Ship(screen)
    bullets = Group()

    while True:                           # Game Started
        gf.check_events(ship,ai_var,screen,bullets)             # Check events
        ship.update(ai_var)                 # Update the status of the ship
        bullets.update()  
        gf.remove_bullets(bullets)                
        gf.update_screen(
            ai_var,screen,ship,bullets)           # Update the screen

try:
    main()
except Exception as e:
    print("Sorry, there are some errors unexpectedly occured.")
    print(e)