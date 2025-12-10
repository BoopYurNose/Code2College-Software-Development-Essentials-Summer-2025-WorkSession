import random

OptionsStorage = [
    "Rock",
    "Paper",
    "Sissors",
]


def MainGame():
    print("Welcome to the MainGame function! please type a option of Rock Paper or Sissors")

    UserChoice = input()

    RandomBotChoice = random.choice(OptionsStorage)
    

    for Option in OptionsStorage:
        if UserChoice == Option:

            if UserChoice == RandomBotChoice:
                print(f"You both picked {RandomBotChoice} you tied!")
            elif RandomBotChoice == "Rock":
                if UserChoice == "Paper":
                    print(f"You won bot choose {RandomBotChoice} and you choose {UserChoice}")
                elif UserChoice == "Sissors":
                    print(f"You lost bot choose {RandomBotChoice} and you choose {UserChoice}")

            elif RandomBotChoice == "Paper":
                if UserChoice == "Sissors":
                    print(f"You won bot choose {RandomBotChoice} and you choose {UserChoice}")
                elif UserChoice == "Rock":
                    print(f"You lost bot choose {RandomBotChoice} and you choose {UserChoice}")

            elif RandomBotChoice == "Sissors":
                if UserChoice == "Rock":
                    print(f"You won bot choose {RandomBotChoice} and you choose {UserChoice}")
                elif UserChoice == "Paper":
                    print(f"You lost bot choose {RandomBotChoice} and you choose {UserChoice}")

            print("returning to StartGame")
            StartGame()
            break
        elif UserChoice == Option:
            print("nope doesn't work try again")
            MainGame()
            

def StartGame():
    print("Welcome to rock, paper, sissors would you like to play if you would type Yes if not then type Quit")
    UserChoice = input()

    if UserChoice == "Yes":
        MainGame()
    elif UserChoice == "Quit":
        print("No worries have a good rest of your day")
    else:
        print("You need to type either Yes or Quit try again")
        StartGame()



StartGame()