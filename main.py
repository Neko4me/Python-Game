import sys
import pygame
from pygame.sprite import Group
from setting import setting
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
	

	while True:
		gf.check_events(ship,ai_setting,scree,bullets)
		ship.update()
		gf.update_bullet(bullets)
		gf.update_screen(ai_setting,scree,ship,bullets,aliens)
run_game()