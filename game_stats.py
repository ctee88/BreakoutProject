#Author: Cameron Tee
#Date: 08/03/2020
#Purpose: Class used to keep track of game statistics

class GameStats():
	"""Track stats for BREAKOUT"""
	
	def __init__(self, settings):
		self.settings = settings
		self.reset_stats()
		
		#Begin the game in an inactive state
		self.game_active = False
		
		#Hi-score should never be reset
		self.hi_score = 0
		
	def reset_stats(self):
		"""These stats can change during the game."""
		self.lives_left = self.settings.lives
		self.score = 0
		self.level = 1
