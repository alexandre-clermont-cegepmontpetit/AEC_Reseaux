import tkinter as tk
from tkinter import messagebox
from collections import deque
import copy

COLORS = ["yellow", "red", "blue"]

def is_winning(grid):
    # Winning if each row OR each column contains the same color per line
    if all(len(set(row)) == 1 for row in grid):
        return True
    if all(len({grid[0][c], grid[1][c], grid[2][c]}) == 1 for c in range(3)):
        return True
    return False

def move(grid, direction):
    new_grid = copy.deepcopy(grid)
    if direction == 'up':
        for col in range(3):
            new_grid[0][col], new_grid[1][col], new_grid[2][col] = \
                new_grid[1][col], new_grid[2][col], new_grid[0][col]
    elif direction == 'down':
        for col in range(3):
            new_grid[2][col], new_grid[1][col], new_grid[0][col] = \
                new_grid[1][col], new_grid[0][col], new_grid[2][col]
    elif direction == 'left':
        for row in range(3):
            new_grid[row][0], new_grid[row][1], new_grid[row][2] = \
                new_grid[row][1], new_grid[row][2], new_grid[row][0]
    elif direction == 'right':
        for row in range(3):
            new_grid[row][2], new_grid[row][1], new_grid[row][0] = \
                new_grid[row][1], new_grid[row][0], new_grid[row][2]
    return new_grid

def grid_to_tuple(grid):
    return tuple(tuple(row) for row in grid)

def solve_puzzle(start_grid):
    visited = set()
    queue = deque()
    queue.append((start_grid, []))

    while queue:
        grid, path = queue.popleft()
        grid_tuple = grid_to_tuple(grid)

        if grid_tuple in visited:
            continue
        visited.add(grid_tuple)

        if is_winning(grid):
            return path

        for direction in ['up', 'down', 'left', 'right']:
            new_grid = move(grid, direction)
            new_path = path + [direction]
            queue.append((new_grid, new_path))
    return None

class PuzzleGUI:
    def __init__(self, master, start_grid):
        self.master = master
        self.grid = start_grid
        self.labels = [[None for _ in range(3)] for _ in range(3)]
        self.frame = tk.Frame(master)
        self.frame.pack()

        for i in range(3):
            for j in range(3):
                label = tk.Label(self.frame, width=10, height=5, bg=self.grid[i][j], relief='ridge', borderwidth=2)
                label.grid(row=i, column=j)
                self.labels[i][j] = label

        self.solve_button = tk.Button(master, text="Solve Puzzle", command=self.solve_and_animate)
        self.solve_button.pack(pady=10)

        self.solution_steps = []
        self.step_index = 0
        self.next_button = tk.Button(master, text="Next Step", command=self.next_step)
        self.next_button.pack(pady=5)
        self.next_button.config(state="disabled")

    def update_display(self):
        for i in range(3):
            for j in range(3):
                self.labels[i][j].config(bg=self.grid[i][j])

    def solve_and_animate(self):
        solution = solve_puzzle(self.grid)
        if not solution:
            messagebox.showinfo("Result", "No solution found.")
            return
        self.solution_steps = solution
        self.step_index = 0
        self.next_button.config(state="normal")
        messagebox.showinfo("Result", f"Solution found with {len(solution)} steps. Click 'Next Step' to proceed.")

    def next_step(self):
        if self.step_index >= len(self.solution_steps):
            messagebox.showinfo("Done", "Puzzle solved!")
            self.next_button.config(state="disabled")
            return
        direction = self.solution_steps[self.step_index]
        self.grid = move(self.grid, direction)
        self.update_display()
        self.step_index += 1

if __name__ == "__main__":
    start_grid = [
        ['red', 'blue', 'yellow'],
        ['yellow', 'red', 'blue'],
        ['yellow', 'red', 'blue']
    ]

    root = tk.Tk()
    root.title("3x3 Color Puzzle")
    app = PuzzleGUI(root, start_grid)
    root.mainloop()
