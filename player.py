import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def rotate(self,dt):
        self.rotation += PLAYER_ROTATION_SPEED * dt

    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation) # this must rotate a vector by a specific angle?
        self.position += forward * PLAYER_SPEED * dt # forward is a unit vector so basically the mag == PLAYER_SPEED * dt and the direction is forward
    
    def update(self, dt):
        self.timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt) 
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt) 
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.timer > 0:
            pass
        else:
            self.timer = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x,self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
