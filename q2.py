import random

magic_sum = 15
size = 3

puzzle = [[0 for j in range(size)] for i in range(size)]
numbers = random.sample(range(1, size*size+1), size*size)
for i in range(size):
    for j in range(size):
        puzzle[i][j] = numbers.pop()

print("Random Puzzle:")
for row in puzzle:
    print(row)
print()

while True:
    row_sums = [sum(row) for row in puzzle]
    col_sums = [sum(col) for col in zip(*puzzle)]
    diag_sums = [sum(puzzle[i][i] for i in range(size)), sum(puzzle[i][size-i-1] for i in range(size))]
    if all(val == magic_sum for val in row_sums + col_sums + diag_sums):
        break
    else:
        puzzle = [[0 for j in range(size)] for i in range(size)]
        numbers = random.sample(range(1, size*size+1), size*size)
        for i in range(size):
            for j in range(size):
                puzzle[i][j] = numbers.pop()

print("Solution:")
for row in puzzle:
    print(row)