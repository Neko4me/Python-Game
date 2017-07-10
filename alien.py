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

	def bitme(self):
		self.scree.blit(self.image,self.rect)
		
