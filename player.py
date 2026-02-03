import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        self.life = PLAYER_LIFE

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation = self.rotation +  PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = SCREEN_HEIGHT
        if self.position.y < 0:
            self.position.y = 0
        if self.position.x > SCREEN_WIDTH:
            self.position.x = SCREEN_WIDTH
        if self.position.x < 0:
            self.position.x = 0
    
    def hit(self):
        self.life -= 1
        if self.life <= 0:
            self.kill()
            return 1
            

    def shoot(self):
        if self.shot_cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED
        shot.velocity += rotated_with_speed_vector
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt

        if keys[pygame.K_a]:
            dt = abs(dt) * -1
            self.rotate(dt)
        if keys[pygame.K_d]:
            dt = abs(dt)
            self.rotate(dt)
        if keys[pygame.K_w]:
            dt = abs(dt)
            self.move(dt)
        if keys[pygame.K_s]:
            dt = abs(dt) * -1
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()