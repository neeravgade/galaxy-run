#i followed the tutorial on a website for this 
#the url is http://programarcadegames.com/python_examples/show_file.php?file=maze_runner.py
import pygame
import sys
import random
import math
import os
from pygame.locals import *
import signal
from player import *
import time

#these are RGB values (in that order)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 204)
GREEN = (0, 204, 0)
RED = (255, 0, 0)
PURPLE = (204, 0, 204)
GOLD = (255, 215, 0)

# init pygame
pygame.init()
# init sound mixer
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

# background music
pygame.mixer.music.load("JS.mp3.mp3")
pygame.mixer.music.set_volume(1)

# loop background music and make it play
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(.5)

#this gets the background image from the directory
imr_dir = "C:/Users/Neerav.Gade18/OneDrive - Bellarmine College Preparatory/CompPrgm/finalPROJECT/galaxy-run/galaxy-run"

#make a wall class 
class Wall(pygame.sprite.Sprite):
    #this class represents the bar at the bottom that the player controls 
 
    def __init__(self, x, y, width, height, color):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
class Coin(pygame.sprite.Sprite):
    #this class represents the group of "coins" on the screen
    #i can use the same format as the wall class
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a GOLD square that the Player sprite can collect
        self.image = pygame.Surface([15, 15])
        self.image.fill(GOLD)
 
        # Make our top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
class Room(object):
    """ Base class for all rooms. """
 
    # Each room has a list of walls, and of coin sprites.
    wall_list = None
    coin_list = None

    def __init__(self):
        #Constructor, create our lists.
        self.wall_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()
 
class Room1(Room):
    #This creates all the walls in room 1
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 250, BLUE], #left top
                 [0, 350, 20, 250, BLUE], #left bottom
                 [780, 0, 20, 250, BLUE], #right top
                 [780, 350, 20, 250, BLUE], #right bottom
                 [20, 0, 760, 20, BLUE], #entire top
                 [20, 580, 760, 20, BLUE], #entire bottom
                 [390, 50, 20, 500, WHITE] #this is the wall in the middle
                ]

        #the same way we made walls, this is the list for coins BUT we are using random function to randomize 
        #where the coins are on the screen each time program runs.
        coins = []
        for i in range(20):
            x = random.randint(40,760)
            y = random.randint(40,560)
            coins.append([x,y])

        for item in coins:
            coin = Coin(item[0], item[1])
            self.coin_list.add(coin)

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
class Room2(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 250, PURPLE],
                 [780, 350, 20, 250, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE],
                 [190, 50, 20, 500, WHITE],
                 [590, 50, 20, 500, WHITE]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        coins = []
        for i in range(20):
            x = random.randint(40,760)
            y = random.randint(40,560)
            coins.append([x,y])

        for item in coins:
            coin = Coin(item[0], item[1])
            self.coin_list.add(coin)

class Room3(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, RED], 
                 [0, 350, 20, 250, RED], 
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, WHITE)
                self.wall_list.add(wall)
 
        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, WHITE)
            self.wall_list.add(wall)
 
        coins = []
        for i in range(20):
            x = random.randint(40,760)
            y = random.randint(40,560)
            coins.append([x,y])

        for item in coins:
            coin = Coin(item[0], item[1])
            self.coin_list.add(coin)

#MAIN FUNCTION
def main():
    """ Main Program """
 
    # Call this function so the Pygame library can initialize itself
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 
    # Set the title of the window
    pygame.display.set_caption('GALAXY RUN')
 
    # Create the player paddle object
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
 
    rooms = []
 
    room = Room1()
    rooms.append(room)
 
    room = Room2()
    rooms.append(room)
 
    room = Room3()
    rooms.append(room)
 
    current_room_no = 0
    current_room = rooms[current_room_no]
 
    clock = pygame.time.Clock()
    #load background image
    background_image = pygame.image.load("stars.png").convert()

    #represents the first position of the moving background image
    x=0

    #make the game run for 50 seconds then quit program
    start = time.time()
    while time.time() - start < 50:
        #put the score in the top left corner of the game
        pygame.display.set_caption("Score: " + str(player.score))

        #event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #the x,y speed for when each key is pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
                if event.key == pygame.K_q:
                    pygame.quit()
            #the x,y speed for when each key is NOT pressed down
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
 
        # Game Logic
        player.move(current_room.wall_list,current_room.coin_list)
 
        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790
 
        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0
 
        #background and sprites
        screen.blit(background_image, [x,0])
        x-=1

        #draw the sprites on the screen
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
        current_room.coin_list.draw(screen)

        pygame.display.flip()

        #60 frames per second
        clock.tick(60)


    pygame.quit()
 
if __name__ == "__main__":
    main()