import sys
from tkinter.font import BOLD
import tkinter as tk
import os

grid = []
ent = []
i = 0


def main():
    sudoku()


def exits():
    os.execl(sys.executable, sys.executable, *sys.argv)


def sudoku():
    root = tk.Tk()

    root.configure(bg="black")

    for i in range(11):
        ent.append([])
        for j in range(9):

            # frame look
            frame = tk.Frame(
                master=root,
                relief=tk.RIDGE,
                borderwidth=3
            )

            # frame griding
            if j % 3 == 0 and i != 4 and i != 7:
                frame.grid(row=i, column=j, padx=(7, 1), pady=1)
            elif i == 4 or i == 7:
                if j % 3 != 0 and j != 8:
                    frame.grid(row=i, column=j, pady=(7, 1))
                elif j == 8:
                    frame.grid(row=i, column=j, padx=(1, 7), pady=(7, 1))
                else:
                    frame.grid(row=i, column=j, padx=(7, 1), pady=(7, 1))
            elif j == 8:
                frame.grid(row=i, column=j, padx=(1, 7), pady=1)
            else:
                frame.grid(row=i, column=j, pady=1, padx=1)

            # entry packing
            if i == 0 or i == 10:
                blank = tk.Entry(master=frame, width=1)
                blank.pack()
            else:
                ent[i - 1].append(tk.Entry(master=frame, width=2, font=("Helvetica", 30), justify='center'))
                ent[i - 1][j].pack()

    # title
    lbl = tk.Label(text="SUDOKU SOLVER", height=2, width=35, bg="black", fg="white", font=("Helvetica", 18, BOLD))
    lbl.grid(row=0, column=0, columnspan=9)

    # button_solve
    btn_solve = tk.Button(text="Solve", height=1, width=36, cursor="dot", bg="#fc6358", font=("Arial", 15),
                          activebackground="green", pady=10, bd=5, command=tmp)
    btn_solve.grid(row=10, column=0, columnspan=7)

    # button_reset
    btn_reset = tk.Button(text="Reset", height=1, width=9, cursor="dot", pady=9, bd=5, font=("Arial", 15),
                          command=exits)
    btn_reset.grid(row=10, column=7, columnspan=2)

    root.mainloop()


def tmp():
    for y in range(9):
        grid.append([])
        for x in range(9):
            if ent[y][x].get() == "":
                z = 0
            elif "0" <= ent[y][x].get() <= "9":
                z = int(ent[y][x].get())
            else:
                exits()
            grid[y].append(z)
    for y in range(9):
        for x in grid[y]:
            if x < 0 or x > 9:
                os.execl(sys.executable, sys.executable, *sys.argv)
    solve()


def solve():
    global grid
    global i
    if i == 0:
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1, 10):
                        if possible(y, x, n):
                            grid[y][x] = n
                            solve()
                            grid[y][x] = 0
                    return True
        display()
        i += 1


def possible(y, x, n):
    global grid
    for i in range(9):
        if grid[y][i] == n or grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[i + y0][j + x0] == n:
                return False
    return True


def display():
    global grid
    for y in range(9):
        for x in range(9):
            if ent[y][x].get() == "":
                ent[y][x].insert(0, str(grid[y][x]))


if __name__ == "__main__":
    main()
