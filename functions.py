import sys
import pygame
from bullet import Bullet
from alien import Alien
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
				

def update_screen(ai_setting,scree,ship,bullets,aliens):
	scree.fill(ai_setting.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.bitme()
	aliens.draw(scree)
	pygame.display.flip()

def update_bullet(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)

def get_number_row(ai_setting,ship_height,alien_height):
	available_space_y=(ai_setting.screen_hight-(2*alien_height)-ship_height)
	number_rows=int(available_space_y/(3*alien_height))
	return number_rows

def get_number_alien_x(ai_setting,alien_width):
	available_space_x=ai_setting.screen_width -1.5*alien_width
	number_aliens_x=int(available_space_x/(1.5*alien_width))
	return number_aliens_x

def create_alien(ai_setting,scree,aliens,alien_number,row_number):
	alien=Alien(ai_setting,scree)
	alien_width=alien.rect.width
	alien.x=alien_width+1.5*alien_width*alien_number
	alien.rect.x=alien.x
	alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
	aliens.add(alien)

def create_fleet(ai_setting,scree,ship,aliens):
	alien=Alien(ai_setting,scree)
	number_aliens_x=get_number_alien_x(ai_setting,alien.rect.width)
	number_rows=get_number_row(ai_setting,ship.rect.height,alien.rect.height)
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_setting,scree,aliens,alien_number,row_number)

def check_fleet_edges(ai_setting,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_setting,aliens)
			break

def change_fleet_direction(ai_setting,aliens):
	for alien in aliens.sprites():
		alien.rect.y+=ai_setting.fleet_drop_speed
	ai_setting.fleet_direction*=-1

def update_aliens(ai_setting,aliens):
	check_fleet_edges(ai_setting,aliens)
	aliens.update()
	pass
			
