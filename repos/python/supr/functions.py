import os
import tty
import sys
import termios

##Strings
#These keys can be changed from the game code
up_key = "k";
down_key = "j";
left_key = "h";
right_key = "l";

##Arrays 
size = os.get_terminal_size()

##Integers
spacing = 0; 
margin = 4;
cols = size[0]
rows = size[1]

##Functions
#Clear the screen
def clear():
	os.system('clear')

#Print the objects inside the camera view on the terminal
def update_frame(cam:object,objects:list,frame_color:str):
	#clear frame
	clear();
	#update frame
	frame = cam.display(objects,".",spacing,margin);
	#display frame
	if frame_color == "":
		print(frame);
	else:
		print(colored(frame,frame_color));

def keyboard():
	key = 0
	orig_settings = termios.tcgetattr(sys.stdin) # save default terminal setting
	tty.setcbreak(sys.stdin) # turn off buffering of input and take rawinput
	key=sys.stdin.read(1)[0] # read key pressed
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings) #reset default terminal setting
	return key

def move(objects,target,key):
	collide = None;
	if key == up_key:
		for obj in objects:
			if obj.x == target.x and obj.y == target.y-1 and obj.solid == True and target.solid == True:
				collide = obj;
		if collide == None:
			target.y-=1;
	elif key == down_key:
		for obj in objects:
			if obj.x == target.x and obj.y == target.y+1 and obj.solid == True and target.solid == True:
				collide = obj;
		if collide == None:
			target.y+=1;
	elif key == left_key:
		for obj in objects:
			if obj.x == target.x-1 and obj.y == target.y and obj.solid == True and target.solid == True:
				collide = obj;
		if collide == None:
			target.x-=1;
	elif key == right_key:
		for obj in objects:
			if obj.x == target.x+1 and obj.y == target.y and obj.solid == True and target.solid == True:
				collide = obj;
		if collide == None:
			target.x+=1;
	return collide

def escape(key):
	if key == chr(27) or key == "q":
		exit();