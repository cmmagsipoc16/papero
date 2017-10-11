import curses
import curses.textpad

def initProg():
	stdscr = curses.initscr()
	# clear screen
	stdscr.clear()
	curses.cbreak()
	# don't write to window
	curses.noecho()
	stdscr.keypad(1)
	
	# create window for showing mode
	# params: nlines, ncols
	modeStat = curses.newwin(2, 30, 0, 0)

	# create window for textpad
	begin_x = 0
	begin_y = 3
	numLines = 150
	numCols = 200
	# params: nlines, ncols, top left coord of y, top left coord of x	
	editWin = curses.newwin(numLines, numCols, begin_y, begin_x)

	# now create textbox that we will be writing to
	editBox = curses.textpad.Textbox(editWin)

	# create one last window for modMode
	# it will show commands that the user types, like save, edit, etc

	# current program execution
	#modMode(stdscr)
	editMode(modeStat, editBox)
	teardown(stdscr)

def modMode(windowObj):
	windowObj.addstr(0, 0, "***Modification Mode***\n", curses.A_STANDOUT)

def editMode(status, windowObj):
	# signifies editing mode
	status.addstr(0, 0, "***Editing Mode***", curses.A_STANDOUT)
	status.refresh()
	# edit returns a string of all of the window's contents
	fileText = windowObj.edit()

	
# restore terminal to original state
def teardown(windowObj):
	curses.nocbreak()
	windowObj.keypad(False)
	curses.echo()
	curses.endwin()


### MAIN ###
initProg()
