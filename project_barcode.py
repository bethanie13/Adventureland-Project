import turtle
import time


class Barcode:
    def __init__(self, life):
        '''
        returns print statements based on the user's input (barcode choice)
        and adds or takes away life points accordingly
        '''
        print('')
        self.life = life

        # testing purposes:
        # print('''This minigame needs not to make the user enter in a barcode, but
        # instead it needs to already have a few in the class.
        # It can be randomly picked, or a particular barcode can be picked
        # based off of the choices the user makes.
        # Each of the barcodes will be predeterminded as good, bad, or neutral.
        # Bad barcode choice: lose life points.
        # Good barcode choice: gain life points.
        # Neutral barcode choice: no gain nor loss.''')
        time.sleep(3.25)
        print('You are walking along a path through Adventureland...')
        time.sleep(3)
        print()
        print('''You stumble across three packages in the middle of your path.
You must pick one of the mysterious packages. Each package has a unique barcode.''') #introducing where the user comes across three boxes
        time.sleep(3.5)
        print()
        print('Package 1: 854650006925, Package 2: 041500799537, Package 3: 020424101923')

        print('')
        self.user_box = input("Enter barcode here:   ") #user must enter a barcode and see what happens
        while self.user_box != "020424101923" and self.user_box != "041500799537" and self.user_box != "854650006925":
            print('')
            print("Input error. Please try again.")
            self.user_box = input("Enter barcode here:   ")
        if self.user_box == "854650006925":
            print('')      #box1 is neutral and contains sunflowers
            print(
                "Great job! You have selected a vase of sunflowers to brighten your day! You may continue your journey through Adventureland.")

        elif self.user_box == "041500799537":
            print('')
            print(       #box2 is bad and contains hotsauce
                '''Ohhh no! You have selected hot sauce and you are forced to drink all of it!! Your tongue is literally on fire!''')
            self.life -= 2
        elif self.user_box == "020424101923":
            print('')    #box3 is good and contains a first aid kit
            print("Hooray! You have selected a first aid kit. This will help you maintain your health. ")
            self.life += 1
        print('')
# Barcode()
