#!/usr/bin/python3

__author__ = "6040608: Phillip Berger, 6082200: Oles Pidgornyy"

import backend
import tkinter as tk
from tkinter import messagebox

game_window = None
game_backend = None

labels = []
inputs = []
userentries = []
n = 4


def __get_hint_index(r, c):
	if (r == 0 or r == n + 1):
		return c - 1
	else:
		return r - 1


def __check_entry_input(char, entry_value):
	if (char in '1234'):
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
				l = tk.Label(game_window, text = \
							 hints[__get_hint_index(r, c)])
				labels.append(l)
				l.grid(row=r, column=c)
			elif (0 < r < n + 1 and 0 < c < n + 1):
				e = tk.Entry(game_window,
							 width=2,
							 validate='key',
							 validatecommand=__check_entry_input)
				inputs.append(e)
				e.grid(row=r, column=c,)


def echo_hey():
	print("hey")


def get_userentries():
	for e in inputs:
		i = e.get()
		userentries.append(i)
	print(userentries)
	return userentries


def action_check():
	pass


def action_new_game():
	global game_backend
	if (all(x == "" for x in get_userentries())):
		start_game = True
	else:
		start_game = messagebox.askyesno("Start new game?",
			"Are you sure you want to start a new game?")

	if (start_game):
		game_backend = backend.Backend()
		game_backend.start_game()
		generate_grid()


def action_help():
	messagebox.showinfo("Help", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")


def action_quit():
	game_window.quit()

# init game window
game_window = tk.Tk()


# menubar
menubar = tk.Menu(game_window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New game", command=action_new_game)
filemenu.add_command(label="Check", command=action_check)
filemenu.add_command(label="Help", command=action_help)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=action_quit)
menubar.add_cascade(label="File", menu=filemenu)


# global window blabla
game_window.config(menu=menubar)
game_window.minsize(width=400, height=400)
game_window.mainloop()
