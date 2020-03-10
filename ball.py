#Author: Cameron Tee
#Date: 07/03/2020
#Purpose: A class managing the behaviour of the ball

import pygame

class Ball(pygame.sprite.Sprite):
	
	def __init__(self, settings, screen, paddle):
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		#Generate ball and get its rect attributes, positioning and colour
		self.rect = pygame.Rect(0, 0, settings.ball_width, 
			settings.ball_height)
		self.center_ball(paddle)		
		self.colour = settings.ball_colour
		
		#Construct screen width to see if ball touches the edges
		self.screen_width = settings.screen_width
		
		#Movement flag
		self.moving = False
		
	def bounce(self, paddle):
		#Check whether the ball touches the top, left or right walls.
		if self.rect.top <= 0:
			self.settings.ball_y_speed *= -1
		if self.rect.right >= self.screen_width:
			self.settings.ball_x_speed *= -1
		if self.rect.left <= 0:
			self.settings.ball_x_speed *= -1
		
		#Check whether the ball hits the paddle. Add 1 to ball's y co-ord (so it appears just above the paddle)
		if self.rect.colliderect(paddle.rect):
			self.rect.bottom = paddle.rect.top + 1
			self.settings.ball_y_speed *= -1
		
	def center_ball(self, paddle):
		#Center the ball in the correct position
		self.rect.centerx = paddle.rect.centerx
		self.rect.bottom = paddle.rect.top	
			
	def update(self, paddle):
		#Update the ball position with paddle before ball release.
		if self.moving == False:
			self.center_ball(paddle)
		if self.moving == True:
		#Update the ball position when the ball is released
			self.rect.x += self.settings.ball_x_speed
			self.rect.y += self.settings.ball_y_speed
			self.bounce(paddle)		
		
	def draw_ball(self):
		#Draw the ball at its current location
		pygame.draw.rect(self.screen, self.colour, self.rect)
