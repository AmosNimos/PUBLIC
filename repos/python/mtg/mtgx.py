# Imports
from random import randrange
from random import shuffle
from random import sample
import os

## External dependency
from termcolor import colored, cprint
import namegenerator
from curtsies import Input
import pyttsx3

# Vars
## Rules Variables
deckSize = 60;
initial_health = 20



# Class
## Cards class
### Creature card class
class cardMonster:
	def __init__(self, id, attack, deffence, color, cost, color_cost):
		self.id = id;
		self.attack = attack;
		self.deffence = deffence;
		self.color = color;
		self.type="Creature";
		self.cost = cost;
		self.color_cost = color_cost;
		self.name = namegenerator.gen();
		self.taped = False;

### Land card class
class cardLand:
	def __init__(self, id, color):
		self.id = id;
		self.color = color;
		self.taped = False;
		self.type="creature"
		self.name = "Land";

# Functions
## Return keypress input from curtsies
def get_input():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			return e

# Main game loop
while True:
	print("mtgx")





