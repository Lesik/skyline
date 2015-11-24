#!/usr/env python3
import backend
import tkinter as tk

class Game():

    game_window = None
    game_backend = None

    grid_labels = None
    grid_entrys = None

    def __init__(self):
        self.self.game_window = tk.Tk()
        self.self.game_backend = backend.Backend()

        self.game_backend.start_game()
        generate_grid()
        self.game_window.mainloop()

    self.grid_labels = []
    self.entries = []
    n = 4
    def get_hint_index(self, r, c):
        if (r == 0 or r == n + 1):
            return c - 1
        else:
            return r - 1

    def generate_grid(self):
        for r in range(n + 2):
            for c in range(n + 2):
                top_bottom_tips = (r == 0 or r == n + 1 ) and (0 < c < n + 1)
                left_right_tips = (c == 0 or c == n + 1) and (0 < r < n + 1)
                if (top_bottom_tips or left_right_tips):
                    hints = self.game_backend.get_hints(r, c)
                    l = tk.Label(self.game_window, text = \
                                 hints[self.get_hint_index(r, c)])
                    self.grid_labels.append(l)
                    l.grid(row=r, column=c)
                elif (0 < r < n + 1 and 0 < c < n + 1):
                    e = tk.Entry(self.game_window, width=2)
                    self.entries.append(e)
                    e.grid(row=r, column=c,)

Game()