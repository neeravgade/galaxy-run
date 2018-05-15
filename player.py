#PLAYER MODULE

import pygame
import sys
import random
import math
import os
from pygame.locals import *

#these are RGB values (in that order)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 204)
GREEN = (0, 204, 0)
RED = (255, 0, 0)
PURPLE = (204, 0, 204)
GOLD = (255, 215, 0)

class Player(pygame.sprite.Sprite):
    #This class represents the sprite that the player controls
 
    # Set speed vector
    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([17, 17])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.score = 0
 
    def changespeed(self, x, y):
        #Change the speed of the player. Called with a keypress. 
        self.change_x += x
        self.change_y += y
 
    def move(self, walls, coins):
        #coin_collect_list is the group of gold coins on the screen. The spritecollide function within pygame
        #automatically checks to see if the sprite collides with the gold coins. If so, kill the coin and add 1 to score.
        coin_collect_list = pygame.sprite.spritecollide(self, coins, False)
        for coin in coin_collect_list:
            coin.kill()
            self.score += 1

        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
            
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 