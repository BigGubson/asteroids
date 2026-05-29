import pygame
import sys
from logger import log_event
from asteroid import Asteroid
from player import Player
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroidfield import AsteroidField
from shot import Shot
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
	shots = pygame.sprite.Group()
	Shot.containers = (shots, drawable, updatable)
	
	while True:
		screen.fill("black")
		log_state()
		dt = (clock.tick(60)/1000)
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				sys.exit()
			for shot in shots:
				if asteroid.collides_with(shot):
					log_event("asteroid_shot")
					shot.kill()
					asteroid.split()
		for thing in drawable:
			thing.draw(screen)
		player.update(dt)
		pygame.display.flip()
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return

if __name__ == "__main__":
    main()
