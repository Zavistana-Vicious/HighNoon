from game_Loop import *

#Loop for pplaying the game multiple times
play = 'yes'
while play == 'yes':
    # Game intro
    print ("\nA figure stands in your path ready to duel.\n")
    print ("You can 'shoot', 'dodge', or 'load'. You and your opponent's guns are empty.")
    print ("\nIT'S HIGH NOON!\t(Press 'ENTER' to begin)\n\n")
    input()
    print ("DRAW!\n\n")

    daGame = gameLoop()
    daGame.game()

    print("\n Play again? (yes or no)\n")
    play = input("-> ")
    play = play.lower()
