import random

grid = [[0 for x in range(9)] for y in range(9)]

def valid_num(x, y, num):
    for i in range(9):
        if grid[x][i] == num or grid[i][y] == num:
            return False

    box_x = (x // 3) * 3
    box_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[box_x+i][box_y+j] == num:
                return False

    return True

def solve_puzzle():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for num in range(1, 10):
                    if valid_num(x, y, num):
                        grid[x][y] = num
                        if solve_puzzle():
                            return True
                        grid[x][y] = 0
                return False
    return True

while True:
    for i in range(3):
        nums = random.sample(range(1, 10), 3)
        for j in range(3):
            grid[i*3+j][i*3+j] = nums[j]
    if solve_puzzle():
        break
    grid = [[0 for x in range(9)] for y in range(9)]

print("Sudoku Puzzle:")
for row in grid:
    print("---------------------------")
    print(row)

print("\nSolution:")
solve_puzzle()
for row in grid:
    print("---------------------------")
    print(row)