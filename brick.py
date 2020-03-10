#Author: Cameron Tee
#Date: 07/03/2020
#Purpose: A class managing the properties of the bricks

import pygame

class Brick(pygame.sprite.Sprite):
	
	def __init__(self, settings, screen):
		#Initialize the brick image and get its rect attribute
		super().__init__()
		self.screen = screen
		
		self.image = pygame.image.load('images/brick_1.bmp')
		self.rect = self.image.get_rect()
	
	def blitme(self):
		#Draw the brick at its current location
		self.screen.blit(self.image, self.rect)
		
		
