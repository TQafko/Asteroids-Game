import pygame
import pygame.font
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
    pygame.font.init()
    font = pygame.font.Font(None, 100)
    print("Starting Asteroids with pygame version: VERSION")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    clockobj = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    score = 0

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
        # Inside the game loop
        score_text = font.render(f"Score: {score}", True, (255, 255, 255)) # White color
        screen.blit(score_text, (10, 10)) # Top-left corner

        for asteroid_i in asteroids:
            if asteroid_i.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                player.position.x = x
                player.position.y = y
                score = 0
        
        for asteroid_i in asteroids:
            for shot_i in shots:
                if shot_i.collides_with(asteroid_i):
                    log_event("asteroid_shot")
                    shot_i.kill()
                    asteroid_i.split()
                    score += 1

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        clockrtn = clockobj.tick(60)
        dt = clockrtn / 1000


if __name__ == "__main__":
    main()
