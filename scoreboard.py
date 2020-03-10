#Author: Cameron Tee
#Date: 09/03/2020
#Purpose: A class providing live updates to the player stats: Score and Lives
import pygame.font

class Scoreboard():
	
	def __init__(self, settings, screen, stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = stats
			
		#Font settings for score information
		self.font_colour = (255, 255, 255)
		#Instantiate a font object (specific font)
		self.font = pygame.font.SysFont("Helvetica", 18) #None: 24
		
		#Prepare initial score and lives images
		self.prep_info()
		self.prep_hi_score()
		self.prep_level()
		
	"""
	Purpose of prep_ methods:
	Change the values into text so that they can be changed into
	images which can then be drawn to the screen.
	"""
	
	def prep_info(self):
		#Change score and lives to be displayed as an image (to be drawn)
		score_str = "{:,}".format(self.stats.score)
		lives_str = str(self.stats.lives_left)
		self.info_image = self.font.render("SCORE: {} LIVES: {}".format(score_str, lives_str), 
			True, self.font_colour, self.settings.bg_colour)
		
		#Display the information at the top left of the screen
		self.info_rect = self.info_image.get_rect()
		self.info_rect.x = 0
		self.info_rect.top = self.screen_rect.top
		
	def prep_hi_score(self):
		#Change hi-score to be displayed as an image (to be drawn)
		hi_score_str = "{:,}".format(self.stats.hi_score)
		self.hi_score_image = self.font.render("HIGHSCORE: {}".format(hi_score_str),
		 True, self.font_colour, self.settings.bg_colour)
			
		#Display the hi-score at the top right of the screen
		self.hi_score_rect = self.hi_score_image.get_rect()
		self.hi_score_rect.right = self.screen_rect.right
		self.hi_score_rect.top = self.screen_rect.top
		
	def prep_level(self):
		#Change level to be displayed as an image (to be drawn)
		level = self.stats.level
		self.level_image = self.font.render("LEVEL {}".format(level), True,
			self.font_colour, self.settings.bg_colour)
		
		#Display the level in the top, middle of the screen
		self.level_rect = self.level_image.get_rect()
		self.level_rect.centerx = self.screen_rect.centerx
		self.level_rect.top = self.screen_rect.top
		
	def show_scores(self):
		#Draw the game information to the screen
		self.screen.blit(self.info_image, self.info_rect)
		self.screen.blit(self.hi_score_image, self.hi_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
