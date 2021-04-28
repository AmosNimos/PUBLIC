import sys
calc_in = "0+0"
#take argument
if __name__ == "__main__":
	if len(sys.argv) < 2:
		calc_in = input(":")
	else:
		calc_in = sys.argv[1]
def calc(calc_in):
	if "*" in calc_in:
		calc_in = calc_in.split("*")
		if "." in calc_in[0] or "." in calc_in[1]:
			result = float(calc_in[0])*float(calc_in[1])
		else:
			result = int(calc_in[0])*int(calc_in[1])
	elif "/" in calc_in:
		calc_in = calc_in.split("/")
		if "." in calc_in[0] or "." in calc_in[0]:
			result = float(calc_in[0])/float(calc_in[1])
		else:
			result = int(calc_in[0])/int(calc_in[1])
	elif "-" in calc_in:
		calc_in = calc_in.split("-")
		if "." in calc_in[0] or "." in calc_in[0]:
			result = float(calc_in[0])-float(calc_in[1])
		else:
			result = int(calc_in[0])-int(calc_in[1])
	elif "+" in calc_in:
		calc_in = calc_in.split("+")
		if "." in calc_in[0] or "." in calc_in[0]:
			result = float(calc_in[0])+float(calc_in[1])
		else:
			result = int(calc_in[0])+int(calc_in[1])
	return result
	
answer = round(calc(calc_in), 2)
print(answer)


