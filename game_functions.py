#Author: Cameron Tee
#Date: 06/03/2020
#Purpose: Module containing a number of functions that make BREAKOUT work

import sys
import pygame
from brick import Brick

def check_events(paddle, ball, settings, stats, msg):
	#Check for KB and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, paddle, ball, settings, stats, msg)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, paddle)

def check_keydown_events(event, paddle, ball, settings, stats, msg):
	#Responses to keypresses
	if event.key == pygame.K_RIGHT:
		paddle.moving_right = True
	elif event.key == pygame.K_LEFT:
		paddle.moving_left = True
	elif event.key == pygame.K_SPACE:
		stats.game_active = True
		ball.moving = True
	elif (stats.lives_left <= 0) and event.key == pygame.K_SPACE:
		reset_game(bricks, settings, screen, sb, stats)
	elif event.key == pygame.K_q: 
		sys.exit()

def check_keyup_events(event, paddle):
	#Responses to key releases
	if event.key == pygame.K_RIGHT:
		paddle.moving_right = False
	elif event.key == pygame.K_LEFT:
		paddle.moving_left = False
			

def update_screen(settings, screen, paddle, ball, bricks, sb, stats, msg):
	#Redraw screen every pass through the loop
	screen.fill(settings.bg_colour)
	sb.show_scores()
	paddle.blitme()
	ball.draw_ball()
	bricks.draw(screen)
	
	#Draw Start prompt if game is inactive
	#Check if lives < 0 and game is not active, otherwise show the start
	#prompt
	if not stats.game_active and (stats.lives_left <= 0):
		msg.show_game_over()
		check_events(paddle, ball, settings, stats, msg)
	elif not stats.game_active:
		msg.show_start()
		
	#Make the most recently flipped screen visible.
	pygame.display.flip()
	
"""
Purpose of build_wall():
Creates a full wall of bricks, 9 columns by 8 rows.
"""	

def build_wall(settings, screen, bricks):
	#Create a brick and get it's rect attributes
	brick = Brick(settings, screen)
	brick_width = brick.rect.width
	brick_height = brick.rect.height
	
	#State constants used to space and place the bricks
	col_num = 9 
	row_num = 8 
	brick_gap = 5 
	x_start = 28
	y_start = 20
	
	for row in range(row_num):
		for brick_num in range(col_num):
			brick = Brick(settings, screen)
			brick.rect.x = x_start + brick_num * (brick_width + brick_gap)
			brick.rect.y = y_start + row * (brick_height + brick_gap)
			bricks.add(brick)
	
	
"""
Purpose of update_bricks():
- Remove any brick that collides with the ball and add settings.brick_points 
to the score for any brick hit.
- Add the correct score if more than brick is hit.
- Creates a new wall if all of the bricks are destroyed.
- Also increases the dynamic settings of the game (when all bricks are destroyed).
"""	
def update_bricks(bricks, ball, screen, settings, sb, stats):	
	#Check if the Ball (sprite) hits any of the bricks (Group)
	bricks_hit_list = pygame.sprite.spritecollide(ball, bricks, True)
			
	if bricks_hit_list:	
		settings.ball_y_speed *= -1
		for brick in bricks_hit_list:
			stats.score += settings.brick_points
			sb.prep_info()
		check_hi_score(stats, sb)
	
	if len(bricks) == 0:
		#Reset the ball's position and create a new wall of bricks.
		ball.moving = False
		stats.game_active = False
		settings.increase_speed()
		
		#Increase level
		stats.level += 1
		sb.prep_level()
		
		build_wall(settings, screen, bricks)
			
def check_hi_score(stats, sb):
	#Check to see if there is a new hi-score
	if stats.score > stats.hi_score:
		stats.hi_score = stats.score
		sb.prep_hi_score()
	
"""
This is where I am currently trying to find a fix for when the lives run out.
I want to display the game over message in this case, and the stats for score,
level and lives should be reset should the player choose to start another game.
"""
def update_lives(paddle, ball, bricks, settings, screen, sb, stats):
	#-1 to self.lives_left if ball touches bottom of screen
	if ball.rect.bottom >= settings.screen_height:
		stats.lives_left -= 1
		sb.prep_info()
		if stats.lives_left > 0:
			ball.moving = False
			stats.game_active = False
		else:
			ball.moving = False
			stats.game_active = False
			
def reset_game(bricks, settings, screen, sb, stats):
	#Game stats must be reset (score, level, dynamic settings)
	stats.game_active = False
	
	#Reset the game stats and dynamic settings
	stats.reset_stats()
	settings.init_dynamic_settings()
			
	#Empty the rest of the bricks and create a new wall
	bricks.empty()
	build_wall(settings, screen, bricks)
			

