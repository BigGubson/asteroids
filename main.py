import pygame
from asteroid import Asteroid
from player import Player
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroidfield import AsteroidField
VERSION = pygame.version.ver

def main():
	print(f"Starting Asteroids with pygame version: {VERSION}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0.0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable, )
	AsteroidField()
	while True:
		screen.fill("black")
		log_state()
		dt = (clock.tick(60)/1000)
		updatable.update(dt)
		for thing in drawable:
			thing.draw(screen)
		player.update(dt)
		pygame.display.flip()
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return

if __name__ == "__main__":
    main()
