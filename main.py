import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    updatable = pygame.sprite.Group() # creating sprite group called updatable to hold all updatable sprites
    drawable = pygame.sprite.Group() # creating sprite group called drawable to hold all drawable sprites
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable) # adding a static containers variable to Player class. This will add all future instances of Player to each of these groups 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots) # This is nuts I only every create a Shot in the player class but because I edit
                                                   # the class to have a containers attribute every time hereafter it will update and draw!

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    astroid_field = AsteroidField() 
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        updatable.update(dt)

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit(1)

            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill() # built-in pygame method it will remove the object from all groups!
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60)/1000 # pauses the game loop until 1/60th of a second has passed (in other words fps)
        
if __name__ == "__main__":
    main()
