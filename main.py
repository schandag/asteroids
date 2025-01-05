# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for up in updatable:
            up.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if asteroid.collision(bullet):
                    bullet.kill()
                    asteroid.split()
        for dr in drawable:
            dr.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()