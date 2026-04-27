import math
import random
import sys
import os

import neat
import pygame

WIDTH = 1600
HEIGHT = 880

CAR_SIZE_X = 30
CAR_SIZE_Y = 30

BORDER_COLOR = (255, 255, 255, 255) 

current_generation = 0 

class Car:

    def __init__(self):
        self.sprite = pygame.image.load('car.png').convert() # Convert Speeds Up A Lot
        self.sprite = pygame.transform.scale(self.sprite, (CAR_SIZE_X, CAR_SIZE_Y))
        self.rotated_sprite = self.sprite 

        self.position = [690, 740] 
        self.angle = 0
        self.speed = 0

        self.speed_set = False 

        self.center = [self.position[0] + CAR_SIZE_X / 2, self.position[1] + CAR_SIZE_Y / 2] # Calculate Center

        self.radars = [] 
        self.drawing_radars = [] 

        self.alive = True

        self.distance = 0 
        self.time = 0 