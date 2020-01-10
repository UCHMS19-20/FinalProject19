import sys
import pygame
import random
from random import randint
from pygame.locals import *

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = {
    "width": = 500,
    "height": = 500
    }


char = {
    "width": 20,
    "height": 20,
    "x": 250,
    "y": 250,
    "velocity": 25
    }

che = { 
    "radius": 15,
    "y": 30,
    "x": randint(0, 500),
    "velocity": 20
    }

score = 0
total = 0

win = pygame.display.set_mode((screen["width"], screen["height"]))

font_score = pygame.font.SysFont("comicsans", 20) 


while True:
    pygame.time.delay(100)
    screen.fill((225, 225, 225))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        char["x"] -= char["velocity"]

    if keys[pygame.K_RIGHT]:
        char["x"] += char["velocity"]

    if keys[pygame.K_UP]:
        char['y'] -= char['velocity']
    
    if keys[pygame.K_DOWN]:
        char['y'] += char['velocity']

    pygame.draw.rect(screen, (255, 0, 0), (char["x"], char["y"], char["width"], char["height"]))
    pygame.display.update()

    textsurface = font_score.render("score: {0}/{1}".format(score, total), False, (0, 0, 0))
    win.blit(textsurface, (10, 10))
    
    pygame.display.update()

pygame.quit()

   
  

