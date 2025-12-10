Options = {
    "Rock",
    "Paper",
    "Sissors",
}


local UserPlaying = true

function MainGame()
    
    print("Great, welcome to the game now type in either Rock Paper or Sissors")
    UserChoice = io.read()
    local BotChoice = math.random(1, #Options)
    for k, v in pairs(Options) do
        if UserChoice == v then
            print("The Bot Chooses "..Options[BotChoice])
            

            if BotChoice == 1 then -- if bot chooses rock
                if UserChoice == "Rock" then
                    print("You both choose rock you tied")
                elseif UserChoice == "Paper" then
                    print("You won you choose paper")
                elseif UserChoice == "Sissors" then
                    print("You lost you choose sissors")
                end
            end
            if BotChoice == 2 then -- if bot chooses paper
                if UserChoice == "Rock" then
                    print("You lost you choose rock")
                elseif UserChoice == "Paper" then
                    print("You both choose paper you tied")
                elseif UserChoice == "Sissors" then
                    print("You won you choose sisssors")
                end
            end
            if BotChoice == 3 then -- if bot chooses sissors
            if UserChoice == "Rock" then
                    print("You won you choose rock")
                elseif UserChoice == "Paper" then
                    print("You won you choose paper")
                elseif UserChoice == "Sissors" then
                    print("you both choose sissors you tied")
                end
            end

            print("Returning to startingMenu")
            StartingMenu()
            break
            return
        end
    end
    if UserPlaying == true then
        print("nope you need to type Rock Paper or Sissors try again")
        MainGame()
    end
end



function StartingMenu()
    print("Welcome to the Rock paper sissors game would you like to start? type Yes if you do otherwise type Quit if you want to exit")
    UserChoice = io.read()

    if UserChoice == "Yes" then
        print("Taking to main game")
        MainGame()
    elseif UserChoice == "Quit" then
        print("Goodbye, have a good day!")
        UserPlaying = false
        return
    elseif UserChoice ~= "Yes" and UserChoice ~= "Quit" then
        print("Try again you need to type either Yes or Quit")
        StartingMenu()
    end
end


if UserPlaying == true then
    StartingMenu()
end


