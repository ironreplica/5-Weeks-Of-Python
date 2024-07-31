import pygame
import random
class enemy:
    # * Default position when creating the asteroid
    pos = pygame.Vector2(0, 40)
    # * Enemy rect
    this_enemy = 0
    def __init__(self, screen):
        # Defaulting to top of the screen
        enemy.pos.y = 0
        # Random width spot on the screen
        enemy.pos.x = random.randint(0, 900)
        
        # Drawing the enemy
        enemy.this_enemy = pygame.draw.circle(screen, 'white', enemy.pos, 10)
    # * Function for applying gravity
    def update(self, increment, screen):
        # Checking if its on the screen
        if(enemy.pos.y > 500):
            return
        # If it is on the screen, increment by the set speed
        enemy.pos.y += increment
        # Paint an asteroid on the screen
        enemy.this_enemy = pygame.draw.circle(screen, 'white', enemy.pos, 10)
        