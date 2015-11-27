#!/usr/bin/python3

__author__ = "6040608: Phillip Berger, 6082200: Oles Pidgornyy"

import backend
import tkinter as tk
from tkinter import messagebox

game_window = None
game_backend = None

labels = []
inputs = []
n = 4


def __get_hint_index(r, c):
	if (r == 0 or r == n + 1):
		return c - 1
	else:
		return r - 1


def __check_entry_input(char, entry_value):
	if ((char in '1234') and len(entry_value) <= 1):
		return True
	else:
		return False


def generate_grid():
	for r in range(n + 2):
		for c in range(n + 2):
			top_bottom_tips = (r == 0 or r == n + 1) and (0 < c < n + 1)
			left_right_tips = (c == 0 or c == n + 1) and (0 < r < n + 1)
			if (top_bottom_tips or left_right_tips):
				hints = game_backend.get_hints(r, c)
				l = tk.Label(game_window, text = game_backend.get_hints(r, c))
				labels.append(l)
				l.grid(row=r, column=c)
			elif (0 < r < n + 1 and 0 < c < n + 1):
				e = tk.Entry(game_window,
							width=2,
							validate='key',
							validatecommand=cmd_validate)
				inputs.append(e)
				e.grid(row=r, column=c,)


def get_userentries():
	userentries = []
	userentries_split = []
	for e in inputs:
		try:
			i = int(e.get())
		except:
			i = None
		if (i is None):
			return None
		userentries.append(i)
	b = int(len(userentries) ** 0.5)
	for i in range(b):
		userentries_split.append(userentries[i * b:(i * b) + b])
	return userentries_split



def action_check():
	user_entries = get_userentries()
	if user_entries is None:
		messagebox.showinfo("Error", "You did not fill in all fields.")
	elif (game_backend.compare_fields(get_userentries())):
		messagebox.showinfo("Winner", "You win. YaY!")
	else:
		messagebox.showinfo("Loser", "You are a Loser.")


def action_new_game():
	global game_backend
	if (all(x == None for x in get_userentries()) or
			messagebox.askyesno("Start new game?",
			"Are you sure you want to start a new game?")):
		game_backend = backend.Backend()
		game_backend.start_game()
		generate_grid()


def action_help():
	messagebox.showinfo("Help", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")

def action_about():
	messagebox._show("About", "Yay")


def action_quit():
	game_window.quit()

# init game window
game_window = tk.Tk()
cmd_validate = (game_window.register(__check_entry_input), '%S', '%P')

# menubar
menubar = tk.Menu(game_window)
"test"
menu_file = tk.Menu(menubar, tearoff=0)
menu_file.add_command(label="New game", command=action_new_game,\
					  underline=1, accelerator="Ctrl+N")
menu_file.add_command(label="Check", command=action_check,\
					  underline=1, accelerator="Ctrl+H")
menu_file.add_separator()
menu_file.add_command(label="Quit", command=action_quit)

menu_help = tk.Menu(menubar, tearoff=0)
menu_help.add_command(label="Skyline help", command=action_help)
menu_help.add_command(label="About", command=action_about)

menubar.add_cascade(label="File", menu=menu_file)
menubar.add_cascade(label="Help", menu=menu_help)


# global window blabla
game_window.config(menu=menubar)
game_window.minsize(width=200, height=200)
game_window.mainloop()
