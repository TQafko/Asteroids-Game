import pygame
import pygame.font
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from gamestats import GameStats

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

print("Starting Asteroids with pygame version: VERSION")
print("Screen width:", SCREEN_WIDTH)
print("Screen height:", SCREEN_HEIGHT)

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
gamestats = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, drawable, updatable)
GameStats.containers = (gamestats, drawable)

gamestats = GameStats()
current_scene = "main_menu"

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    global current_scene
    while current_scene == "main_menu":
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    current_scene = "game" 
                if exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        font = pygame.font.Font(None, 74)
        draw_text('Main Menu', font, "white", screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        
        score, _, _ = gamestats.get_stats()
        draw_text(f'Score: {score}', font, "white",screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5)

        play_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
        pygame.draw.rect(screen, "white", play_button_rect)
        draw_text('Play', pygame.font.Font(None, 40), "black", screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)

        exit_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 70, 200, 50)
        pygame.draw.rect(screen, "white", exit_button_rect)
        draw_text('Exit', pygame.font.Font(None, 40), "black", screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 95)

        pygame.display.update()

def game_loop():
    global current_scene
    clockobj = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    score = 0

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while current_scene == "game":
        screen.fill("black")

        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)
        gamestats.update(score, player.life, dt)

        for asteroid_i in asteroids:
            if asteroid_i.collides_with(player):
                log_event("player_hit")
                player.position.x = x
                player.position.y = y
                dead = player.hit()
                gamestats.update(score, player.life, dt)
                if dead == 1:
                    player.kill()
                    for asteroid_i in asteroids:
                        asteroid_i.kill()
                    print("Game Over!")
                    print("(Score, Life, Time Elapsed)",gamestats.get_stats())
                    current_scene = "main_menu"
        
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
    while True:
        if current_scene == "main_menu":
            main_menu()
        elif current_scene == "game":
            game_loop()
