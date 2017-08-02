import sys
import pygame
from pygame.sprite import Group
from setting import setting
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import functions as gf

def run_game():
	pygame.init()
	ai_setting=setting()
	scree=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_hight))
	aliens=Group()
	ship=Ship(scree,ai_setting)
	alien=Alien(ai_setting,scree)
	gf.create_fleet(ai_setting,scree,ship,aliens)
	bullets=Group()
	pygame.display.set_caption('New game')
	stats=GameStats(ai_setting)
	sb=Scoreboard(ai_setting,scree,stats)
	play_button=Button(ai_setting,scree,"Play")

	while True:
		gf.check_events(ship,ai_setting,scree,bullets,stats,play_button,aliens)
		if stats.game_active:
			ship.update()
			gf.update_aliens(ai_setting,aliens,ship,stats,bullets,scree)
			gf.update_bullet(ai_setting,scree,ship,aliens,bullets,sb,stats)
		gf.update_screen(ai_setting,scree,ship,bullets,aliens,play_button,stats,sb)
run_game()