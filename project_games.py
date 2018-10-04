from project_nim import *
from project_barcode import *
from project_even_odd import *
from project_places import *
from project_lifepoints import *
from project_three_letters import *  # here is where we are importing all of the minigmaes
from project_zodiac_sign import *    #into the class that will be able to runs all of the minigames at once
from project_life_pathnum import *
from project_chocolate import *

#make it so that there is space after the input questions to avoid the user having to put the space which casuses issues

class Games:
    def __init__(self):
        '''
        main code that plays all of the minigames
        '''


        print('Welcome to Adventureland, we are seeking a new ruler!')
        time.sleep(2)
        print()
        print('Our current king is awfully wicked and the Adventurers need YOU to save the day!')
        time.sleep(2.)
        print()
        print("Many challenges await you that could cost you your life.")   #introduction to the game for the user
        time.sleep(2)
        print()
        print('''If you pass all of Adventureland's obstacles, you will have proven
your worthiness to the citizens of our land and restore peace!''')
        time.sleep(3)
        print()
        print("Good luck... You are going to need it!")


        print('')
        time.sleep(2)

        self.life = LifePoints()    #enables life points to be ran in the game
        self.all_games = (x for x in [Barcode, Places, Zodiac, Even_Odd,Chocolate, Life_Path,Nim, Three_Letters])  # all the minigames
        while not self.life.dead():
            self.levels()

        else:
            quit()

    def levels(self):              #goes to next game if the user has life points
        time.sleep(2)
        self.current_game = next(self.all_games)(self.life)


def main():
    Games()        #the main where the games are called


main()
