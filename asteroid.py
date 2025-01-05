
import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(random_angle) * 1.2
            vel2 = self.velocity.rotate(-random_angle) * 1.2
            rad = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position[0], self.position[1], rad)
            asteroid_2 = Asteroid(self.position[0], self.position[1], rad)
            asteroid_1.velocity = vel1
            asteroid_2.velocity = vel2
