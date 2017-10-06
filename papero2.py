import curses

def initProg():
	stdscr = curses.initscr()
	# clear screen
	stdscr.clear()
	curses.cbreak()
	# don't write to window
	curses.noecho()
	stdscr.keypad(1)
	
	# current program execution
	modMode(stdscr)
	editMode(stdscr)
	teardown(stdscr)

def modMode(windowObj):
	windowObj.addstr(0, 0, "***Modification Mode***\n", curses.A_STANDOUT)

def editMode(windowObj):
	# write this to screen first
	windowObj.addstr(0, 0, "***Edit Mode***\n", curses.A_STANDOUT)
	windowObj.addstr("\n")
	# gather text and print it until user presses ESC
	c = windowObj.getch()
	while(c != 27):
		# if backspace or delete is pressed, delete previous character
		if(c == 8 or c == 127):
			# get coordinates at cursor
			coords = windowObj.getyx()
			# delete the previous character
			# needs to cover case in which you want to backspace so cursor goes to previous line
			if(coords[1] != 0):
				windowObj.delch(coords[0], coords[1] - 1)
		else:		
			windowObj.addch(c)
		c = windowObj.getch()
	

# restore terminal to original state
def teardown(windowObj):
	curses.nocbreak()
	windowObj.keypad(False)
	curses.echo()
	curses.endwin()


### MAIN ###
initProg()
