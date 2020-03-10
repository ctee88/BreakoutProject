#Author: Cameron Tee
#Date: 06/03/2020
#Purpose: Controls the running of the game.

import pygame

from pygame.sprite import Group
from settings import Settings
from paddle import Paddle
from ball import Ball
from game_stats import GameStats
from scoreboard import Scoreboard
from messages import Messages
import game_functions as gf

def run_game(): 
	# Initialize pygame, settings and screen object
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode(
		(settings.screen_width, settings.screen_height))
	pygame.display.set_caption("BREAKOUT clone by Cameron Tee")
	
	#Instantiate GameStats, Scoreboard and Messages
	stats = GameStats(settings)
	sb = Scoreboard(settings, screen, stats)
	msg = Messages(settings, screen)

	#Make the paddle, ball and group of bricks
	paddle = Paddle(settings, screen)
	ball = Ball(settings, screen, paddle)
	bricks = Group()
	
	#Creates a 'wall' (rows and columns) of bricks
	gf.build_wall(settings, screen, bricks)
	
	#Clock controlling the frequency of the screen updates
	clock = pygame.time.Clock()
	
    #Begin the main loop for the game
	while True:
		gf.check_events(paddle, ball, settings, stats, msg)
		if not stats.game_active:
			paddle.update()
			ball.center_ball(paddle)			
		
		if stats.game_active:
			paddle.update()
			ball.update(paddle)
			gf.update_lives(paddle, ball, bricks, settings, screen, sb, stats)
			gf.update_bricks(bricks, ball, screen, settings, sb, stats)
		
		gf.update_screen(settings, screen, paddle, ball, bricks, sb, stats,
			msg)
			
		#At most 120 frames will pass per second
		clock.tick(120)	

run_game()

