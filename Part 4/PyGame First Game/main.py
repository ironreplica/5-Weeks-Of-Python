import pygame
from enemy import enemy
import threading
# Pygame setup
pygame.init()
screen = pygame.display.set_mode((900,500))
clock = pygame.time.Clock()

# Game running Status
running = True

# Delta Time
dt = 0
gt = 0
curtime = 1
curtimeM = 1
# Centering the player
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() - 30)
player_size = 30
# Asteroid Data
cur_asteroids = []
max_asteroids = 5

def update_asteroid(asteroid, increment, screen):
    asteroid.update(increment, screen)
def shootProjectile():
    # if the player is not shooting
        # shoot a ray out from the player 
    pass

# * Main Game loop
while running:
    # * Pygame quit means a user clicked the x to close the app.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    color = (200,200,0)
    
    # * Fill the screen to black
    screen.fill('black')
    
    # * Creating the player
    player_shape = pygame.Rect(player_pos.x , player_pos.y, player_size,30)
    player = pygame.draw.rect(screen, 'white', player_shape)
        
    # * Time, Limit FPS to 60
    dt = clock.tick(60) / 1000
    gt = round(pygame.time.get_ticks()/1000) # Game time in seconds
    gtm = round(pygame.time.get_ticks()/100) # Game time in miliseconds
    
    # * Creating an array of threads to update all objects gravity at once
    threads = []
    # * Utilizing list comprehension you can adjust the list of asteroids to only includes asteroids on screen
    cur_asteroids = [asteroid for asteroid in cur_asteroids if asteroid.pos.y < 500]
    
    # * List for current asteroids rect objects to detect collision
    cur_asteroids_rect = [asteroid.this_enemy for asteroid in cur_asteroids]
    
    for asteroid in cur_asteroids:
        thread = threading.Thread(target=update_asteroid, args=(asteroid,10,screen))
        threads.append(thread)
        thread.start()

    # * Wait for threads to finish
    for thread in threads:
        thread.join()
    # * Executes every second
    if(gt > curtime):
        curtime+=1
        if(len(cur_asteroids) < max_asteroids):
            newEnemy = enemy(screen)
            cur_asteroids.append(newEnemy)

    # * Controls
        # Move the player around using the keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos.x -= 500 * dt 
    if keys[pygame.K_d]:
        player_pos.x += 500 * dt 
        
    # * Collision
    collide = player.collidelist(cur_asteroids_rect)
    if(collide == 0):
        player_size+=5
        
    # * Have to flip the display to work on the screen
    pygame.display.flip()
        
pygame.quit()

