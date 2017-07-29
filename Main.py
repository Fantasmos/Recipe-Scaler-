import re
import Dictionary
import MLConverter
import CookingUtilities

import UserInterface

from fractions import Fraction

AllDicts = Dictionary.GetAllDictionaries()
Interface = UserInterface.ConsoleInterface()
HumanMeasurements = Interface.GetDictionaryToUse(AllDicts)


'''Get all the ingredients from User'''

UserRecipe = Interface.GetRecipeFromUser(HumanMeasurements)

'''Scale entire recipe by changing one ingredient''' 

Running = True

while (Running): 
    try:
        Interface.ScaleRecipe(UserRecipe, HumanMeasurements)
    except: 
        Interface.Print("An error occured, please try again")
    