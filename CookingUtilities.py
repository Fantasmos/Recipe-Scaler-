class Ingredient():

    def __init__(self, Name, ML): 
        self.Name = Name
        self.ML = float(ML)

class Recipe():
    
    def __init__(self):
        self.ingredients = []
    def AddToRecipe(self, Ingredient):
        self.ingredients.append(Ingredient)
    def GetIngredients(self):
        return self.ingredients