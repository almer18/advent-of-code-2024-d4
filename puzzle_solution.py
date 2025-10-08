with open("puzzle_input.txt") as f:
    grid = [line.strip() for line in f]

rows = len(grid)
cols = len(grid[0])
count = 0
word = "XMAS"
word_len = len(word)
directions = [
    (1, 0),   # down
    (-1, 0),  # up
    (0, 1),   # right
    (0, -1),  # left
    (1, 1),   # down-right diagonal
    (1, -1),  # down-left diagonal
    (-1, 1),  # up-right diagonal
    (-1, -1)  # up-left diagonal
]

def in_bounds(x, y):
    return 0 <= x < rows and 0 <= y < cols

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == word[0]:
            for dx, dy in directions:
                found = True
                for k in range(word_len):
                    nx, ny = i + dx*k, j + dy*k
                    if not in_bounds(nx, ny) or grid[nx][ny] != word[k]:
                        found = False
                        break
                if found:
                    count += 1
print("XMAS Count = ", count)