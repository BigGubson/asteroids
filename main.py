import pygame
from player import Player
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
VERSION = pygame.version.ver

def main():
	print(f"Starting Asteroids with pygame version: {VERSION}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0.0
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
	while True:
		log_state()
		dt = (clock.tick(60)/1000)
		screen.fill("black")
		player.update(dt)
		player.draw(screen)
		pygame.display.flip()
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return

if __name__ == "__main__":
    main()
