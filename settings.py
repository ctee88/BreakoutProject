#Author: Cameron Tee
#Date: 06/03/2020
#Purpose: A class storing all the settings for Breakout

class Settings():

	def __init__(self):
		#Screen settings
		self.screen_width = 640
		self.screen_height = 480
		self.bg_colour = (0, 0, 0)
		
		#Ball settings
		self.ball_width = 10
		self.ball_height = 10
		self.ball_colour = (230, 230, 230)
		
		#Lives settings
		self.lives = 5
		
		#Factors in which the game changes between levels
		self.paddle_speedup_scale = 1.1
		self.ball_x_speedup_scale = 1.2
		self.ball_y_speedup_scale = 1.2
		self.brick_points_scale = 2
		
		self.init_dynamic_settings()
		
	def init_dynamic_settings(self):
		#Sets initial values for dynamic game settings
		self.paddle_speed = 3 
		self.ball_x_speed = 2
		self.ball_y_speed = -2
		self.brick_points = 1000
		
	def increase_speed(self):
		self.ball_x_speed *= self.ball_x_speedup_scale
		self.ball_y_speed *= self.ball_y_speedup_scale
		self.paddle_speed *= self.paddle_speedup_scale
		self.brick_points *= self.brick_points_scale
