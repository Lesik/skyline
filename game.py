
import backend
import tkinter as tk

master = tk.Tk()

labels = []
inputs = []
n = 10

for r in range(n + 2):
    for c in range(n + 2):
        top_bottom_tips = (r == 0 or r == n +1 ) and (0 < c < n + 1)
        left_right_tips = (c == 0 or c == n + 1) and (0 < r < n + 1)
        if (top_bottom_tips or left_right_tips):
            l = tk.Label(master, text = str(r) + str(c))
            labels.append(l)
            l.grid(row = r, column = c)
        elif (0 < r < n + 1 and 0 < c < n + 1):
            e = tk.Entry(master)
            inputs.append(e)
            e.grid(row = r, column = c)
            

master.mainloop( )
