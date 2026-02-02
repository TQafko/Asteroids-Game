import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids with pygame version: VERSION")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    clockobj = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(x, y)
    asteroid_field = AsteroidField()
    while(1):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for asteroid_i in asteroids:
            if asteroid_i.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                player.position.x = x
                player.position.y = y
        
        for asteroid_i in asteroids:
            for shot_i in shots:
                if shot_i.collides_with(asteroid_i):
                    log_event("asteroid_shot")
                    shot_i.kill()
                    asteroid_i.split()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        clockrtn = clockobj.tick(60)
        dt = clockrtn / 1000


if __name__ == "__main__":
    main()
