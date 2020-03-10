#Author: Cameron Tee
#Date: 07/03/2020
#Purpose: A class managing the behaviour of the blocks

import pygame
from pygame.sprite import Sprite

class Brick(Sprite):
	
	def __init__(self, settings, screen):
		"""Initialize the block and its starting position"""
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		#Load the block image and get its rect attribute
		self.image = pygame.image.load('images/block.bmp')
		self.rect = self.image.get_rect()
		
		#Start each block at the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#Store the exact position of the block
		self.x = float(self.rect.x)
	
	def blitme(self):
		"""Draw the block at its current location"""
		self.screen.blit(self.image, self.rect)
		
		
