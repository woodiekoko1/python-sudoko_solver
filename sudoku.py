# Sample grid, could be replaced with anything
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

# Checks if each number is viable
def check_solvable(x, y, n):
    # Check columns
    for i in range(9):
        if grid[i][x] == n:
            return False
    for i in range(9):
        if grid[y][i] == n:
            return False

    # Checks boxes, don't judge me I was lazy
    if x < 3 and y < 3:
        for i in range(3):
            for j in range(3):
                if grid[i][j] == n:
                    return False
    if (x > 2 and x < 6) and (y < 3):
        for i in range(3):
            for j in range(3):
                if grid[i][j + 3] == n:
                    return False
    if (x > 5) and (y < 3):
        for i in range(3):
            for j in range(3):
                if grid[i][j + 6] == n:
                    return False
    if x < 3 and (y > 2 and y < 6):
        for i in range(3):
            for j in range(3):
                if grid[i + 3][j] == n:
                    return False
    if (x > 2 and x < 6) and (y > 2 and y < 6):
        for i in range(3):
            for j in range(3):
                if grid[i + 3][j + 3] == n:
                    return False
    if (x > 5) and (y > 2 and y < 6):
        for i in range(3):
            for j in range(3):
                if grid[i + 3][j + 6] == n:
                    return False
    if x < 3 and y > 5:
        for i in range(3):
            for j in range(3):
                if grid[i + 6][j] == n:
                    return False
    if (x > 2 and x < 6) and y > 5:
        for i in range(3):
            for j in range(3):
                if grid[i + 6][j + 3] == n:
                    return False
    if x > 5 and y > 5:
        for i in range(3):
            for j in range(3):
                if grid[i + 6][j + 6] == n:
                    return False
    return True

# Recursive function to solve the grid
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if check_solvable(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(grid)


solve()
