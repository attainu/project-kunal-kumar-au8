import time
import random
import sys

# variables
Delay = 1
Cells = 100
Dice_Faces = 6

# Snakes 'key' to 'value'
snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

# ladder 'key' to 'value'
ladders = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

# function for greeting and rules
def Rules():
    rules = """
    Welcome to Snake and Ladder Console Game.
    Rules:
      1. Both the players are at starting position i.e. 0. 
      2. If players reach at the bottom of a ladder, you can move up to the top of the ladder.
      3. If playes reach on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position (100) is the winner.
      5. Press enter to roll the dice.
    
    """
    print(rules)

# function for selecting no players
def no_of_players():
    count = 0
    while count < 1:
        players = int(input("How many players wnats to play: "))
        if players <= 4:
            return players
        else:
            print("Maximum no of players is 4, Please select in-between !")

# function for taking players names
def get_player_names():

    player1_name = None
    while not player1_name:
        player1_name = input("Please enter a valid name for first player: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter a valid name for second player: ").strip()

    player3_name = None
    while not player3_name:
        player3_name = input("Please enter a valid name for third player: ").strip()

    player4_name = None
    while not player4_name:
        player4_name = input("Please enter a valid name for forth player: ").strip()

    print("\nMatch will be played between '" + player1_name + "' , '" + player2_name + "' , '" + player3_name + "' and '" + player4_name + "'\n")
    return player1_name, player2_name, player3_name, player4_name


# function for dice display
def get_dice_value():
    time.sleep(Delay)
    dice_value = random.randint(1, Dice_Faces)
    if dice_value == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
        print("Its a " + str(dice_value))
        return dice_value
    if dice_value == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
        print("Its a " + str(dice_value))
        return dice_value
    if dice_value == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
        print("Its a " + str(dice_value))
        return dice_value
    if dice_value == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
        print("Its a " + str(dice_value))
        return dice_value
    if dice_value == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
        print("Its a " + str(dice_value))
        return dice_value
    if dice_value == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
        print("Its a " + str(dice_value))
        return dice_value
        
# function for snake bite
def got_snake_bite(old_value, current_value, player_name):
    print("\n" + "Ohh no! :(" + " ~~~~~~~~8>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))

# function for ladder jump
def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + "Bale Bale :)" + " ||||||||||")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))

# function for dice movement
def snake_ladder(player_name, current_value, dice_value):
    time.sleep(Delay)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > Cells:
        print("You need " + str(Cells - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value

# function that check and greet the winner
def check_win(player_name, position):
    time.sleep(Delay)
    if Cells == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.\n\n")
        sys.exit(1)

# function to game Code start from here...
def start():
    Rules()
    time.sleep(Delay)
    player1_name, player2_name, player3_name, player4_name = get_player_names()
    time.sleep(Delay)

    player1_current_position = 0
    player2_current_position = 0
    player3_current_position = 0
    player4_current_position = 0

    while True:
        time.sleep(Delay)
        input_1 = input("\n" + player1_name + ": " + "Your turn." + " Press the enter to roll dice: ")
        dice_value = get_dice_value()
        time.sleep(Delay)
        print(player1_name + " moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)

        check_win(player1_name, player1_current_position)

        input_2 = input("\n" + player2_name + ": " + "Your turn." + " Press the enter to roll dice: ")
        dice_value = get_dice_value()
        time.sleep(Delay)
        print(player2_name + " moving....")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)

        check_win(player2_name, player2_current_position)

        input_3 = input("\n" + player3_name + ": " + "Your turn." + " Press the enter to roll dice: ")
        dice_value = get_dice_value()
        time.sleep(Delay)
        print(player2_name + " moving....")
        player3_current_position = snake_ladder(player3_name, player3_current_position, dice_value)

        check_win(player3_name, player3_current_position)

        input_4 = input("\n" + player4_name + ": " + "Your turn." + " Press the enter to roll dice: ")
        dice_value = get_dice_value()
        time.sleep(Delay)
        print(player4_name + " moving....")
        player4_current_position = snake_ladder(player4_name, player4_current_position, dice_value)

        check_win(player4_name, player4_current_position)


if __name__ == "__main__":
    start()