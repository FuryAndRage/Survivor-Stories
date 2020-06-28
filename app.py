from pygame_functions import *
setAutoUpdate(False)
screenSize(800, 800)
class Player():
	def __init__(self):
		self.pos_x = 400
		self.pos_y = 400
		self.speed = 3
		self.health = 100
		self.xdir = 0
		self.ydir = 0
		self.frame = 0
		self.timeOfNextFrame = clock()
		self.current_weapon = 0
		self.sprite = makeSprite('survivor/knife/move/survivor-move_knife_0.png' )
		transformSprite(self.sprite,180,0.3)
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_1.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_2.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_3.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_4.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_5.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_6.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_7.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_8.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_9.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_10.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_11.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_12.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_13.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_14.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_15.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_16.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_17.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_18.png' )
		addSpriteImage(self.sprite,'survivor/knife/move/survivor-move_knife_19.png' )
		showSprite(self.sprite)

		self.footstep = makeSound('sounds/foot.ogg')

	def move(self):
		if keyPressed("left"):
			self.pos_x -= self.speed
			
			transformSprite(self.sprite,180,0.3)
			if clock() > self.timeOfNextFrame:
				self.frame += 1
				if self.frame >19:
					self.frame = 0
				changeSpriteImage(self.sprite, self.frame)
				self.timeOfNextFrame = clock() + 15
				self.xdir = -1
		elif keyPressed("right"):
			self.pos_x += self.speed
			
			transformSprite(self.sprite,0,0.3)
			if clock() > self.timeOfNextFrame:
				self.frame += 1
				if self.frame > 19:
					self.frame = 0
				changeSpriteImage(self.sprite, self.frame)
				self.xdir = 1
		else:
			self.xdir = 0


		if keyPressed("up"):
			self.pos_y -= self.speed
			
			transformSprite(self.sprite,-90,0.3)
			if clock() > self.timeOfNextFrame:
				self.frame += 1
				if self.frame > 19:
					self.frame = 0
				changeSpriteImage(self.sprite, self.frame)
				self.timeOfNextFrame = clock() + 15
				self.ydir = -1
		elif keyPressed("down"):
			self.pos_y +=self.speed
			
			transformSprite(self.sprite,90,0.3)
			if clock() > self.timeOfNextFrame:
				self.frame +=1
				if self.frame > 19:
					self.frame = 0
				changeSpriteImage(self.sprite, self.frame)
				self.timeOfNextFrame = clock() + 15
				self.ydir = 1
		else:
			self.ydir = 0

		moveSprite(self.sprite, self.pos_x, self.pos_y)

	def update(self):
		self.move()


player = Player()
while True:
	player.update()
	updateDisplay()
	tick(30)


endWait()