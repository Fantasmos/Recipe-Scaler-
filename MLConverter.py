from fractions import Fraction
import Ingredient
import CookingUtilities

def TurnMLtoHumanMeasurements(ML , HumanMeasurements):
    Pair = HumanMeasurements.GetSmallestValue()
    Threshold = Pair[1]
    
    Measurements = {}

    PreviousMeasurement = None
    PreviousResult = None
    CurrentResult = None

    '''Wish I could rename ML to MLRemaining'''
    while Threshold <= ML: 
        
        OptimalResult = 9999
        OptimalMeasurement = None
        OptimalMLRemaining = None
        for Key, Value in HumanMeasurements.Dictionary.items(): 
            
            CurrentResult = ML // Value 
            

            if (OptimalMeasurement is None) | ((CurrentResult <= OptimalResult) & (CurrentResult >= 1) ) :
                if (OptimalMLRemaining is None ) or (( (ML % Value) < OptimalMLRemaining) or (CurrentResult < OptimalResult)) :
                    if CurrentResult != 0: 
                        OptimalResult = CurrentResult
                    OptimalMeasurement = Key 
                    OptimalMLRemaining = (ML % Value)

            

        ML = OptimalMLRemaining
        
        Measurements[OptimalMeasurement] = OptimalResult
    PostString = Pair[0] + " Remaining"
    Measurements[PostString] = ML / Pair[1]  
    return Measurements 


def GetML(unit, Numbers , UnitConversions): 
    ML = UnitConversions.GetEntry(unit)
    
    MeasurementParts = Numbers.split(' ')
    MeasurementParts = filter(None, MeasurementParts)
    TotalMeasurement = 0
    TotalMeasurement = float((sum(Fraction(s) for s in MeasurementParts)) * ML)
    
    '''Fix this properly, later'''
    if TotalMeasurement == 0:
        TotalMeasurement = TotalMeasurement + 1
    return TotalMeasurement


