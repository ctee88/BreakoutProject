#Author: Cameron Tee
#Date: 07/03/2020
#Purpose: A class managing the behaviour of the ball

import pygame
#from pygame.sprite import Sprite

class Ball(pygame.sprite.Sprite):
	
	def __init__(self, settings, screen, paddle):
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		#Load the ball image and get its rect attributes
		#Must make the ball from the class pygame.Rect() and make the ball
		#from scratch due to the black corners
		#self.image = pygame.image.load('images/ball_1.bmp')
		self.rect = pygame.Rect(0, 0, settings.ball_width, 
			settings.ball_height)
			
		self.center_ball(paddle)
		
		self.colour = settings.ball_colour
		
		#Velocity
		#self.ball_x_speed = settings.ball_x_speed
		#self.ball_y_speed = settings.ball_y_speed
		
		#Screen dimensions
		self.screen_width = settings.screen_width
		#self.screen_height = settings.screen_height
		
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
		
		#Check whether the ball hits the paddle.
		if self.rect.colliderect(paddle.rect):
			"""
			+1 adds one pixel to the position of the bottom of the ball.
			This ensures that when the ball collides with the paddle, the
			new position of the ball (just before its velocity is reversed)
			is just above (by 1 pixel) the top of the paddle.
			This fixed the bug of the ball going inside of the paddle 
			(when colliiding with the top left/top right of the paddle) and
			bouncing of the top and bottom of the paddle before being released
			"""
			self.rect.bottom = paddle.rect.top + 1
			self.settings.ball_y_speed *= -1
		
	def center_ball(self, paddle):
		self.rect.centerx = paddle.rect.centerx
		self.rect.bottom = paddle.rect.top	
		
	#def update(self, paddle):	
	def update(self, paddle):
		#Update the ball position with paddle before ball release.
		if self.moving == False:
			self.center_ball(paddle)
			#self.rect.centerx = paddle.rect.centerx
			#self.rect.bottom = paddle.rect.top
		if self.moving == True:
			self.rect.x += self.settings.ball_x_speed
			self.rect.y += self.settings.ball_y_speed
			self.bounce(paddle)		
		
	def draw_ball(self):
		#Draw the ball at its current location
		pygame.draw.rect(self.screen, self.colour, self.rect)
		
