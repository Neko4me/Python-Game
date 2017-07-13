import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	def __init__(self,ai_setting,scree):
		super().__init__()
		self.scree=scree
		self.ai_setting=ai_setting
		self.image=pygame.image.load('images/alien.bmp')
		self.rect=self.image.get_rect()
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		self.x=float(self.rect.x)

	def check_edges(self):
		scree_rect=self.scree.get_rect()
		if self.rect.right>=scree_rect.right:
			return True
		elif self.rect.left<=0:
			return True

	def update(self):
		self.x+=(self.ai_setting.alien_speed*self.ai_setting.fleet_direction)
		self.rect.x=self.x
		pass

	def bitme(self):
		self.scree.blit(self.image,self.rect)
		
