from pygame_functions import *
import time

setAutoUpdate(False)
WIDTH = 1000
HEIGHT = 800
screenSize(WIDTH, HEIGHT)
#setBackgroundImage('bg5.jpg')

class Player():
	def __init__(self):
		self.pos_x = 400
		self.pos_y = 400
		self.feet_pos_y = 400
		self.feet_pos_x = 400
		self.speed = 3
		self.health = 100
		self.xdir = 0
		self.ydir = 0
		self.frame = 0
		self.timeOfNextFrame = clock()
		self.current_weapon = 0
		self.walking = False
		self.direction = 0

		self.footstep = makeSound('sounds/foot.ogg')

		self.feet = makeSprite('survivor/feet/walk/survivor-walk_0.png')
		transformSprite(self.feet,180,0.3)

		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_1.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_2.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_3.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_4.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_5.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_6.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_7.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_8.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_9.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_10.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_11.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_12.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_13.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_14.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_15.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_16.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_17.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_18.png')
		addSpriteImage(self.feet, 'survivor/feet/walk/survivor-walk_19.png')
		showSprite(self.feet)

		self.sprite_knife = makeSprite('survivor/knife/move/survivor-move_knife_0.png' )
		transformSprite(self.sprite_knife,180,0.3)
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_1.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_2.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_3.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_4.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_5.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_6.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_7.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_8.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_9.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_10.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_11.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_12.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_13.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_14.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_15.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_16.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_17.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_18.png' )
		addSpriteImage(self.sprite_knife,'survivor/knife/move/survivor-move_knife_19.png' )
		showSprite(self.sprite_knife)

		self.sprite_knife_attack = makeSprite('survivor/knife/move/survivor-move_knife_0.png')
		transformSprite(self.sprite_knife_attack,180,0.3)
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_0.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_1.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_2.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_3.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_4.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_5.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_6.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_7.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_9.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_10.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_11.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_12.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_13.png')
		addSpriteImage(self.sprite_knife_attack, 'survivor/knife/meleeattack/survivor-meleeattack_knife_14.png')
		

	def move_feet(self):
		if keyPressed("a"):

			self.feet_pos_x = self.pos_x - 20
			transformSprite(self.feet,180,0.3)
			
			if clock() > self.timeOfNextFrame:
				self.frame += 1
				if self.frame >19:
					self.frame = 0
				
				changeSpriteImage(self.feet,self.frame)
				
				self.xdir = -1

		elif keyPressed("d"):	
			self.walking = True
			self.feet_pos_x = self.pos_x + 20
			transformSprite(self.feet,0,0.3)
			
			if clock() > self.timeOfNextFrame:
				self.frame += 1
				if self.frame > 19:
					self.frame = 0
				changeSpriteImage(self.feet,self.frame)
				
				self.xdir = 1
		else:
			self.xdir = 0
			self.walking = False

		if keyPressed("w"):
			self.walking = True
			self.feet_pos_y = self.pos_y + 20
			transformSprite(self.feet,-90,0.3)
			
			if clock() > self.timeOfNextFrame:
				self.frame += 1
				if self.frame > 19:
					self.frame = 0
				changeSpriteImage(self.feet,self.frame)
				
				self.timeOfNextFrame = clock() + 15
				self.ydir = 1
		elif keyPressed("s"):
			self.walking = True
			self.pos_y +=self.speed
			transformSprite(self.feet,90,0.3)
			
			if clock() > self.timeOfNextFrame:
				self.frame +=1
				if self.frame > 19:
					self.frame = 0
				changeSpriteImage(self.feet,self.frame)
				
				self.timeOfNextFrame = clock() + 15
				self.ydir = 1
		else:
			self.ydir = 0
			self.walking = False
		
		moveSprite(self.feet, self.pos_x, self.pos_y)

	def move(self):
		if keyPressed("a"):
			self.walking = True
			self.pos_x -= self.speed
			
			transformSprite(self.sprite_knife,180,0.3)
			
			if clock() > self.timeOfNextFrame:
				self.frame += 1
				if self.frame >19:
					self.frame = 0
				changeSpriteImage(self.sprite_knife, self.frame)
				
				self.timeOfNextFrame = clock() + 15
				self.xdir = -1

		elif keyPressed("d"):
			self.walking = True
			self.pos_x += self.speed
			
			transformSprite(self.sprite_knife,0,0.3)
			if clock() > self.timeOfNextFrame:
				self.frame += 1
				if self.frame > 19:
					self.frame = 0
				changeSpriteImage(self.feet,self.frame)
				changeSpriteImage(self.sprite_knife, self.frame)
				self.xdir = 1
		else:
			self.xdir = 0
			self.walking = False

		if keyPressed("w"):
			self.walking = True
			self.pos_y -= self.speed
			
			transformSprite(self.sprite_knife,-90,0.3)
			if clock() > self.timeOfNextFrame:
				self.frame += 1
				if self.frame > 19:
					self.frame = 0
				
				changeSpriteImage(self.sprite_knife, self.frame)
				self.timeOfNextFrame = clock() + 15
		elif keyPressed("s"):
			self.walking = True
			self.pos_y +=self.speed
			
			transformSprite(self.sprite_knife,90,0.3)
			if clock() > self.timeOfNextFrame:
				self.frame +=1
				if self.frame > 19:
					self.frame = 0
				
				changeSpriteImage(self.sprite_knife, self.frame)
				self.timeOfNextFrame = clock() + 15
				self.ydir = 1
		else:
			self.ydir = 0
			self.walking = False
		moveSprite(self.sprite_knife, self.pos_x, self.pos_y)
		


		if keyPressed('space'):
			showSprite(self.sprite_knife_attack)
			if clock() > self.timeOfNextFrame:
				self.frame += 1
				if self.frame >14:
					self.frame = 0

				changeSpriteImage(self.sprite_knife_attack, self.frame)

		else:
			changeSpriteImage(self.sprite_knife_attack, 0)

		if self.walking:
			playSound(self.footstep, 1)
		else:
			stopSound(self.footstep)


	def attack(self):
		pass

	def update(self):
		self.move()
		self.move_feet()


player = Player()
while True:
	player.update()
	updateDisplay()
	tick(30)


endWait()