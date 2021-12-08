# Simple Animation with PyGame, Tyler Fann, 12/08/21, 12:50, v0.3

from _typeshed import ReadableBuffer
import pygame, sys, time
from pygame.locals import *

# Setup PyGame
pygame.init()

# Setup the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Setup the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Setup color values.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)