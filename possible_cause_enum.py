from enum import Enum

class Material(Enum):

    def __init__(self, material):
        self.material = material
    
    #Assign material to facade or components materials list
    def assign(self, target):
        target.materials.append(self)

