'''Look into using this'''
'''http://www.jsward.com/cooking/conversion.shtml'''


class AmericanUnits ():
    def __init__(self):
        self.Dictionary = {}

        self.AddEntry('CUP', 240)
        self.AddEntry('TEASPOON', 5)
        self.AddEntry('TABLESPOON', 16)
        self.AddEntry('GALLON', 3785)
        self.AddEntry('QUART',  950)
        self.AddEntry('PINT', 475)
        self.AddEntry('OUNCE', 30)   
        

        self.Abbreviations = {}
        self.AddAbbreviation('TBSP', 'TABLESPOON')
        self.AddAbbreviation('TSP', 'TEASPOON')
        self.AddAbbreviation('OZ', 'Ounce')     
    
        for Key in self.Dictionary:
            Entry = (Key + "s")
            self.AddAbbreviation(Entry, Key)

    def AddEntry(self, key,value):
        self.Dictionary[key.upper()] = value

    def ReplaceEntry(self, key,value):
        self.AddEntry(key,value)

    def AddAbbreviation(self, key, value):
        self.Abbreviations[key.upper()] = value

    def GetEntry(self, key):
        if key.upper() in self.Abbreviations:
            key = self.Abbreviations[key.upper()]
        
        if key.upper() in self.Dictionary:
            return self.Dictionary[key.upper()]
        else:
            return 1 
    def GetSmallestValue(self):
        ReturnValue = None 

        for key, value in self.Dictionary.items():
            if (ReturnValue is None) or (value < ReturnValue) : 
                ReturnValue = value 
        return ReturnValue


class UKUnits (AmericanUnits):
    def __init__(self):
        super().__init__()
        self.ReplaceEntry("tablespoon", 15)
        self.ReplaceEntry("CUP",250)
        self.ReplaceEntry("TEASPOON",5)
        self.ReplaceEntry("OUNCE",28)

class AusUnits (UKUnits): 
    def __init__(self):
        super().__init__()
        self.ReplaceEntry('TABLESPOON' , 20)


def GetAllDictionaries ():
    Tuple = (AmericanUnits, UKUnits , AusUnits)
    return Tuple