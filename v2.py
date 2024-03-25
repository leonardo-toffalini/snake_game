import pygame
from random import randint
from time import sleep
import shutil

term_columns, term_rows = shutil.get_terminal_size()

pygame.init()

BUFFER_SIZE = 10
ROWS = term_rows - BUFFER_SIZE - 10
ROWS = ROWS // 2
COLS = term_columns - BUFFER_SIZE - 5
print(ROWS, COLS)


def print_board(board):
    vertical_buffer = "\n" * BUFFER_SIZE
    horizontal_buffer = " " * BUFFER_SIZE

    print(vertical_buffer)
    print(horizontal_buffer + "-" * (COLS + 1) + horizontal_buffer)
    for row in board:
        print(horizontal_buffer + "|" + row + "|" + horizontal_buffer)
    print(horizontal_buffer + "-" * (COLS + 1) + horizontal_buffer)
    print(vertical_buffer)


def update_board(snake, berries):
    board = ["." * COLS] * ROWS
    for i, part in enumerate(snake):
        if i == 0:
            board[part[0]] = (
                board[part[0]][: part[1]] + "@" + board[part[0]][part[1] + 1 :]
            )
        else:
            board[part[0]] = (
                board[part[0]][: part[1]] + "#" + board[part[0]][part[1] + 1 :]
            )
    for berry in berries:
        board[berry[0]] = (
            board[berry[0]][: berry[1]] + "*" + board[berry[0]][berry[1] + 1 :]
        )

    return board


def move_snake(snake, direction, grow):
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    snake.insert(0, new_head)
    if not grow:
        snake.pop()
    return snake


def check_collision(snake, direction):
    head = snake[0]
    next_row, next_col = head[0] + direction[0], head[1] + direction[1]
    if ROWS < next_row or next_row < 0 or COLS < next_col or next_col < 0:
        return True
    if (next_row, next_col) in snake:
        return True
    return False


def check_berries(snake, direction, berries):
    head = snake[0]
    next_row, next_col = head[0] + direction[0], head[1] + direction[1]
    if (new_pos := (next_row, next_col)) in berries:
        new_row, new_col = randint(5, ROWS - 5), randint(5, COLS - 5)
        berries.append((new_row, new_col))
        berries = berries.remove(new_pos)
        return True
    return False


def main():
    start_row, start_col = ROWS // 2, COLS // 2
    snake = [(start_row + i, start_col) for i in range(3)]
    berries = []
    berries = [(5, 5)]
    board = update_board(snake, berries)

    direction_index = 0
    directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

    running = True
    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                direction_index = 0
            elif keys[pygame.K_LEFT]:
                direction_index = 1
            elif keys[pygame.K_DOWN]:
                direction_index = 2
            elif keys[pygame.K_RIGHT]:
                direction_index = 3

        direction = directions[direction_index]
        collided = check_collision(snake, direction)
        if collided:
            print("Game over.")
            running = False
        grow = check_berries(snake, direction, berries)
        snake = move_snake(snake, direction, grow)
        board = update_board(snake, berries)
        print_board(board)
        sleep(0.1)


if __name__ == "__main__":
    main()
