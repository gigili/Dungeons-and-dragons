from random import randint
import os

os.system("clear")

class Player: 

	name = "John Doe"
	health = 100
	power = 10
	eh = 20
	ep = 2
	score = 0
	move = 1
	slayed = 0
	canAttack = False

	def continueMess(self):
		print "<< Press <<ENTER>> to continue >>"
		raw_input()
		os.system("clear")

	def start(self):
		self.name = raw_input("Enter your name: ")
		os.system("clear")
		print "***********************************************************"
		print "*                                                         *"
		print "*      Welcome, %s to the dragons and dungeons game!     *" % self.name
		print "*                                                         *"
		print "***********************************************************"
		print
		print
		print "Pleas choose your next move"
		print
		print "(1) Start the game"
		print "(2) Exit the game"
		print
		self.move = input("Enter the move number: ")
		if self.move == 1:
			self.start_new_game()	
		elif self.move == 2:
			self.exit_game()
		else:
			os.system("clear")
			print "Invalid option! Try again"
			self.start()

	def start_new_game(self):
		os.system("clear")
		print "You are an explorer looking for a hidden treasure"
		print "hidden deep inside the cave. But what you don't know is"
		print "that the cave is actually a big dungeon filled with dragons"
		print "and suprises. Your goal is to find your way trough the dungeon"
		print "and get the lost grail from the masters trone!"
		
		self.continueMess()		

		print "To see the list of commands type commands()"
		print "To see the list of items in your backpack type bag()"
		print "To see your health and score status type status()"
		print "Good luck and have fun! :)"
		
		self.continueMess()

	def exit_game(self):
		os.system("clear")
		print "R.I.P %s \nYour total score is: %d" % (self.name,self.score)
		print
		self.health = 0

	def eneterCommand(self):
		command = raw_input("> ")
		os.system("clear")

		if command == "commands()":
			self.printCommands()
		elif command == "status()":
			self.status()
		elif command == "left":
			self.goLeft()
		elif command == "right":
			self.goRight()
		elif command == "forward":
			self.goForward()
		elif command == "attack":
			self.attack()
		elif command == "exit()":
			self.exit_game()
		elif command == "skip_fight()":
			if self.health >=15 :
				self.health = self.health - 15
			else:
				self.health = 0

			if self.score >= 20 :
				self.score = self.score - 20
			else:
				self.score = 0
			print "You have skipped the fight and lost 20 points and 15 health"
			print "You are facing a hallway with 3 passages. One on the left, one on the right and one in front of you. Where do you go?"
		else:
			print "Invalid command!"
			print "You are facing a hallway with 3 passages. One on the left, one on the right and one in front of you. Where do you go?"


	def printCommands(self):
		print "List of all available commands"
		print "commands() - Lists all commands"
		#print "bag() - List all the items you have stored"
		print "status() - Prints your current health and score status"
		print "left - Takes you to the dungeon on the left"
		print "right - Takes you to the dungeon on the right"
		print "forward - Takes you to the next hallway"
		print "attack - Attacks the enemy in front of you"
		print "skip_fight() - Skips the current figth but costs you 20 points and 15 health"
		print "exit() - Exits the game \n"

	def goLeft(self):
		print "You have taken the passage on your left side.\nBut there is a dragon waiting for your there. What do you do?"
		self.canAttack = True

	def goRight(self):
		print "You have taken the passage on your right side.\nBut there is a dragon waiting for your there. What do you do?"		
		self.canAttack = True

	def goForward(self):
		print "You have taken the passage in fron of you.\nBut there is a dragon waiting for your there. What do you do?"		
		self.canAttack = True

	def attack(self):
		if self.canAttack :
			self.eh = 20
			self.ep = 2
			while self.eh > 0:
				print "Enemy health: %s" % self.eh
				print "Your health: %s" % self.health
				self.eh = self.eh - self.power
				self.health = self.health - self.ep
				self.score = self.score + 5
				print "You have hit the dragon and coused %d damage" % self.power
				print "Dragon has returnd the strike and coused %d damage to you" % self.ep
				raw_input("Press <<ENTER>>")
				os.system("clear")
			print "You have defeated the enemy and went trough."	
			print "You are facing a hallway with 3 passages. One on the left, one on the right and one in front of you. Where do you go?"
			self.canAttack = False			
		else:
			print "There is nothing to attack!"
			print "You are facing a hallway with 3 passages. One on the left, one on the right and one in front of you. Where do you go?"

	def status(self):
		print "Your health: %d" % self.health
		print "Your score is: %d" % self.score
		print "You are facing a hallway with 3 passages. One on the left, one on the right and one in front of you. Where do you go?"
		self.eneterCommand()		

g = Player()

g.start()

print "You are facing a hallway with 3 passages. One on the left, one on the right and one in front of you. Where do you go?"
while(g.health > 0):
	g.eneterCommand()

if g.health == 0:
	g.exit_game()
