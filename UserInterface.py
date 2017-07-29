import Dictionary
import re
import CookingUtilities
import MLConverter
class UnitAndVolume(): 
    def __init__(self, unit, volume):
        self.unit = unit
        self.volume = volume

class VolumeAndString(): 
    def __init__(self, string, volume):
        self.string = string
        self.volume = volume

class Interface():
    def GetDictionaryToUse(self, DictionariesToChooseFrom):
        raise NotImplementedError('Abstract method has not been overriden!') 
    def SplitStringByVolume(self, Response):
        raise NotImplementedError('Abstract method has not been overriden!') 
    '''Unit is in [0] and volume is in [1]'''
    def GetUnitAndVolume(self): 
        raise NotImplementedError('Abstract method has not been overriden!') 

    def GetAllIngredientNameAndVolumeFromUser(self):
        raise NotImplementedError('Abstract method has not been overriden!')  
    def GetIngredientFromRecipe(self, recipe):
        raise NotImplementedError('Abstract method has not been overriden!') 
    def GetRecipeFromUser(self , HumanMeasurements):
        raise NotImplementedError('Abstract method has not been overriden!') 

class ConsoleInterface(Interface):
    def GetDictionaryToUse(self, DictionariesToChooseFrom):
        HumanMeasurements = None

        while (HumanMeasurements is None): 

            iterator = 1
            AllDicts = Dictionary.GetAllDictionaries()
            for entry in AllDicts: 
                print ("%s. %s"  % (iterator, entry.__name__))
                iterator = iterator + 1
            try:
                EntryWanted = int(input("Please type the number you would like")) 
                HumanMeasurements = AllDicts[EntryWanted - 1]()
            except:
                print("An error occured, please try again")
        return HumanMeasurements

    def SplitStringByVolume(self, Response):
        ParsedResponseVolume = re.split('[^0-9 | ' ' | "/" ]',Response)
        IndividualIngredient = Response.split(ParsedResponseVolume[0],1)[-1]
        print("Ingredient is: %s with volume: %s" % (IndividualIngredient , ParsedResponseVolume[0]))
        Pair = VolumeAndString(IndividualIngredient,ParsedResponseVolume[0])
       
        return Pair
    
    '''Unit is in [0] and volume is in [1]'''
    def GetUnitAndVolume(self): 
        Response = input("Type up your volume")
        Pair = self.SplitStringByVolume(Response)

        return UnitAndVolume(Pair.string, Pair.volume)

    def GetAllIngredientNameAndVolumeFromUser(self):
        EachIngredientUnParsed = []
        GivingIngredients = True
        while GivingIngredients: 
            Response = input("Please put in ingredients")
            if Response == "Done":
                GivingIngredients = False
                break
            else:
                Pair = self.SplitStringByVolume(Response)
                EachIngredientUnParsed.append(Pair)
        
        return EachIngredientUnParsed

    def GetIngredientFromRecipe(self, recipe):
        print ("Which ingredient do you want to change")

        iterator = 0
        for item in recipe.GetIngredients():
            print("%s. %s" % (iterator , item.Name))
            iterator = iterator + 1

        SelectedNumber = int(input ("Type which one you would like to modify"))

        NameOfSelected = (recipe.GetIngredients()[SelectedNumber].Name)
        VolumeOfSelected = int(recipe.GetIngredients()[SelectedNumber].ML)

        print("You selected: %s" %(NameOfSelected))

        return recipe.GetIngredients()[SelectedNumber]

    def ParseIngredient(self, string, volume , HumanMeasurements  ):
    
        '''An Input would look like:  1 1/2 Cups of flour'''
        MeasurementUnit = string.split(' ', 1)
        
        TotalMeasurement = MLConverter.GetML(MeasurementUnit[0],  volume , HumanMeasurements)
        
        return CookingUtilities.Ingredient(MeasurementUnit[1],TotalMeasurement)

    def GetRecipeFromUser(self , HumanMeasurements):
        EachIngredientUnParsed = self.GetAllIngredientNameAndVolumeFromUser()
        UserRecipe = CookingUtilities.Recipe()
        for item in EachIngredientUnParsed:
            
            Ingredient = self.ParseIngredient(item.string, item.volume, HumanMeasurements)
            UserRecipe.AddToRecipe(Ingredient)
        
        return UserRecipe