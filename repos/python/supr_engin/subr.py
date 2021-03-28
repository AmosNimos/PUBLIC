import os
from termcolor import colored

size = os.get_terminal_size()
cols = size[0]
rows = size[1]

def colorate(color):
	if color == 1:
		return "yellow"
	elif color == 2:
		return "green"
	elif color == 3:
		return "blue"
	elif color == 4:
		return "cyan"
	elif color == 5:
		return "orange"
	elif color == 6:
		return "gray"
	elif color == 7:
		return "magenta" 
	elif color == 8:
		return "white"
	elif color == 9:
		return "red"
	else:
		return None

# this should be changable depending on the project
sprite_size = 8
#8x8

#sprite exemple (make a softwair to generate these using this engin)
#sprite can be use to display ui on top of the game

##start sprite_001
sprite_001=[]

# sprite size w h:
sprite_001 += [8,8]

#symbol color
sprite_001 += [0,0,0,9,9,0,0,0]
sprite_001 += [0,0,0,3,3,0,0,0]
sprite_001 += [0,0,0,8,8,0,0,0]
sprite_001 += [0,0,9,9,9,9,0,0]
sprite_001 += [0,0,1,9,9,1,0,0]
sprite_001 += [0,0,1,9,9,1,0,0]
sprite_001 += [0,0,0,9,9,0,0,0]
sprite_001 += [0,0,0,3,3,0,0,0]

#on color
sprite_001 += [0,0,0,9,9,0,0,0]
sprite_001 += [0,0,0,1,1,0,0,0]
sprite_001 += [0,0,0,1,1,0,0,0]
sprite_001 += [0,0,9,9,9,9,0,0]
sprite_001 += [0,0,1,9,9,1,0,0]
sprite_001 += [0,0,1,9,9,1,0,0]
sprite_001 += [0,0,0,9,9,0,0,0]
sprite_001 += [0,0,0,3,3,0,0,0]

#symbol
sprite_001 += [" "," "," ","#","#"," "," "," "]
sprite_001 += [" "," "," ","*","*"," "," "," "]
sprite_001 += [" "," "," ","=","="," "," "," "]
sprite_001 += [" "," ","#","#","#","#"," "," "]
sprite_001 += [" "," ","#","#","#","#"," "," "]
sprite_001 += [" "," ","#","#","#","#"," "," "]
sprite_001 += [" "," "," ","#","#"," "," "," "]
sprite_001 += [" "," "," ","#","#"," "," "," "]

# position x y and depth
sprite_001 += [0,0,0]

##end sprite_001

## start sprite_002
sprite_001=[]
sprite_001 += [1,1]
#symbol color
sprite_001 += [8]
#on color
sprite_001 += [0]
#symbol
sprite_001 += ["#"]
# position x y and depth
sprite_001 += [0,0,1]



#make a sprite maker softwair using this engin

col=""
on_color="on_red"
color="cyan"
symbol="#"

#background = colored(" ","blue","on_blue")
background = " "

#print the output line by line
for y in range(rows-1):
	col=""
	for x in range(cols):
		col+=background
	print(col)

#test draw sprite
for y in range(sprite_size):
	line=""
	for x in range(sprite_size):
		sprite_color=sprite_001[y*sprite_size+x]
		color = colorate(sprite_color)
		if color == None:
			line += background
		else:
			line += colored("**",color,"on_"+color)
	print(line)
