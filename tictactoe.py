import random


print("Welcome to TicTacToe")
print("------------------------------------------------")

possible_numbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3


def print_game_board():
    for x in range(rows):
        print("+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], end=" |")
        print("\n+---+---+---+")


def modify_array(num, turn):
    num -= 1
    if num == 0:
        gameBoard[0][0] = turn
    elif num == 1:
        gameBoard[0][1] = turn
    elif num == 2:
        gameBoard[0][2] = turn
    elif num == 3:
        gameBoard[1][0] = turn
    elif num == 4:
        gameBoard[1][1] = turn
    elif num == 5:
        gameBoard[1][2] = turn
    elif num == 6:
        gameBoard[2][0] = turn
    elif num == 7:
        gameBoard[2][1] = turn
    elif num == 8:
        gameBoard[2][2] = turn


def check_winner():
    if gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][3] == 'X':
        print("X has won!")
        return "X"
    elif gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O':
        print("O has Won")
        return "O"
    elif gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X':
        print("X has Won")
        return "X"

leave_loop = False
turn_counter = 0

while not leave_loop:
    if turn_counter % 2 == 1:
        print_game_board()
        number_picked = int(input("\n Choose a Number 1-9: "))
        if number_picked >= 1 or number_picked < 9:
            possible_numbers.remove(number_picked)
            modify_array(number_picked, 'X')
        else:
            print("invalid number")
        turn_counter += 1

    else:
        while True:
            cpuChoice = random.choice(possible_numbers)
            print("\nCpu choice:", cpuChoice)
            if cpuChoice in possible_numbers:
                modify_array(cpuChoice, 'O')
                possible_numbers.remove(cpuChoice)
                turn_counter += 1
                break


if __name__ == "__main__":
    print_game_board()