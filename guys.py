import random

class Guy(object):
    def __init__(self):
        self.alive = True
        self.bullets = 0
        self.choice = ""

    def choose(self):
        valid = False
        print ("\nEnter your choice: 'shoot, 'dodge', or 'load'")

        while valid == False:
            self.choice = input("->  ")
            self.choice = self.choice.lower()

            if self.choice == 'shoot' or self.choice == 'dodge' or self.choice == 'load':
                valid = True
            else:
                print ("Invalid input, try again")

        #Player actions resolved
        if self.choice == 'shoot':
            if self.bullets == 0:
                self.choice = 'click'
            else:
                self.bullets = self.bullets - 1
        elif self.choice == 'load':
            self.bullets = self.bullets + 1

class BOT(Guy):
    def __init__(self):
        self.alive = True
        self.bullets = 0
        self.choice = ""

    def choose(self, rc): # rc is the roundCount
        if rc == 1:
            self.choice = 'load'
        elif self.bullets == 0:
            choices = ['dodge', 'load']
            self.choice = random.choice(choices)
        elif self.bullets == 3:
            choices = ['dodge', 'shoot']
            self.choice = random.choice(choices)
        else:
            choices = ['shoot', 'dodge', 'load']
            self.choice = random.choice(choices)

        #Comp Actions resolved
        if self.choice == 'shoot':
            self.bullets = self.bullets - 1
        elif self.choice == 'load':
            self.bullets = self.bullets + 1
