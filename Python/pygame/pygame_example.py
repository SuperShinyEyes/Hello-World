# import sys, pygame
# pygame.init()
#
# size = width, height = 320, 240
# speed = [2, 2]
# black = 0, 0, 0
#
# screen = pygame.display.set_mode(size)
# ball = pygame.image.load("ball.bmp")
# ballrect = ball.get_rect()
#
# while 1:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       sys.exit()
#
#     ballrect = ballrect.move(speed)
#     if ballrect.left < 0 or ballrect.right > width:
#       speed[0] = -speed[0]
#     if ballrect.top < 0 or ballrect.bottom > height:
#       speed[1] = -speed[1]
#
#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()

#!/usr/bin/python

import pygame
from pygame.locals import *

def main():
	# Initialise screen
	pygame.init()
	screen = pygame.display.set_mode((150, 50))
	pygame.display.set_caption('Basic Pygame program')

	# Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))

	# Display some text
	font = pygame.font.Font(None, 36)
	text = font.render("Hello There", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()

	# Event loop
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

		screen.blit(background, (0, 0))
		pygame.display.flip()


if __name__ == '__main__': main()
