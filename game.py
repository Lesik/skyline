#!/usr/bin/python3

""" The GUI code of the game Skyline by P. Berger and O. Pidgornyy

this is one of two parts of the whole program skyline.
This part is the frontend and generates the gui and uses the backend
to let the user play the game.

"""

import backend
import tkinter as tk
from tkinter import messagebox

__author__ = "6040608: Phillip Berger, 6082200: Oles Pidgornyy"
__email__ = "berger.phillip@hotmail.com," \
			"pidgornyy@informatik.uni-frankfurt.de"

# global variables are defined
game_window = None
game_backend = None

# global lists are defined
labels = []
inputs = []
# possible heights for the skyscrapers
house_heights = 4


def __check_entry_input(char, entry_value):
	"""Checks the input for allowed input."""
	if ((char in '1234') and len(entry_value) <= 1):
		return True
	else:
		return False


def generate_grid():
	""" Generates the graphical background on the basis of grid """
	for r in range(house_heights + 2):
		for c in range(house_heights + 2):
			# The conditions are defined
			top_bottom_tips = (r == 0 or r == house_heights + 1) \
							  and (0 < c < house_heights + 1)
			left_right_tips = (c == 0 or c == house_heights + 1) \
							  and (0 < r < house_heights + 1)
			# generates the hints
			if top_bottom_tips or left_right_tips:
				hints = game_backend.get_hints(r, c)
				l = tk.Label(game_window, text = game_backend.get_hints(r, c))
				labels.append(l)
				l.grid(row=r, column=c)
			# generates the entries
			elif 0 < r < house_heights + 1 and 0 < c < house_heights + 1:
				e = tk.Entry(game_window,
							width=4,
							validate='key',
							validatecommand=cmd_validate)
				inputs.append(e)
				e.grid(row=r, column=c,)


def get_user_entries():
	""" takes the input of the user and saves it as four lists """
	user_entries = []
	user_entries_split = []
	for e in inputs:
		# checks if all fields are filled
		try:
			i = int(e.get())
		except:
			i = None
		if (i is None):
			return None
		user_entries.append(i)
	b = int(len(user_entries) ** 0.5)
	for i in range(b):
		user_entries_split.append(user_entries[i * b:(i * b) + b])
	return user_entries_split



def action_check():
	""" compares the gnerated solution with the solution of the user """
	if game_backend is None:
		messagebox.showerror("Error", "You need to the game first to play.")
	else:
		user_entries = get_user_entries()
		if user_entries is None:
			messagebox.showerror("Error", "You did not fill in all fields.")
		elif (game_backend.compare_fields(get_user_entries())):
			messagebox.showinfo("Winner", "You win. YaY!")
		else:
			messagebox.showinfo("You lose", "Sorry, but you lose you can "
											"try again.")



def action_new_game():
	""" starts a new game """
	global game_backend
	if (get_user_entries() is None or \
			all(x is None for x in get_user_entries()) or
			messagebox.askyesno("Start new game?",
			"Are you sure you want to start a new game?")):
		game_backend = backend.Backend()
		game_backend.start_game()
		generate_grid()


def action_help():
	""" opens a messagebox if the help-button is pressed """
	messagebox.showinfo("Help", "Hello, \n"
								"welcome in the beautiful world of skyline.\n"
								"On all four sides of the field are hints "
								"for you. They tell you how many houses "
								"you can see from their position. The heights "
								"of the houses are represented by the "
								"digits you can fill in. They go from 1 to 4. "
								"Higher houses cover lower ones. After "
								"you think you are done you press check.\n"
								"Have fun.")
def action_about():
	""" opens a messagebox if the about-button is pressed """
	messagebox.showinfo("About", "Hier würden eigentlich unsere "
								 "Hausnummern stehen, aber wir sind nur "
								 "Studenten...")


def action_quit():
	""" stops the program if the quit-button is pressed """
	game_window.quit()

# init game window
game_window = tk.Tk()
cmd_validate = (game_window.register(__check_entry_input), '%S', '%P')

# menubar
menubar = tk.Menu(game_window)
"test"
menu_file = tk.Menu(menubar, tearoff=0)
menu_file.add_command(label="New game", command=action_new_game, \
					  underline=1, accelerator="Ctrl+N")
menu_file.add_command(label="Check", command=action_check, \
					  underline=1, accelerator="Ctrl+H")
menu_file.add_separator()
menu_file.add_command(label="Quit", command=action_quit)

menu_help = tk.Menu(menubar, tearoff=0)
menu_help.add_command(label="Skyline help", command=action_help)
menu_help.add_command(label="About", command=action_about)

menubar.add_cascade(label="File", menu=menu_file)
menubar.add_cascade(label="Help", menu=menu_help)


# global window starts and it's width and height is set
game_window.config(menu=menubar)
game_window.minsize(width=140, height=130)
game_window.mainloop()


##############################################################################
# test cases
# test cases are shown in the form: command, output (change)
# start program, opens wwindow with a menu bar
# press New game, generates new field with hints and clear panels
# press check, opens pop-up for error "You did not fill in all fields."
# type one number in one panel and press check, pop-up opens
# type in every panel a 1 and check, opens pup-up "You lose"
# type the solution and check,