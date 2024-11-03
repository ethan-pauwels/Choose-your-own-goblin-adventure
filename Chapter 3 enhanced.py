from time import sleep
import sys
def StartGame():
    print("You are walking through a busy city street")
    sleep(.75)
    print("Someone bumps into you and steals your wallet")
    sleep(.75)
    
    
def ChaseTheif():
    sleep(.75)
    path = (input("Do you chase the theif to get your wallet? (yes/no) "))
    if 'yes' == path:
         print("Uh-oh. The theif didn't like that")
         sleep(1.25)
    elif 'no' == path:
         print("You were never the chasing type anyway")
         sleep(1.25)
         print("The theif did take all of your money though")
         sleep(1.25)
         print("You have no money for food or shelter. :(")
         sleep(1.25)
         print("You die in the city streets. Broke and hungry. YOU LOSE")
         sleep(5)
         quit()

    else:
         print("Invalid Input. Try again!")
         sleep(2)
         ChaseTheif()

def Kidnapped():
    print("The theif snatches you off the street")
    sleep(1.25)
    print("Throws you in a van and puts you in a dungeon")
    sleep(1.25)
    print("The dungeon floor is populated with some trinkets")
    sleep(1.25)
    print("A collection of BONES")
    sleep(1.25)
    print("a big ROCK")
    sleep(1.25)
    print("and a big shiny COIN")
    sleep(1.25)

    choice = ""
    while choice.upper() != "ROCK":
        choice = input("Which of these tools will free you from the dungeon? ")
        if choice.upper() != "ROCK":
            print("You fumble around in the dungeon with your trinket")
            sleep(1.5)
            print("but you aren't any closer to getting out of the dungeon")
            sleep(1.5)
            print("What other trinket will you grab? (BONES/ROCK/COIN) ")
         
def JailBreak():
    print("You grab the rock")
    sleep(1.5)
    print("It feels good in the hands")
    sleep(1.25)
    print("The bars on the bottom left of the cage look old and rusted")
    sleep(1.25)
    print("You smash those bars until they break off the cage")
    sleep(1.25)
    print("Smash Smash Smash")
    sleep(1.25)
    print("You squeeze yourself through the cage")
    sleep(1.25)
    print("Uh-oh your pants get caught on the rused bars")
    sleep(1.25)
    print("and you hear someone coming down the dungeon halls")
    sleep(1.25)
    choice2 = (input("Do you take take your pants off or keep trying to squeeze? (PANTS/SQUEEZE) "))
    if 'pants' == choice2:
         print("The footsteps grow louder")
         sleep(1.25)
         print("You undo your belt and lose your pants")
         sleep(1.25)
         print("By some terrible act of fate the pants get even more tied up in the bars")
         sleep(1.5)
         print("With yourslef still stuck half in the cage half in the pants")
         sleep(1.5)
         print("The footsteps grow even louder")
         sleep(1.5)
         print("It's the theif")
         sleep(1.5)
         print("He laughs at your situation")
         sleep(1.5)
         print("How humiliating")
         sleep(1.5)
         print("You die of embarrassment")
         print("Game Over")
         sleep(5)
         quit()
    elif 'squeeze' == choice2:
         print("Your persistance pays off")
         sleep(1.25)
         print("You wiggle your way out of the cage")
         sleep(1.25)
         print("You sprint down the hall and into a room full of loot")
         
         

    else:
         print("Invalid input")
         print("Try again!")
         sleep(2)
         JailBreak()
def left():
    print()
    print("You run hard down the right path")
    sleep(1.25)
    print("You begin to see a light at the end of the path")
    sleep(1.25)
    print("You can almost taste the freedom")
    sleep(1.25)
    print("Once you lay eyes on the exit...")
    sleep(1.25)
    print("You are grabbed by the theif once again!")
    sleep(1.25)

def right():
    print("You run hard down the left path")
    sleep(1.25)
    print("This path leads to a single door")
    sleep(1.25)
    print("You open that door and see 2 hungry lions")
    sleep(1.25)
    print("They maul you instantly")
    sleep(1.25)
    print("Someone should really put a sign up")
    print("GAME OVER")
    quit()
         
def WalletTime():
    sleep(.75)
    print("You find yourself in what must be the theif's loot room")
    sleep(1.25)
    print("There you see it")
    sleep(1.25)
    print("Your wallet!")
    sleep(1.25)
    print("You take whats yours and leg it to an exit")
    sleep(1.25)
    print("Problem is, this dungeon has many paths")
    choices = {
        'left': left,
        'right': right
    }

    while True:
        path2 = input("Which path will you choose? (left/right): ").lower()
        if path2 in choices:
            choices[path2]()
            break
        else:
            print("Invalid choice. Please enter 'left' or 'right'.")
    
    
    

def NotAgain():
    print("In the struggle you see that you have two options")
    choice3 = (input("Do you KICK him in the shins or grab a nearby ROCK? "))
    if 'rock' == choice3:
         sleep(1.25)
         print("You grab a rock on the ground in the midst of the struggle")
         sleep(1.25)
         print("This feels even better in the hands")
         sleep(1.25)
         print("You smash the rock over the theif's head")
         sleep(1.25)
         print("He's stunned")
         sleep(1.25)
         print("You take advantage of your window and break out of the dungeon")
         sleep(1.25)
         print("You are free with all of your belongings once again!")
         sleep(1.25)
         print("You navigate your way back home")
         sleep(1.25)
         print("You kick your shoes off")
         sleep(2.5)
         print("And enjoy some nice peaceful rest")
         sleep(1.25)
         print("Now you know not to take a stroll down thieves alley again")
         sleep(2)
         print("YOU WIN!")
         sleep(10)
         quit()
         
         
    elif 'kick' == choice3:
         sleep(1.25)
         print("You kick him in the shins as hard as you can")
         sleep(1.25)
         print("he doesn't flinch")
         sleep(1.25)
         print("Oh-No")
         sleep(1.25)
         print("He has shins of steel")
         sleep(1.25)
         print("You're in real trouble now")
         sleep(1.25)
         print("He rips the wallet out of your hand again")
         sleep(1.25)
         print("And throws you back into the dungeon")
         sleep(1.25)
         print("Game Over")
         sleep(5)
         Kidnapped()

    else:
         print("Invalid Input!")
         print("Try Again!")
         sleep(2)
         NotAgain()
    
while True:       
    StartGame()
    ChaseTheif()
    Kidnapped()
    JailBreak()
    WalletTime()
    NotAgain()
