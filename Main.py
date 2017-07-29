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

SelectedIngredient = Interface.GetIngredientFromRecipe(UserRecipe)

UnitAndVolume = Interface.GetUnitAndVolume()

Scaler = MLConverter.GetML(UnitAndVolume.unit , UnitAndVolume.volume, HumanMeasurements ) / SelectedIngredient.ML 

for item in UserRecipe.GetIngredients():
    NewRatio = item.ML * Scaler
    PrintableML =  MLConverter.TurnMLtoHumanMeasurements(NewRatio,HumanMeasurements)
    
    print("%s : %s" % (item.Name , PrintableML))



