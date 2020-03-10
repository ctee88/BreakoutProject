#Author: Cameron Tee
#Date 10/03/2020
#Purpose: Class containing messages for GAME OVER and START conditions

import pygame.font

class Messages():
	
	def __init__(self, settings, screen):
		self.settings = settings
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#Set the format of the messages
		self.font_colour = (255, 255, 255)
		self.font = pygame.font.SysFont("Helvetica", 18)
		
		#Value for y co-ordinate for the drawn messages
		self.y_pos = 250
		
		self.prep_start()
		self.prep_game_over()
		
		"""
		Purpose of prep_ methods:
		Change the values into text so that they can be changed into
		images which can then be drawn to the screen.
		"""
		
	def prep_start(self):
		#Turn start msg into an image and position it slightly lower than the screen's centre
		start_str = "Press SPACE to launch ball"
		self.start_image = self.font.render(start_str, True, self.font_colour,
			self.settings.bg_colour)
		
		self.start_rect = self.start_image.get_rect()
		self.start_rect.centerx = self.screen_rect.centerx
		self.start_rect.y = self.y_pos
		
	def prep_game_over(self):
		#Turn game over msg into an image and position it slightly lower than the screen's centre
		game_over_str = "GAME OVER! Press SPACE to restart or Q to quit"
		self.game_over_image = self.font.render(game_over_str, True, self.font_colour,
			self.settings.bg_colour)
		
		self.game_over_rect = self.game_over_image.get_rect()
		self.game_over_rect.centerx = self.screen_rect.centerx
		self.game_over_rect.y = self.y_pos
	
	def show_start(self):
		#Draw the start msg onto the screen
		self.screen.blit(self.start_image, self.start_rect)
		
	def show_game_over(self):
		#Draw the game over msg onto the screen
		self.screen.blit(self.game_over_image, self.game_over_rect)
