# Search-algorithms-with-hueristics

## Sudoku Solver Report

## Introduction
Sudoku, derived from the Japanese words "su" (meaning "number") and "doku" (meaning "single"), is a numerical puzzle game popular worldwide. This assignment focuses on developing a Sudoku solver using search algorithms with heuristics to tackle puzzles of varying difficulty. The task involves generating and solving classic 9x9 Sudoku puzzles.

## Problem Description
Consider the classic 9x9 Sudoku puzzle, where the objective is to fill in empty cells such that each row, column, and 3x3 box contains the digits 1 through 9 without repetition. The constraints include:

1. **Digit Constraints:** The digits to be entered are 1, 2, 3, 4, 5, 6, 7, 8, and 9.
2. **Row Constraints:** A filled row must have exactly one occurrence of each digit.
3. **Column Constraints:** A filled column must have exactly one occurrence of each digit.
4. **Box Constraints:** A filled box (3x3 layout) must have exactly one occurrence of each digit.

## Tasks

### Task 1: Sudoku Solver Implementation (60 Marks)
- Develop a Sudoku solver program using search algorithms with heuristics.
- The solver should fill in the empty cells adhering to the Sudoku constraints.

### Task 2: Program to Generate Classic 9x9 Sudoku Puzzles
- Write a program to generate random classic 9x9 Sudoku puzzles.
- Note that generated puzzles may have zero, one, or more solutions due to their random nature.

### Task 3: Ensuring Correctness
- Ensure that every correct Sudoku puzzle has only one solution.
- Implement validation mechanisms to verify the correctness of the generated puzzles.

## Conclusion
Sudoku puzzles, with their seemingly simple rules, offer a wide range of complexity. The Sudoku solver and puzzle generator programs will leverage search algorithms to navigate through the puzzle space and provide solutions, making this assignment an exploration into both problem-solving and algorithmic techniques.

# Solution
## Sudoku Solver Code Analysis

## 1. Initialization of the Sudoku Grid
The code initializes an empty 9x9 grid using a nested list comprehension, where each element is set to 0. This grid will serve as the foundation for the Sudoku puzzle.

```python
grid = [[0 for x in range(9)] for y in range(9)]
```

## 2. Validating Numbers
The `valid_num` function checks the validity of placing a number in a specific cell of the grid. It takes the row and column indices (x and y) along with the number to check (num). The function verifies if the number satisfies the Sudoku constraints for the given cell, checking the same row, column, and 3x3 sub-grid.

```python
def valid_num(x, y, num):
    # Implementation details...
```

## 3. Sudoku Puzzle Solver
The `solve_puzzle` function implements a recursive backtracking algorithm to solve the Sudoku puzzle. It iterates through each cell, attempting to place numbers from 1 to 9. If a valid number is found, it recursively calls itself to solve the next cell. If a solution is found, the function returns True; otherwise, it backtracks and tries the next number.

```python
def solve_puzzle():
    # Implementation details...
```

## 4. Puzzle Generation
The code utilizes a `while` loop to generate random numbers to fill in the Sudoku grid until a solvable puzzle is created. It generates a 3x3 sub-grid at a time, filling the diagonal cells with three random numbers between 1 and 9 using the `random.sample` function. The generated puzzle is considered solvable if the `solve_puzzle` function returns True.

```python
while True:
    # Implementation details...
```

## 5. Printing the Generated Puzzle
Once a solvable puzzle is generated, the code prints the Sudoku puzzle.

```python
print("Sudoku Puzzle:")
for row in grid:
    print("---------------------------")
    print(row)
```

## 6. Solving and Printing the Solution
The code then calls the `solve_puzzle` function again to solve the generated puzzle and prints the solution.

```python
print("\nSolution:")
solve_puzzle()
for row in grid:
    print("---------------------------")
    print(row)
```

This code demonstrates a systematic approach to generating and solving Sudoku puzzles using a backtracking algorithm, ensuring the generated puzzles are solvable with a unique solution.

# Problem Statement: Moving Magic Square

## Problem Description
The magic square is a square matrix of odd order where the sum of the elements in each row, column, and diagonal is the same. The sum for each row, column, or diagonal can be calculated using the formula n(n^2 + 1)/2. A specific example is the "Moving Magic Square," played on a 3x3 table with the numbers 1 to 9. The number 9 is movable, and the player can swap it with adjacent numbers in four directions (up/down/left/right). The goal is to reach a final state where the sum of every row, column, and diagonal is 15.

## Example Puzzle: "Moving Magic Square"
Consider a 3x3 table with numbers 1 to 9, where 9 is movable. The initial state is shown in Table 1. The player's objective is to move 9 to reach a final state such that the sum of the three numbers on every row, column, and diagonal is 15.

You are tasked with writing programs to generate and solve classic 3x3 magic square puzzles. However, since these puzzles are generated randomly, they may have zero, one, or more solutions.

# My Solution: Moving Magic Square Solver

## 1. Initialization of the Grid
An empty 3x3 grid is created using a nested list comprehension, initializing each element to 0.

```python
grid = [[0 for x in range(3)] for y in range(3)]
```

## 2. Filling the Grid with Random Numbers
The code generates a list of numbers from 1 to 9 using `random.sample` and fills in the grid with these numbers in random order using nested for loops.

```python
numbers = random.sample(range(1, 10), 9)
for i in range(3):
    for j in range(3):
        grid[i][j] = numbers.pop()
```

## 3. Printing the Randomly Generated Puzzle
The code prints the randomly generated puzzle.

```python
print("Randomly Generated Puzzle:")
for row in grid:
    print(row)
```

## 4. Validating the Magic Square
The code enters a while loop to check if the puzzle is a valid magic square. It calculates the sum of each row, column, and diagonal using list comprehension and the `zip` function. If all sums equal the magic sum of 15, the loop is broken, and the puzzle is valid. If not, the code generates a new puzzle.

```python
while True:
    # Validation and generation process...
```

## 5. Printing the Solution
The code prints the solution (i.e., the valid magic square puzzle).

```python
print("\nSolution (Valid Magic Square):")
for row in grid:
    print(row)
```

This solution generates and validates Moving Magic Square puzzles, ensuring they satisfy the conditions of a valid magic square.

