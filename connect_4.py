red = 1
yellow = 2


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
    red_piece = "\033[1;31m●\033[0m"
    yellow_piece = "\033[1;33m●\033[0m"
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
    print("\nPlayer 1 is red\nPlayer 2 is yellow\n")
    grid = make_grid()
    print_grid(grid)
    player = 1

    while True:
        try:
            column_choice = int(
                input(f"Player {player}, choose a column (1 - 7): "))
            print()
            if column_choice < 1 or column_choice > 7:
                print("Pick a column from 1 - 7.")
                continue
        except ValueError:
            print("That's not a number, try again.")
            continue

        if player == 1:
            colour = red
        else:
            colour = yellow

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


play()
