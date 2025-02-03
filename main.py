import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    updatable = pygame.sprite.Group() # creating sprite group called updatable to hold all updatable sprites
    drawable = pygame.sprite.Group() # creating sprite group called drawable to hold all drawable sprites
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # adding a static containers variable to Player class. This will add all future instances of Player to each of these groups 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

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


        pygame.display.flip()
        dt = clock.tick(60)/1000 # pauses the game loop until 1/60th of a second has passed (in other words fps)
        
if __name__ == "__main__":
    main()
