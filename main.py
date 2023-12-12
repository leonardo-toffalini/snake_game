import pygame
from time import sleep
import random

pygame.init()

COLS, ROWS = 40, 30
BUFF = 20

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # UP, LEFT, DOWN, RIGHT


def print_grid(grid):
    space = [" "] * BUFF
    for _ in range(BUFF):
        print()
    print("".join(space) + "".join(["-"] * (COLS + 1)) + "".join(space))
    for row in grid:
        print("".join(space) + "|" + row + "|" + "".join(space))
    print("".join(space) + "".join(["-"] * (COLS + 1)) + "".join(space))
    for _ in range(BUFF):
        print()


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


def move_snake(snake, dir_index, ate_berry):
    dir = directions[dir_index]
    head = snake[0]
    new_head = (head[0] + dir[0], head[1] + dir[1])
    snake.insert(0, new_head)
    if not ate_berry:
        snake.pop()


def handle_logic(snake, berries, dir):
    head = snake[0]
    nr, nc = head[0] + dir[0], head[1] + dir[1]
    if nr < 0 or nr > ROWS or nc < 0 or nc > COLS:
        return -1
    elif (nr, nc) in berries:
        berries.remove((nr, nc))
        return 1
    elif (nr, nc) in snake:
        return -1
    else:
        return 0


def generate_berry(berries):
    r, c = random.randint(5, ROWS - 5), random.randint(5, COLS - 5)
    berries.append((r, c))


def main():
    dir_idx = 0
    start = (ROWS // 2, COLS // 2)
    snake = [(start[0], start[1]), (start[0] + 1, start[1]), (start[0] + 2, start[1])]
    berries = [(1, 1)]

    while True:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                dir_idx = 0
            elif keys[pygame.K_LEFT]:
                dir_idx = 1
            elif keys[pygame.K_DOWN]:
                dir_idx = 2
            elif keys[pygame.K_RIGHT]:
                dir_idx = 3

        out = handle_logic(snake, berries, directions[dir_idx])
        if out == -1:
            print("Game over.")
            exit(0)
        ate_berry = True if out == 1 else False
        if ate_berry:
            generate_berry(berries)
        move_snake(snake, dir_idx, ate_berry)
        grid = update_grid(snake, berries)
        print_grid(grid)
        sleep(0.1)


if __name__ == "__main__":
    main()
