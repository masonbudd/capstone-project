import random
import time

red = 1
yellow = 2
red_piece = "\033[1;31m●\033[0m"
yellow_piece = "\033[1;33m●\033[0m"


def make_grid():
    grid = []
    for i in range(6):
        row = []
        for j in range(7):
            row.append(0)
        grid.append(row)
    return grid


def print_grid(grid):
    print("1 2 3 4 5 6 7")
    symbols = {0: "_", 1: red_piece, 2: yellow_piece}
    for row in grid:
        for num in row:
            print(symbols[num], end=" ")
        print()
    print()


def drop_piece(grid, col, colour):
    for i in range(5, -1, -1):
        if grid[i][col-1] == 0:
            grid[i][col-1] = colour
            return grid
    return "Full"


def computer_move(grid, colour, opponent_colour):
    # Priority 1: Can the computer win on this turn? If so return that column.
    for col in range(1, 8):
        test_grid = [row[:] for row in grid]
        drop_piece(test_grid, col, colour)
        if check_win(test_grid, colour):
            return col

    # Priority 2: Is the opponent about to win? If so return the column that will block.
    for col in range(1, 8):
        test_grid = [row[:] for row in grid]
        drop_piece(test_grid, col, opponent_colour)
        if check_win(test_grid, opponent_colour):
            return col

    # Priority 3: Pick a random column that is'nt full, with preference to the inner columns.
    valid_columns = []
    for col in range(1, 8):
        if grid[0][col-1] == 0:
            valid_columns.append(col)

    weighted = []
    weights = {1: 1, 2: 2, 3: 3, 4: 4, 5: 3, 6: 2, 7: 1}
    for col in valid_columns:
        weighted += [col] * weights[col]

    return random.choice(weighted)


def check_win(grid, colour):
    # Check horizontal win
    for i in range(6):
        for j in range(4):
            if grid[i][j] == colour and grid[i][j+1] == colour and grid[i][j+2] == colour and grid[i][j+3] == colour:
                return True

    # Check vertical win
    for i in range(3):
        for j in range(7):
            if grid[i][j] == colour and grid[i+1][j] == colour and grid[i+2][j] == colour and grid[i+3][j] == colour:
                return True

    # Check horizontal down right win
    for i in range(3):
        for j in range(4):
            if grid[i][j] == colour and grid[i+1][j+1] == colour and grid[i+2][j+2] == colour and grid[i+3][j+3] == colour:
                return True

    # Check horizontal down left win
    for i in range(3):
        for j in range(3, 7):
            if grid[i][j] == colour and grid[i+1][j-1] == colour and grid[i+2][j-2] == colour and grid[i+3][j-3] == colour:
                return True
    return False


def check_draw(grid):
    empty_slots = 0
    for num in grid[0]:
        if num == 0:
            empty_slots += 1
    if empty_slots == 0:
        return True
    return False


def play():
    print("\nWelcome to Connect 4!!")

    while True:
        try:
            mode = int(input("Choose mode: 1-player or 2-player? (1/2): "))
            if mode in [1, 2]:
                break
            print("Please enter 1 or 2.")
        except ValueError:
            print("Please enter 1 or 2.")

    while True:
        print(
            f"\nPlayer 1 is red ({red_piece})\nPlayer 2 is yellow ({yellow_piece})\n")
        grid = make_grid()
        print_grid(grid)
        player = 1

        while True:
            if player == 1:
                colour = red
                piece = red_piece
            else:
                colour = yellow
                piece = yellow_piece

            if mode == 1 and player == 2:
                time.sleep(0.9)
                column_choice = computer_move(grid, yellow, red)
                print(f"Computer chose column {column_choice}.\n")

            else:
                try:
                    column_choice = int(
                        input(f"Player {player} ({piece}), choose a column (1 - 7): "))
                    print()

                    if column_choice < 1 or column_choice > 7:
                        print("Pick a column from 1 - 7.")
                        continue
                except ValueError:
                    print("That's not a number, try again.")
                    continue

            result = drop_piece(grid, column_choice, colour)
            if result == "Full":
                print("Column is full.")
                continue

            print_grid(grid)

            if check_win(grid, colour):
                print(f"Player {player} wins!")
                break

            if check_draw(grid):
                print("Draw! No-one wins")
                break

            if player == 1:
                player = 2
            else:
                player = 1

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break


play()
