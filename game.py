
import backend
import tkinter as tk

game_window = tk.Tk()
game_backend = backend.Backend()

labels = []
inputs = []
n = 4

def get_hint_index(r, c):
    if (r == 0 or r == n + 1):
        return c - 1
    else:
        return r - 1

def generate_grid():
    for r in range(n + 2):
        for c in range(n + 2):
            top_bottom_tips = (r == 0 or r == n + 1 ) and (0 < c < n + 1)
            left_right_tips = (c == 0 or c == n + 1) and (0 < r < n + 1)
            if (top_bottom_tips or left_right_tips):
                hints = game_backend.get_hints(r, c)
                l = tk.Label(game_window, text = \
                             hints[get_hint_index(r, c)])
                labels.append(l)
                l.grid(row=r, column=c)
            elif (0 < r < n + 1 and 0 < c < n + 1):
                e = tk.Entry(game_window, width = 2)
                inputs.append(e)
                e.grid(row=r, column=c,)

game_backend.start_game()            
generate_grid()
game_window.mainloop()
