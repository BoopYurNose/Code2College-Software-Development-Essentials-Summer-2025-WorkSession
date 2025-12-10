Card_Balance = 10
AmeliaWallet = 20

print("Welcome to the Cafe Curtis App!")

def EnterCode():
    CardCode = input("Enter your 6 digit gift card number")
    if CardCode == "123456":
        print("Access granted \n")
        MainThing()
    else:
        print("This did not work try again")
        EnterCode()





def MainThing():
    global Card_Balance, AmeliaWallet
    MoneyAmount = input("How much money would you like to add to your Cafe Curtis GiftCard?")
    MoneyAmount = int(MoneyAmount)
    if MoneyAmount > AmeliaWallet:
        print("Error you don't have that much money to put into your gift card.. HAHAHA BROKE LOSER!.. try again")
        MainThing()
    else:
        AmeliaWallet -= MoneyAmount
        Card_Balance += MoneyAmount
        print(f"Success you have {Card_Balance} amount of funds in your gift card and {AmeliaWallet} in your wallet")

EnterCode()