#! /usr/bin/env python3
# _*_ coding: utf-8 _*_

import pygame                             # pygame
from var import Var                       # for const
from ship import Ship                     # ship
from scores import Scores
from sounds import Sounds
import game_functions as gf               # Game functions
from pygame.sprite import Group

pygame.init()
ai_var = Var()
screen = pygame.display.set_mode(
    [ai_var.screen_width,ai_var.screen_height])
pygame.display.set_caption("Alien War")
ship = Ship(screen)
sc = Scores(screen,ai_var)
sd = Sounds()
timer = pygame.time.Clock()
bullets = Group()
aliens = Group()

def main():
    while sc.game_active:                           # Game Started
        gf.check_events(ship,ai_var,screen,bullets,sc,sd)             # Check events
        ship.update(ai_var)                 # Update the status of the ship
        bullets.update()  
        aliens.update(sc)
        gf.update_aliens(aliens,screen,ai_var,bullets,sc,ship,sd)
        gf.remove(bullets,aliens,screen)  
        gf.update_screen(
            ai_var,screen,ship,bullets,aliens,sc)           # Update the screen
        timer.tick(ai_var.fps)                     # fps

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Sorry, there are some errors unexpectedly occured.")
        print("Here are the errors report: ")
        print(e)
    else:
        print("You have gained " + str(sc.score) + " points.")
        print("Thanks for playing!")