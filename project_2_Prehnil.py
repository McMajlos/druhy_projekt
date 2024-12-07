"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Miloslav Přehnil
email: milosprehnil@gmail.com
"""

# Functions

# Print game rules:
def show_game_rules() -> str:
    print(
        """Welcome to Tic Tac Toe
============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
============================================
Let's start the game
--------------------------------------------"""
    )


# Drawing playing board:
def draw_board(fields):
    field = (
        "+---+---+---+\n"
        f"| {fields[1]} | {fields[2]} | {fields[3]} |\n"
        "+---+---+---+\n"
        f"| {fields[4]} | {fields[5]} | {fields[6]} |\n"
        "+---+---+---+\n"
        f"| {fields[7]} | {fields[8]} | {fields[9]} |\n"
        "+---+---+---+"
    )

    print(field)


# Which player is playing:
def who_plays(turn):
    if turn % 2 == 0:
        return "X"
    else:
        return "O"


# Func for checking if the game is finished by finding same fields horizontaly, verticaly and diagonaly:
def game_finished(fields):
    if (
        (fields[1] == fields[2] == fields[3]) or
        (fields[4] == fields[5] == fields[6]) or
        (fields[7] == fields[8] == fields[9])):
        return True
    elif (
        (fields[1] == fields[4] == fields[7]) or
        (fields[2] == fields[5] == fields[8]) or 
        (fields[3] == fields[6] == fields[9])):
        return True
    elif (
        (fields[1] == fields[5] == fields[9]) or
        (fields[3] == fields[5] == fields[7])):
        return True
    else:
        return False


# Func for printing results
def results(complete, turn) -> str:
    # Announce the result
    if complete:
        if who_plays(turn) == "O":
            print("=" * 50)
            print("Congratulations, player X wins!")
            print("=" * 50)
        else:
            print("=" * 50)
            print("Congratulations, player O wins!")
            print("=" * 50)
    else:
        print("=" * 50)
        print("It's a draw!")
        print("=" * 50)


# Main game func
def play_tic_tac_toe():
    fields = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    play = True
    complete = False
    turn = 0

    show_game_rules()

    while play:
        draw_board(fields)
        print("=" * 50)
        player_choice = input(f"Player {who_plays(turn)}'s turn: Choose your number: ")

        if player_choice.isdigit() and int(player_choice) in fields:
            # Check if the selected field is free
            if fields[int(player_choice)] not in {"X", "O"}:
                fields[int(player_choice)] = who_plays(turn)
                turn += 1
            else:
                print("That spot is already taken! Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")

        # Check if the game is finished
        if game_finished(fields):
            play = False
            complete = True
        if turn >= 9:  # All fields filled
            play = False
        
    # Show the final board
    draw_board(fields)

    # Show results
    results(complete, turn)


# Loop with main func made for replay
while True:
    play_tic_tac_toe()
    replay = input("Do you want to play again? (y/n): ").strip().lower()
    if replay != "y":
        print("Thanks for playing, goodbye!")
        break
