Map = [
    "xxxxx",
    "x...x",
    "x...x",
    "x.t.x",
    "xxxxx",
]

UserOptions = [
    "up",
    "down",
    "left",
    "right",
]

Player_Row = 2
Player_Column = 2


def Movement(Current_Row, Current_Column, Direction):
    New_Row = Current_Row
    New_Column = Current_Column
    
    if Direction == "up":
        New_Row -= 1
    elif Direction == "down":
        New_Row += 1
    elif Direction == "left":    
        New_Column -= 1
    elif Direction == "right":
        New_Column += 1

    if Map[New_Row][New_Column] == "x":
        print("You are hitting a wall. Try moving a different direction")
        if Direction == "up":
            New_Row += 1
        elif Direction == "down":
            New_Row -= 1
        elif Direction == "left":    
            New_Column += 1
        elif Direction == "right":
            New_Column -= 1


    return New_Row, New_Column


while Map[Player_Row][Player_Column] != "t":
    
    print("Select a direction to move. Here are your options below")
    for Choices in UserOptions:
        print(Choices)
    
    UserChoice = input()
    while UserChoice not in UserOptions:
        print("Try again you need to type a valid direction")
        UserChoice = input()

    Player_Row, Player_Column = Movement(Player_Row, Player_Column, UserChoice)
    print(f"Your row is {Player_Row}")
    print(f"Your Column is {Player_Column}")

print("Good job you found the treasure")