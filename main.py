import pygame
from constants import *

def main():
    [numpass, numfail] = pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(a,b) 
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        
        screen.fill((0,0,0))
        pygame.display.flip()
        pygame.time.wait(10)
    pygame.quit()



if __name__ == "__main__":
    main()
