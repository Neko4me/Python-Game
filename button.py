import pygame.font
class Button():
	def __init__(self,ai_setting,scree,msg):
		self.scree=scree
		self.screen_rect=scree.get_rect()
		self.width,self.height=200,50
		self.button_color=(88,87,86)
		self.text_color=(255,255,255)
		self.font=pygame.font.SysFont(None,48)
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center
		self.prep_msg(msg)
		
	def prep_msg(self,msg):
		self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center

	def draw_button(self):
		self.scree.fill(self.button_color,self.rect)
		self.scree.blit(self.msg_image,self.msg_image_rect)
		