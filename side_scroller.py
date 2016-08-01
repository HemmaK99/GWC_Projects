import pygame
import random
from cityscroll import * 
from block import *

pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
score = 0
lives = 10

## Font to allow for 
font = pygame.font.SysFont("Droid Sans", 45, True, False)

# Blocks for first run of game, stores them in all the lists 
make_blocks()

#check that game is not done
done = False

x = 0;
width = random.randint(50, 100)
height = random.randint(10, 400)

building_list = []

#Start game loop
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
                
    # Clear the screen
    screen.fill(WHITE)
    
    if x % 20 == 0:
       building = Building(700 + width, 500 - height, width, height, RED)
       building_list.append(building)
       
    x += 1
       
    for building in building_list:
        building.draw()
        building.move(2)
  
    x += 1

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
    # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # See if the player block has collided with anything.
    black_blocks_hit_list = pygame.sprite.spritecollide(player, black_block_list, True)
    green_blocks_hit_list = pygame.sprite.spritecollide(player, green_block_list, True)

    # Move the blocks.
    black_block_list.update()
    green_block_list.update()

    # Check the list of collisions.
    for block in green_blocks_hit_list:
        score += 1

    for block in black_blocks_hit_list:
        lives -= 1

    #Creates the scrote variables using pretty font    
    score_text = font.render("Score: " +str(score), True, BLACK)
    lives_text = font.render("Lives: "+ str(lives), True, BLUE)

    #keeps the text on the page at these coordinates
    screen.blit(score_text, [500, 50])
    screen.blit(lives_text, [50, 50])
    
    if score >= 25:
        screen.fill(GREEN)
        progress = False 
        winner_text = font.render("You win!!!", True, WHITE)
        screen.blit(winner_text, [150, 200])
        
    if lives <= 0:
        screen.fill(RED)
        progress = False
        loser_text = font.render("You lose!!!", True, WHITE)
        screen.blit(loser_text, [150, 200])

    
    # Draw the scrolling background
    #Add your scrolling background here
    #any_scroller.draw_buildings(screen)
    #any_scroller.move_buildings()

    # Draw all the sprites  
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
exit()

