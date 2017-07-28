import re
from fractions import Fraction

print("Hello, please put in your ingrediants")


'''Look into using this'''
'''http://www.jsward.com/cooking/conversion.shtml'''
AmericanMeasurementsML = {
    'CUP': 240,
    'TEASPOON': 5,
    'TABLESPOON': 16,
    'GALLON': 3.8,
    'QUART' : 950,
    'PINT': 475,
    'OUNCE': 30,
}

UKMeasurementML = {
    'TABLESPOON': 15,
    'CUP': 250,
    'TEASPOON': 5,
    'OUNCE' : 28.4131,
}

'''Tell the user a tablespoon is 20ML'''
AustralianMeasurementsML = {
    'TABLESPOON': 20,
}
Dictionary = AmericanMeasurementsML

Abbreviations = {
    'TBSP' : 'TABLESPOON',
    'TSP' : 'TEASPOON',
    'OZ' : 'OUNCE'
}

'''Setup Dictionary'''
response = input("Are you using the imperial (UK/Australia) system?")
if response == "Y" :
    
    for Measurement, ML in UKMeasurementML.values():
        Dictionary[Measurement] = ML

    response = input("Are you using the Australian system? (1TBSP = 20ml)")
    if response == "Y":
        for Measurement, ML in AustralianMeasurementsML.values():
            Dictionary[Measurement] = ML

GivingIngredients = True

EachIngredientUnParsed = []
while GivingIngredients: 
    Response = input("Please put in ingredients")
    if Response == "Done":
        GivingIngredients = False
        break
    else:
        ParsedResponseVolume = re.split('[^0-9 | ' ' | "/" ]',Response)
        Ingredient = Response.split(ParsedResponseVolume[0],1)[-1]
        print("Ingredient is: %s with volume: %s" % (Ingredient , ParsedResponseVolume[0]))
        Pair = (Ingredient , ParsedResponseVolume[0])
        EachIngredientUnParsed.append(Pair)






'''Make Recipe'''
for item in EachIngredientUnParsed:
    
    '''Fuck this code doesn't documentItself'''
    MeasurementUnit = item[0].split(' ', 1)
    if (Abbreviations.get(MeasurementUnit[0].upper()) != None):
        MeasurementUnit[0] = Abbreviations[MeasurementUnit[0].upper()]

    
    if (Dictionary.get(MeasurementUnit[0].upper()) == None):
        ML = 1
    else:
        ML = Dictionary[MeasurementUnit[0].upper()]
    
    '''This will split 1 and 1/2 into seperate items in a list (1, 1/2)'''
    MeasurementParts = item[1].split(' ')
    MeasurementParts = filter(None, MeasurementParts)
    TotalMeasurement = 0
    TotalMeasurement = float((sum(Fraction(s) for s in MeasurementParts)) * ML)
    
    
    print("Ingredient is: %s with volume: %s ML" % (MeasurementUnit[-1] , TotalMeasurement))
