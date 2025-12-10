App_Balance = 32
AmeliaMoney = 40
UserName = "Amelia"

print("Welcome to Cafe Curtis App")

function EnterCard()
    print("Enter your 6-digit gift card number:")
    Card_Code = io.read()
    if Card_Code == "123456" then
        MoneyDeposit()
    else
        print("Error wrong card number. Try again")
        EnterCard()
    end
end

function MoneyDeposit()
    print("Hello "..UserName)
    print("How much money would you like to add to your Cafe Curtis App?")
    MoneyAmount = io.read()
    MoneyAmount = tonumber(MoneyAmount)
    if MoneyAmount > AmeliaMoney then
        print("Error you don't have enough money to add that to your Cafe Curtis App BROKIEEEE try again broke ass! bum!!")
        MoneyDeposit()
    else
        App_Balance = App_Balance + MoneyAmount
        AmeliaMoney = AmeliaMoney - MoneyAmount
        print("Your Cafe Curtis App balance is now "..App_Balance.." The amount of money in your bank account is "..AmeliaMoney)
    end
end

EnterCard()