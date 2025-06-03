import pygame, sys

class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		# self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('catwalk/1.png'))
		self.sprites.append(pygame.image.load('catwalk/2.png'))
		self.sprites.append(pygame.image.load('catwalk/3.png'))
		self.sprites.append(pygame.image.load('catwalk/4.png'))
		self.sprites.append(pygame.image.load('catwalk/5.png'))
		self.sprites.append(pygame.image.load('catwalk/6.png'))
		self.sprites.append(pygame.image.load('catwalk/7.png'))
		self.sprites.append(pygame.image.load('catwalk/8.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,):
		# if self.attack_animation == True:
		self.current_sprite += 1
		if int(self.current_sprite) >= len(self.sprites):
			self.current_sprite = 0
				# self.attack_animation = False

		self.image = self.sprites[int(self.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		'''if event.type == pygame.KEYDOWN:
			player.attack()'''

	# Drawing
	screen.fill((0,0,0))
	moving_sprites.draw(screen)
	moving_sprites.update()
	pygame.display.flip()
	clock.tick(60)