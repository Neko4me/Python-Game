import pygame.font
class Scoreboard():
	def __init__(self,ai_setting,scree,stats):
		self.scree=scree
		self.scree_rect=scree.get_rect()
		self.ai_setting=ai_setting
		self.stats=stats
		self.text_color=(30,30,30)
		self.font=pygame.font.SysFont(None,48)
		self.prep_score()

	def prep_score(self):
		rounded_score=int(round(self.stats.score,-1))
		score_str="{:,}".format(rounded_score)
		self.score_image=self.font.render(score_str,True,self.text_color,self.ai_setting.bg_color)
		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.scree_rect.right-20
		self.scree_rect.top=20

	def show_score(self):
		self.scree.blit(self.score_image,self.score_rect)
		