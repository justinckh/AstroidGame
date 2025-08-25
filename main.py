import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    [numpass, numfail] = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_running = True

    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    while game_running:
        #if close window close game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        #blackbackground
        screen.fill((0,0,0))

        #draw all drawable objects
        for drawers in drawable:
            drawers.draw(screen)
        #check for player astrioid collisions
        for asteroid in asteroids:
             if  asteroid.check_collision(player):
                sys.exit("Game over!")
        #check for bullet hit
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
        #update all updateable objects
        updateable.update(dt)
        #update the display
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    pygame.quit()



if __name__ == "__main__":
    main()
