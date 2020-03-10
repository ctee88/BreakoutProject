#Author: Cameron Tee
#Date: 06/03/2020
#Purpose: A class managing the behaviour of the player-controlled paddle

import pygame

class Paddle(pygame.sprite.Sprite):
    
	def __init__(self, settings, screen):
		#Initialize the paddle and its starting position
		super().__init__()
		self.screen = screen
		self.settings = settings

		#Load the paddle image and get its rect attributes
		self.image = pygame.image.load('images/paddle_2.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start the paddle at the bottom, centre of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Movement flags
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update the position of the paddle based on the movement flag"""
		#Update the paddle's center value with speed factor
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.settings.paddle_speed
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= self.settings.paddle_speed
		
	def blitme(self):
		#Draw the paddle at its current location
		self.screen.blit(self.image, self.rect)

