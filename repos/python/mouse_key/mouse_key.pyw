#!/usr/bin/env python3

##Description:
#move the mouse with the keyboard
#Default key are (hjkl;')

#bug the key are still typed so not idea to move the mouse above text document...
#if you have a solution please submit it.

#also "u" and "i" would probably be more suitable to be used as the right and left mouse button


from curtsies import Input
from pynput import keyboard
import mouse
import pyautogui

current_key = ""
last_key = 0
mouse_spd=1
initial_spd = 2
Press_Keyboard = keyboard.Controller()

move_down = keyboard.KeyCode(char='j')
move_up = keyboard.KeyCode(char='k')
move_left = keyboard.KeyCode(char='h')
move_right = keyboard.KeyCode(char='l')
click_left = keyboard.KeyCode(char="'")
click_right = keyboard.KeyCode(char=";")
escape_key = keyboard.KeyCode(char='q')

code_down = keyboard.KeyCode(char='j')
code_up = keyboard.KeyCode(char='k')
code_left = keyboard.KeyCode(char='h')
code_right = keyboard.KeyCode(char='l')

def on_press(key):
		global current_key, mouse_spd, last_key
		current_key = key
		mouse_spd, last_key = main(mouse_spd,last_key)
		return current_key, mouse_spd, last_key

def on_release(key):
	pass

def on_listener():
	with keyboard.Listener(on_press=on_press,on_release=on_release) as event:
		event.join()

def execute(key):
	print("key:"+str(key))

def setmouse(x,y,d):
	pos = pyautogui.position()
	pyautogui.moveTo(pos[0]+x, pos[1]+y, d)
            
def getmouse():
	pos = pyautogui.position()
	mouse_x=pos[0]
	mouse_y=pos[1]
	return mouse_x,mouse_y
	
def getkey():
	with Input(keynames='curses') as input_generator:
		for e in input_generator:
			return e

def main(mouse_spd,last_key):
	key=current_key
	if key != escape_key:
		print(str(key))
		mouse_y=0
		mouse_x=0
		if key == move_down:
			if last_key != 1:
				mouse_spd=initial_spd
			else:
				mouse_spd*=2
			last_key = 1
			mouse_y+=mouse_spd
		if key == move_up:
			if last_key != 2:
				mouse_spd=initial_spd
			else:
				mouse_spd*=2
			last_key = 2
			mouse_y-=mouse_spd
		if key == move_left:
			if last_key != 3:
				mouse_spd=initial_spd
			else:
				mouse_spd*=2
			last_key = 3
			mouse_x-=mouse_spd
		if key == move_right:
			if last_key != 4:
				mouse_spd=initial_spd
			else:
				mouse_spd*=2
			last_key = 4
			mouse_x+=mouse_spd
		if key == click_left:
			pyautogui.click(button='right')
			mouse_spd=initial_spd
			last_key=0
		if key == click_right:
			pyautogui.click()
			mouse_spd=initial_spd
			last_key=0
		if key == "u":
			mouse_spd=initial_spd;
		if key == "i":
			mouse_spd+=1;
		if key == "o":
			mouse_spd-=1;
		if key == escape_key:
			print("exit")
			exit()
		if key != "":
			mouse.move(mouse_x,mouse_y, absolute=False, duration=0.1)
			#setmouse(mouse_x,mouse_y,0.2)
			print(mouse_spd)
	else:
		print("exit")
		exit()
	return mouse_spd, last_key

def main_loop():
	mouse_spd=1
	key=""
	last_key=0
	while key != "q":
		key = getkey()
		mouse_y=0
		mouse_x=0
		if key == move_down:
			if last_key != 1:
				mouse_spd=1
			else:
				mouse_spd*=2
			last_key = 1
			mouse_y+=mouse_spd
		if key == move_up:
			if last_key != 2:
				mouse_spd=1
			else:
				mouse_spd*=2
			last_key = 2
			mouse_y-=mouse_spd
		if key == move_left:
			if last_key != 3:
				mouse_spd=1
			else:
				mouse_spd*=2
			last_key = 3
			mouse_x-=mouse_spd
		if key == move_right:
			if last_key != 4:
				mouse_spd=1
			else:
				mouse_spd*=2
			last_key = 4
			mouse_x+=mouse_spd
		if key == click_left:
			pyautogui.click(button='right')
			mouse_spd=1
			last_key=0
		if key == click_right:
			pyautogui.click()
			mouse_spd=1
			last_key=0
		if key == "u":
			mouse_spd=1;
		if key == "i":
			mouse_spd+=1;
		if key == "o":
			mouse_spd-=1;
		if key != "":
			mouse.move(mouse_x,mouse_y, absolute=False, duration=0.1)
			print(mouse_spd)
	else:
		print("end")
		#Press_Keyboard.release(keyboard.Key.ctrl)
		exit()

print("start")
#Press_Keyboard.press(keyboard.Key.ctrl)
on_listener()
print("end")
#Press_Keyboard.release(keyboard.Key.ctrl)
exit()