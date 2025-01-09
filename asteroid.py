import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(center=self.position, radius=self.radius, width=2, surface=screen, color=(255,255,255))
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        direction_1, direction_2 = (self.velocity.rotate(angle), self.velocity.rotate(-angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_1, split_2 = (Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius))
        split_1.velocity = direction_1 * 1.2
        split_2.velocity = direction_2 * 1.2