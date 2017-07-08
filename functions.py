import sys
import pygame
from bullet import Bullet
def chekc_keydown_events(event,ai_setting,scree,ship,bullets):
	if event.key==pygame.K_SPACE:
		if len(bullets)<ai_setting.bullet_allow:
			new_bullet=Bullet(ai_setting,scree,ship)
			bullets.add(new_bullet)
	
def check_events(ship,ai_setting,scree,bullets):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			chekc_keydown_events(event,ai_setting,scree,ship,bullets)
			if event.key==pygame.K_RIGHT:
				ship.moving_right=True
			elif event.key==pygame.K_LEFT:
				ship.moving_left=True

		elif event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT:
				ship.moving_right=False
			elif event.key==pygame.K_LEFT:
				ship.moving_left=False
				

def update_screen(ai_setting,scree,ship,bullets):
	scree.fill(ai_setting.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.bitme()
	pygame.display.flip()

def update_bullet(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)