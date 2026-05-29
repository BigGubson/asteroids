import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
class Asteroid(CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
    		super().__init__(x, y, radius)

	def draw(self, screen: pygame.Surface) -> None:
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			rng = random.uniform(20, 50)
			rotate1 = self.velocity.rotate(rng)
			rotate2 = -self.velocity.rotate(rng)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid1 = Asteroid(self.position, self.velocity, new_radius)
			asteroid2 = Asteroid(self.position, self.velocity, new_radius)
			asteroid1.velocity = rotate1 * 1.2
			asteroid2.velocity = rotate2 * 1.2

	def update(self, dt: float) -> None:
		self.position += (self.velocity * dt)
