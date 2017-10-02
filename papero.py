# Python will be instantiated from the terminal (launcher)

DEBUG = True

import sys
import random

import tty
import termios

orig_tty_settings = termios.tcgetattr(sys.stdin)

isRunning = True
isEditing = False


argv = sys.argv
argc = len(argv)

cmd_in = "" 	# delcare
file_string = ""

# print(argv)
# print(argc)


def suicide():
	# Stop intercepting user input
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings) 
	# and Exit
	quit(0)

def getCommand():
	l_cmd_in = '' 	# reset
	c = sys.stdin.read(1)[0]
	if(DEBUG):
		print(ord(c))
	while(c!= chr(13) and c!= chr(27)): 	# while not ENTER, ESC
		if(c == chr(3)): 						# if ^C
			suicide()
		if(c == chr(127)): 						# if BACKSPACE
			l_cmd_in = l_cmd_in[:-1]
		else:
			l_cmd_in += c
			sys.stdout.write(c)
		#print(c), print (ord(c))
		c = sys.stdin.read(1)[0]
	#print(l_cmd_in)
	return l_cmd_in

def drawDraft():
	sys.stdout.write(file_string)
	sys.stdout.flush()
	


### MAIN ###
orig_settings = termios.tcgetattr(sys.stdin)
tty.setraw(sys.stdin)
c = 0

#text_in = str() 		# size pow(2, 7)

# generate random draft for testing
for i in range(30):
	file_string += chr(random.randint(65, 75))

while(isRunning):
	drawDraft()
	print('\n\rgetting command:'),
	cmd_in = getCommand()
	print('\n\rcommand received:'), print(cmd_in)
	if(cmd_in == "draw"):
		drawDraft()
	if(cmd_in == "exit" or cmd_in == "quit"):
		suicide()
	if(cmd_in == "erase"):
		file_string = ""
	if(cmd_in == "edit"):
		isEditing = True
	
	print('Edit head')
	while(isEditing): 		
		c = sys.stdin.read(1)[0]
		
		if (c == chr(27)): 	# if ESC
			isEditing = False
			break
		
		if (c == chr(13)): 	# if ENTER
			file_string += "\n\r"
			drawDraft()
		if (c == chr(127)):
			file_string = file_string[:-1]
		else:
			file_string += c

	print('Edit tail; loop\n')
