from enum import Enum

#from .material_loss import MaterialLoss

"""
Enumeration class for materials
Parent class for FacadeMaterial and ComponentMaterial
"""

class Material(Enum):

    def __init__(self, material):
        self.material = material
    
    #Assign material to facade or components materials list
    def assign(self, target):
        target.materials.append(self)

    #get material value
    
    '#TODO: add function that allow user to define new material and add it to the enumeration list'

"""
Enumeration for Facade material
TODO: modify the material value to match the mapping key
"""

import sys
import os

class FacadeMaterial(Material):
    # directory and dataset declared
    # dataset is opened as a txt file
    directory = os.getcwd()
    folder_name = "ChecklistImplementation"
    dataset_name = 'facadeMaterialDataset.txt'
    #temp_dataset_path = os.path.join(directory, folder_name)
    dataset_path = os.path.join(directory, dataset_name)
    dataset = open(dataset_path)
    # directory = '/Users/youngjun/Documents/GitHub/Checklist_Generation/'
    # dataset = open(directory + 'dataset.txt')

    # final enum
    # Fascinating mechanism.
    # Recall that every iteration of ".readline()" makes the next ".readline()" read the next
    # row of the txt file. Now, look at the dataset.txt. It has the "code" every 2 rows. Why is that?
    # Take a look at the loop. It executes the first row, then the second row is accessed in the
    # if statement. While it is a blank space on the txt file, recall that these blank spaces contain
    # a "/n" to go to the next line. Thus, the only instance where the row is truly empty is the last
    # row, where I have no row afterwards and thus, there is no "/n" in the last row.
    # This is why the loop will stop at the last row, the empty row.
    # The dataset.txt, thus, must have a line of "code" every 2 lines.
    # Why not use a for loop? Because in enum, changing variable more than once is forbidden.
    # Loops must be done in a way that the variable is not changed.
    # At the bottom of this .py, there is are print functions for testing.
    while True:
        exec(dataset.readline())
        if dataset.readline() == '':
            break

    # transitional enum
    """
    directory = '/Users/youngjun/Documents/GitHub/Checklist_Generation/'

    dataset = open(directory + 'dataset.txt')

    exec(dataset.readline())
    exec(dataset.readline())
    exec(dataset.readline())
    exec(dataset.readline())
    exec(dataset.readline())
    exec(dataset.readline())
    exec(dataset.readline())
    exec(dataset.readline())
    exec(dataset.readline())
    exec(dataset.readline())
    exec(dataset.readline())

    """

    # Original enum
    """
    castIron = "cast iron"
    'TODO: map similar materials to one material enumeration'
    castStone = "stone"
    naturalStone = "stone"
    concrete = "concrete"
    glass = "glass"
    masonry = "brick masonry"
    metal = "metal"
    sheetMetal = "metal"
    stucco = "stucco"
    EIFS = "EIFS"
    terraCotta = "terra cotta"
    """

"""
Enumeration materials for facade components
Materials from AUtoDesk default material library
"""

class ComponentMaterial(Material):

    glass = 'glass'
    wood = 'wood'
    steel = 'steel'
    porcelain = 'porcelain'
    plastic = 'plastic'
    aluminum = 'alumninum'
    concreteMasonryUnit = 'concrete masonry unit'
    brick = 'brick'
    metal = 'metal'
    concreteWallPanel = 'concrete wall panel'
    stucco = 'stucco'
    terrazo = 'terrazo'
    travertine = 'travertine'
    gypsum = 'gypsum'
    ceramic = 'ceramic'
    plaster = 'plaster'
    stone = 'stone'

    
class SoilingMaterial(Material):
    atmospheric = 'atmospheric'
    biological = 'biological'
    bituminous = 'bituminous'
    cementitious = 'cementitious'
    copper = 'copper'
    efflorescene = 'efflorescene'
    guano = 'guano'
    leachedSalt = 'leached salt'
    paint = 'paint'
    rust = 'rust'







masonry_facade = FacadeMaterial('brick masonry')
cast_iron_facade = FacadeMaterial('cast iron')
cast_stone_facade = FacadeMaterial('stone')
natural_stone_facade = FacadeMaterial('stone')
concrete_facade = FacadeMaterial('concrete')
glass_facade = FacadeMaterial('glass')
metal_facade = FacadeMaterial('metal')
sheet_metal_facade = FacadeMaterial('metal')
stucco_facade = FacadeMaterial('stucco')
EIFS_facade  = FacadeMaterial('EIFS')
terra_cotta = FacadeMaterial('terra cotta')




directory = os.getcwd()
folder_name = "ChecklistImplementation"
dataset_name = 'facadeMaterialDataset.txt'
dataset_path = os.path.join(directory, dataset_name)
dataset = open(dataset_path)



start_exec = False

while True:
    #print("why")
    current_line = dataset.readline()
    #print(current_line)

    if current_line == "#start newly added components\n":

        start_exec = True
        #print("veri")

    if start_exec:
        #print("???")
        current_line = current_line[:current_line.find("=")].strip()
        for index in range(len(current_line)):
            if current_line[index].isupper():
                current_line = current_line[:index] + "_" + current_line[index:].lower()

        script = current_line + " = FacadeMaterial(\"" + current_line + "\")"
        #print(script, 201932)
        exec(script)
    if dataset.readline() == '':
        break









glass = ComponentMaterial('glass')
wood = ComponentMaterial('wood')
steel = ComponentMaterial('steel')
porcelain = ComponentMaterial('porcelain')
plastic = ComponentMaterial('plastic')
aluminum = ComponentMaterial('alumninum')
concreteMasonryUnit = ComponentMaterial('concrete masonry unit')
brick = ComponentMaterial('brick')
metal = ComponentMaterial('metal')
concreteWallPanel = ComponentMaterial('concrete wall panel')
stucco = ComponentMaterial('stucco')
terrazo = ComponentMaterial('terrazo')
travertine = ComponentMaterial('travertine')
gypsum = ComponentMaterial('gypsum')
ceramic = ComponentMaterial('ceramic')
plaster = ComponentMaterial('plaster')
stone = ComponentMaterial('stone')

atmospheric_soiling = SoilingMaterial('atmospheric')
biological_soiling = SoilingMaterial('biological')
bituminous_soiling = SoilingMaterial('bituminous')
cementitious_soiling = SoilingMaterial('cementitious')
copper_soiling = SoilingMaterial('copper')
efflorescene = SoilingMaterial('efflorescene')
guano = SoilingMaterial('guano')
leachedSalt = SoilingMaterial('leached salt')
paint_soiling = SoilingMaterial('paint')
rust_soiling = SoilingMaterial('rust')

# x = FacadeMaterial('stone')
# y = FacadeMaterial('cast iron')
# z = FacadeMaterial('brick masonry')
# print(x)
# print(y)
# print(z)