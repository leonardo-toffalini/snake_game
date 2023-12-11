import pygame

pygame.init()

COLS, ROWS = 10, 15

grid = ["".join(["." for _ in range(COLS)]) for _ in range(ROWS)]


def print_grid(grid):
    for row in grid:
        print(row)


snake = [(ROWS // 2, COLS // 2)]
berries = [(1, 1)]


def update_grid(snake, berries):
    grid = ["".join(["." for _ in range(COLS)]) for _ in range(ROWS)]
    head = snake[0]
    grid[head[0]] = grid[head[0]][: head[1]] + "@" + grid[head[0]][head[1] + 1 :]
    for body in snake[1:]:
        grid[body[0]] = grid[body[0]][: body[1]] + "#" + grid[body[0]][body[1] + 1 :]
    for berry in berries:
        grid[berry[0]] = (
            grid[berry[0]][: berry[1]] + "*" + grid[berry[0]][berry[1] + 1 :]
        )
    return grid


def main():
    while True:
        grid = update_grid(snake, berries)
        print_grid(grid)


if __name__ == "__main__":
    main()
