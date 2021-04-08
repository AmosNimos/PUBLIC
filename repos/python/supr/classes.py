from termcolor import colored

# default class
class Thing():
	def __init__(self,x:int,y:int,solid:bool):
		self.x=x;
		self.y=y;
		self.solid=solid;

class Visible(Thing):
	def __init__(self,x:int,y:int,solid:bool,name:str,symbol:str,symbol_color:str):
		self.x=x;
		self.y=y;
		self.solid=solid;
		self.name=name;
		if symbol_color == "":
			self.symbol=symbol;
		else :
			self.symbol=colored(symbol,symbol_color);
	

#game engin	class
class Camera():
	def __init__(self,x:int,y:int,symbol:str,view_width:int,view_height:int):
		self.x=x;
		self.y=y;
		self.solid=False;
		self.name="Camera"
		self.symbol=symbol;
		self.view_width=view_width;
		self.view_height=view_height;

	def move(self,target_x:int,target_y:int):
		self.x=target_x;
		self.y=target_y;

	def target(self,target:object):
		self.x=target.x-int(self.view_width/2);
		self.y=target.y-int(self.view_height/2);

	def zoom(self,target_width,target_height):
		#Use negative number to zoom out duh...
		self.view_width=target_width;
		self.view_height=target_height;

	def display(self,objects:list,empty_string:str,spacing:int,margin:int):
		camera_x=self.x;
		camera_y=self.y;
		camera_w=self.x+self.view_width+1;
		camera_h=self.y+self.view_height+1;
		object_in_view=[];
		output="";

		for i in range(int(margin/2)-1):
			output+="\n";

		#scan for object inside view only once
		for index in objects:
			if index.x>=camera_x and index.x<camera_w:
				if index.y>=camera_y and index.y<camera_h:
					object_in_view.append(index);

		#from left to right, top to button
		for y in range(camera_y,camera_h):
			output+=" "*int(margin/2);
			for x in range(camera_x,camera_w):
				if(x==camera_w):
					symbol=empty_string;
				else:
					symbol=empty_string+spacing*" ";
				for index in object_in_view:
					if index.x==x and index.y==y and index.symbol!="":
						symbol=index.symbol+spacing*" ";
				output+=symbol;
			output+="\n";
		return output;
