#import classes modual
from classes import *
from functions import *
from random import randint as random_range
#from time import sleep

##strings
#symbols
wall_sym = "#";
pc_sym = "@"; #pc = playable_character
frame = "";


##Arrays
objects = [];
walls = [];

##Integers
wall_number = 9;

##Boolean
Playing = True;

##Objects
cam = Camera(0,0,"",cols-margin,rows-margin);
for wall in range(wall_number):
	walls.append(Visible(random_range(0,10),random_range(0,10),True,"wall",wall_sym,""));
playable_character = Visible(0,0,True,"player",pc_sym,"green");

#store objects into the objects array
objects.append(cam);
objects.append(playable_character);
objects+=walls;

def main():
	frame_color = "";
	camera_movement = False;
	while Playing:
		update_frame(cam,objects,frame_color);
		key = keyboard();
		if key == "z":
			camera_movement = not camera_movement;
		if camera_movement == False:
			move(objects,playable_character,key);
			cam.target(playable_character)
			#frame_color = "";
			cam.symbol=""
		else:
			move(objects,cam,key);
			#frame_color = "green";
			cam.symbol="⚠️"
		escape(key);

main();
