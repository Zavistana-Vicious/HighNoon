from guys import *

class gameLoop(object):
    def __init__(self):
        self.player = Guy()
        self.comp = BOT()
        self.result = ""
        self.roundCount = 0

    def game(self):
        while self.player.alive == True and self.comp.alive == True:

            self.roundCount = self.roundCount + 1

            self.player.choose()
            self.comp.choose(self.roundCount)

            print ('\nPlayer Action: %s\tComp Action: %s' % (self.player.choice, self.comp.choice))

            #Choice results (Deaths only)
            if self.comp.choice == 'shoot' and self.player.choice == 'shoot':
                self.player.alive = False
                self.comp.alive = False
                self.result = "You both shot each other."
            elif self.comp.choice == 'shoot' and (self.player.choice == 'load' or self.player.choice == 'click'):
                self.player.alive = False
                if self.player.choice == 'load':
                    self.result = "You got shot while loading"
                else:
                    result = "'Click'.You didn't have any bullets and got shot"
            elif self.comp.choice == 'load' and self.player.choice == 'shoot':
                self.comp.alive = False
                self.result = "You killed him. Nice."

        # Prints endgame results
        print ("\n")
        print (self.result)
