
#superstructure imports
from facade_component import FacadeComponent
from shapely.geometry import Polygon

#vertical imports
#from facade_component import FacadeComponent
#from shapely.geometry import Polygon
#from material_enum import *



#horizontal imports
#from _typeshed import Self
#from facade_component import FacadeComponent
#from shapely.geometry import Polygon
from material_enum import *





# Store the hierarchy of facade components
# group the instances based on the structure







def comp_init(self, compType, materials, comPlane, subcomponents=..., safeCon=None):
    #super().__init__(compType, materials, comPlane, subcomponents=[], safeCon=None)
    #super(self.__class__, self).__init__(compType, materials, comPlane, subcomponents=[], safeCon=None)
    super(self.__class__, self).__init__(compType, materials, comPlane, subcomponents=subcomponents, safeCon=None)

###source: https://stackoverflow.com/questions/34142895/dynamic-class-inheritance-using-super
# source: https://python-course.eu/oop/dynamically-creating-classes-with-type.php
# source: https://www.geeksforgeeks.org/create-classes-dynamically-in-python



#get text file containing list of classes instead


directory = os.getcwd()
folder_name = "ChecklistImplementation"
dataset_name = 'classDataset.txt'
#temp_dataset_path = os.path.join(directory, folder_name)
dataset_path = os.path.join(directory, dataset_name)
dataset = open(dataset_path)



#list_of_classes = ['AirConditioningUnit','AllGlassEntrance','Antenna','AutomaticEntrance','Awning','BalancedDoor','BalconyFloor','BalconyWall','BallisticsResistantGlazing','Baluster','Balustrade','Beam','BirdControlDevice',	'Bulkhead',	'Canopy',	'CanopyFrame',	'Cap',	'Catwalk',	'Chimney',	'Cladding',	'Coating',	'CoilingDoor',	'CoilingGrille',	'ColdStorageDoor',	'Column',		'ConductorHead',	'ConstructionSupplementary',	'Coping',	'Cornice',	'CounterFlashing',	'Cupola',	'Deck',	'DecorativeMetal',	'DetentionDoor',	'Door',	'DoorFrame',	'DoorGlazing',	'DoorLouver',	'DoorSupplementary',	'DownSpout',	'EIFS',	'EntranceDoor',		'EquipmentScreen',	'ExpansionJoint',	'ExteriorCeiling',	'ExteriorSoffit',	'FabricatedWallAssembly',	'FacedPanel',	'Fence',	'FireEscape',	'FixedScreen',	'FixedWindow',	'Flagpole',	'Flashing',	'FoldingGrille',	'FrameSkylight',	'Framing',	'Girder',	'Glass',	'GlassBlock',	'GlassUnitMasonry',	'Glazing',	'Grating',	'GravelStopFascia',	'Grille',	'Grouting',	'Gutter',	'GypsumBoard',	'HangerDoor',	'HoriOpeningSupplementary',	'HorizontalOpening',	'IndustrialDoor',	'Insulation',	'JointSealant',	'Joist',	'Ladder',	'LightFixture',	'Lintel',	'Louver',	'LouveredEnclosure',	'LowSlopeRoof',	'ManufacturedMasonry',	'Marquee',	'MasonryVeneer',		'MetalWalkway',	'Mullion',	'OpeningProtection',	'OperatingWindow',	'OrnamentalWoodwork',	'OverSizeDoor',	'OverheadExteriorEnclosure',	'PanelDoor',	'Parapet',	'Pediment',	'Plaster',	'PlasterBoard',	'Polygon',	'Portico',	'PressureResistantDoor',	'RadiationResistantGlazing',	'RadiationShieldingDoor',	'RadioFrequencyInterferenceShieldingDoor',	'Railing',	'RainWaterManagement',	'Ramp',	'ReliefVent',	'RevolvingDoor',	'RidgeVent',	'Roof',	'RoofAccessory',	'RoofAppurtenance',	'RoofConstructionSupplementary',	'RoofCurb',	'RoofGravel',	'RoofHatch',	'RoofLadder',	'RoofPanel',	'RoofPaver',	'RoofShake',	'RoofShingle',	'RoofSlate',	'RoofSpecialty',	'RoofTile',	'RoofWalkway',	'RoofWindow',	'Roofing',	'RoofingBallast',	'RoofingCover',	'RoofingSupplementary',	'Scupper',	'Sealant',	'SecurityDoor',	'SecurityGate',	'Setback',	'Sheathing',	'SheetMetalRoofing',	'Shutter',	'Siding',	'Signage',	'Sill',	'SkylightProtection',	'SkylightScreen',	'Slab',	'SlidingGlassDoor',	'SlidingStoreFront',	'SmokeVent',	'SnowGuard',	'Soffit',		'SoundControlDoor',	'Spandrel',	'SpecialFunctionDoor',	'SpecialFunctionWindow',	'Spire',	'Stair',	'StairNosing',	'StairTread',	'SteepSlopeRoofing',	'Steeple',	'StoneUnit',	'StoreFront',	'StormPanel',	'StormWindow',	'StructuralFrame',	'StructuralPanel',	'StructuralPlastic',	'Stucco',	'SubstrateBoard',	'SunControlDevice',	'Superstructure',	'Terrace',	'Topping',	'Tower',	'TrafficBearingHoriEnclosure',	'TrafficDoor',	'Trim',	'Truss',	'UnitMasonry',	'UnitSkylight',	'UtilityDoor',	'Vent',	'VerticalEnclosure',	'Wall',	'WallAppurtenance',	'WallInteriorSkin',	'WallOpeningSupplementaryComponent',	'WallPanel',	'WallSupplementaryComponent',	'WallVeneer',	'WeatherBarrier',	'WeatherVane',	'Window',	'WindowFrame',	'WindowJamb',	'WindowPanel',	'WindowScreen',	'WindowWall']
#if I do for all classes, some error occurs, so I cannot seem to do it for all classes.
#in particular, I must exclude the 'FacadeComponent' class (as it would be a self reference)


while True:
    class_name = dataset.readline().strip()
    print(class_name)
    if class_name == '':
        break
    exec_str = class_name + " = type(\"" + class_name + "\", (FacadeComponent, ), {\"__init__\": comp_init})"
    exec(exec_str)


"""
for i in dataset:

    print(i)

    exec_str = i + " = type(\"" + i + "\", (FacadeComponent, ), {\"__init__\": comp_init})"

    #print(exec_str)

    exec(exec_str)

"""

###start superstructure.py

"""
class Roof(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof'
"""



"""
class Superstructure(FacadeComponent):
    "TODO: implement superstructure class"

    def __init__(self, id, compType, materials, comPlane, subcomponents=[], safeCon=None):
        super().__init__(compType, materials, comPlane, subcomponents=[], safeCon=None)
        self.compType = 'superstructure'





class Stair(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'stair'


class ConstructionSupplementary(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'construction supplymentary'


class StructuralFrame(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof structural frame'


class Deck(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'deck'


class Slab(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'slab'


class Sheathing(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'sheathing'


class BalconyFloor(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'balcony floor'


class Ramp(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'ramp'


class Canopy(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'canopy'


class RoofConstructionSupplementary(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof construction supplementary'


class Soffit(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'soffit'


class Railing(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'railing'


class FireEscape(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'fire escape'


class MetalWalkway(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'metal walkway'


class Ladder(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'ladder'


class Column(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'column'


class Girder(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'girder'


class Beam(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.comType = 'beam'


class Joist(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'joist'


class Truss(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'truss'


class Topping(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'topping'


class StructuralPanel(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'structural panel'


class GlassUnitMasonry(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'glass unit masonry'


class ExteriorCeiling(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'exterior ceiling'


class StructuralPlastic(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'structural plastic'


class StairTread(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'stair tread'


class StairNosing(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'stair nosing'


class PlasterBoard(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'plaster board'


class GypsumBoard(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'gypsum board'


class Catwalk(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.comType = 'catwalk'


class Grating(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'grating'


###end superstructure.py


###start exterior_vertical_enclosure.py


from facade_component import FacadeComponent
from shapely.geometry import Polygon
from material_enum import *


# Store the hierarchy of facade components
# group the instances based on the structure

class VerticalEnclosure(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'vertical enclosure'


class Wall(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'exterior wall'


"""

class Window(FacadeComponent):
    # TODO: modify the id
    def __init__(self, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'exterior window'
    
"""


exec("Window = type(\"Window\", (FacadeComponent, ), {\"__init__\": comp_init})")




class WallAppurtenance(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'exterior wall appurtenance'


class WallVeneer(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'wall veneer'


class WallPanel(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'wall panel'


class UnitMasonry(FacadeComponent):
    '''

    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'unit masonry'


class MasonryVeneer(FacadeComponent):
    '''
    Masonry veneer walls consist of a single non-structural external layer of masonry, typically made of brick, stone or manufactured stone.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'masonry veneer'


class ManufacturedMasonry(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'manufactured masonry'


class Cladding(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'cladding'


class StoneUnit(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'stone unit'
        self.materials = [stone]


class GlassBlock(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'glass block'
        self.materials = [glass]


# class FinishCarpentry(FacadeComponent):
'''
NOT a component, it's a construction work. Finish carpentry encompasses all work done inside a house after framing, sheathing, 
wiring, plumbing, insulation and drywall have been installed. 
'''


#     def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
#         super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
#         self.compType = 'finish carpentry'
#         self.materials = ['wood']

class EIFS(FacadeComponent):
    '''
    Exterior insulation and finish systems
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'EIFS'


class FacedPanel(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'faced panel'


class Siding(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'siding'


class Plaster(FacadeComponent):
    '''
    a gypsum plaster with certain impurities present or added in the calcining process mixed with sand or wood fiber and water to form a mortar for plastering interior surfaces
— called also hard wall plaster, patent plaster
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'plaster'
        self.materials = [plaster]


class Stucco(FacadeComponent):
    '''
    Stucco, or portland cement plaster, is a versatile facing material that can be applied to flat or curved surfaces either inside or outside any building or structure.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'stucco'
        self.materials = [stucco]


class Coating(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'coating'


class Framing(FacadeComponent):
    '''
    wood framing, structural metal stud framing
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'framing'


class WallInteriorSkin(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'wall interior skin'


class PlasterBoard(WallInteriorSkin):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'plaster board'
        self.materials = [plaster]


class GypsumBoard(WallInteriorSkin):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'gypsum board'
        self.materials = [gypsum]


class FabricatedWallAssembly(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'fabricated wall assembly'


class Mullion(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'mullion'
        self.materials = [metal]


class Glass(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'glass'
        self.materials = [glass]


class Parapet(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'parapet'


class EquipmentScreen(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'equipment screen'


class LouveredEnclosure(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'louvered equipment enclosure'


class WallSupplementaryComponent(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'wall supplementary component'


class Grouting(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'grouting'


class ExpansionJoint(FacadeComponent):
    '''
    In building construction, an expansion joint is a mid-structure separation designed to
    relieve stress on building materials caused by building movement.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'expansion joint'


class WeatherBarrier(FacadeComponent):
    '''
    Weather-resistive barriers are a part of exterior wall systems that protect building materials
    from exterior water penetration. They perform like a shell for buildings—liquid water that has penetrated
    the exterior finish does not pass through, yet water vapor can escape.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'weather barrier'


class Insulation(FacadeComponent):
    '''
    Building insulation is any object in a building used as insulation for thermal management.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'insulation'


class WallOpeningSupplementaryComponent(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'wall opening supplementary component'


class Lintel(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'lintel'


class Sealant(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'sealant'


class Flashing(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'flashing'


class Sill(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'sill'


class Cap(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'cap'


class OperatingWindow(Window):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'operating window'


class WindowScreen(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'window screen'


class StormWindow(Window):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'storm window'


class WindowFrame(FacadeComponent):
    def __init__(self, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'window frame'


class WindowJamb(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'window jamb'


class WindowPanel(FacadeComponent):
    def __init__(self, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'window panel'


class FixedWindow(Window):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'fixed window'


class Glazing(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'glazing'


class WindowWall(Window):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'window wall'


class StoreFront(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'store front'


class SpecialFunctionWindow(Window):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'special function window'


class Door(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'door'


class EntranceDoor(Door):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'entrance door'


class SlidingGlassDoor(EntranceDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'sliding glass door'


class RevolvingDoor(EntranceDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'revolving door'


class BalancedDoor(EntranceDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'balanced door'


class SlidingStoreFront(EntranceDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'sliding storefront'


class AllGlassEntrance(EntranceDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'all-glass entrance'


class AutomaticEntrance(EntranceDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'automatic entrance'


class UtilityDoor(Door):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'utility door'


class OverSizeDoor(Door):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'oversize door'


class CoilingDoor(OverSizeDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'coiling door'


class PanelDoor(OverSizeDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'panel door'


class HangerDoor(OverSizeDoor):
    '''
    aircraft hanger doors
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'hanger door'


class SpecialFunctionDoor(Door):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'special function door'


class ColdStorageDoor(SpecialFunctionDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'cold storage door'


class IndustrialDoor(SpecialFunctionDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'industrial door'


class RadioFrequencyInterferenceShieldingDoor(SpecialFunctionDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'radio frequency interference shielding door'


class RadiationShieldingDoor(SpecialFunctionDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'radiation shielding door'


class RadiationResistantGlazing(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'radiation resistant glazing'
        self.materials = [glass]


class SecurityDoor(SpecialFunctionDoor):
    '''
    Security doors typically come in two basic types.
    One type is an openwork steel door, which looks like wrought iron and has a tempered glass back panel.
    The second type looks like a regular wooden or fiberglass door, but is actually made of steel with sturdy side fixings.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'security door'


class BallisticsResistantGlazing(FacadeComponent):
    '''
    bulletproof glass
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'ballistics resostant glazing'
        self.materials = [glass]


class DetentionDoor(SpecialFunctionDoor):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'detention door'
        self.materials = [metal]


class SoundControlDoor(SpecialFunctionDoor):
    '''
    sound proof door
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'sound control door'


class TrafficDoor(SpecialFunctionDoor):
    '''
    Traffic Doors also known as swing doors, impact doors and double acting doors,
    are a cost-effective solution for fast and efficient, two-way movement through an opening where visual,
    sound and environmental barriers are required.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'traffic door'


class PressureResistantDoor(SpecialFunctionDoor):
    '''
    Pressure resistant/relief are available in Vertical Lift, Sliding, Turnover or Hinged applications.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'pressure resistant door'


class Grille(FacadeComponent):
    '''
    Grille: a network of metal, wooden, or plastic bars that acts as a barrier or screen.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'grille'


class CoilingGrille(Grille):
    '''
    The coiling grilles and security gates are available in brick or straight patterns.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'coiling grille'
        self.materials = [metal]


class FoldingGrille(Grille):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'folding grille'
        self.materials = [metal]


class SecurityGate(Door):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'security gate'
        self.materials = [metal]


class DoorSupplementary(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'door supplementary'


class DoorFrame(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'door frame'


class DoorGlazing(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'door glazing'


class DoorLouver(FacadeComponent):
    '''
    Louvers (door vents) can be added to virtually any commercial steel or wood door.
    Louvers provide air ventilation between rooms or inside of closets.
    Louvered doors help ventilate rooms when closed while still providing privacy and security.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'door louver'


class Louver(WallAppurtenance):
    '''
    A louver is a ventilation product that allows air to pass through it
    while keeping out unwanted elements such as water, dirt, and debris.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'louver'


class Vent(WallAppurtenance):
    '''
    The Register Vents cover the wall opening where the ducts come in.
    The air will be pushed through the ducts by a fan. They are supposed to protect the duct from trapping loose items and adjust the flow of air.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'vent'


class FixedScreen(WallAppurtenance):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'fixed screen'


class DecorativeMetal(WallAppurtenance):
    '''
    Decorative metal can be defined as metal that provides architectural decoration but has no structural value.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'decorative metal'
        self.materials = [metal]


class OrnamentalWoodwork(WallAppurtenance):
    '''
    Ornamental woodwork includes any type of custom woodwork that is shop fabricated for specific applications.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'ornamental woodwork'
        self.materials = [wood]


class OpeningProtection(WallAppurtenance):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'opening protection'


class Awning(OpeningProtection):
    '''
    An awning or overhang is a secondary covering attached to the exterior wall of a building.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'awning'


class Shutter(OpeningProtection):
    '''
    A window shutter is a solid and stable window covering usually consisting of a frame of vertical stiles and horizontal rails (top, centre and bottom).
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'shutter'
        self.materials = [wood, glass]


class SunControlDevice(OpeningProtection):
    '''
    Shading devices on the external side of the window include shutters, awnings, canopies, blinds, and projecting horizontal and vertical fins.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'sun control device'


class StormPanel(OpeningProtection):
    '''
    They are solid coverings that can be placed in front of your windows right before a storm rolls in, and taken down after it passes.
    Typically, storm panels are made out of steel, aluminum or a clear/white plastic that’s designed to withstand mild impact,
    eliminating glass breakage in the event of storm damage.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'storm panel'
        self.materials = [metal, plastic]


class BalconyWall(WallAppurtenance):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'balcony wall'


class Railing(WallAppurtenance):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'railing'
        self.materials = [metal]


class BirdControlDevice(WallAppurtenance):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'bird control device'


class AirConditioningUnit(WallAppurtenance):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'air conditioning unit'


class Antenna(WallAppurtenance):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'antenna'


class Marquee(WallAppurtenance):
    '''
    A sign usually over the entrance of a theater or arena that displays the names of
    featured attractions and principal performers
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'marquee'


class Cornice(WallAppurtenance):
    '''
    In architecture, a cornice is generally any horizontal decorative moulding
    that crowns a building or furniture element—for example, the cornice over a door or window, around the top edge of a pedestal,
    or along the top of an interior wall.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'cornice'


class LightFixture(WallAppurtenance):
    '''
    a lighting fixture is part of a light that is attached to the wall or ceiling where you put the light bulb or other lighting element,
    and which cannot be easily removed.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'light fixture'


class Pediment(WallAppurtenance):
    '''
    pediment, in architecture, triangular gable forming the end of the roof slope over a portico
    (the area, with a roof supported by columns, leading to the entrance of a building);
    or a similar form used decoratively over a doorway or window. The pediment was the crowning feature of the Greek temple front.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'pediment'


class Baluster(WallAppurtenance):
    '''
    a short pillar or column, typically decorative in design,
    in a series supporting a rail or coping. Common materials used are wood, stone, and less frequently metal and ceramic.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'baluster'
        self.materials = [wood, stone]


class Balustrade(WallAppurtenance):
    '''
    a railing supported by balusters, especially an ornamental parapet on a balcony, bridge, or terrace.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'balustrade'


class Portico(WallAppurtenance):
    '''
     portico is a porch leading to the entrance of a building, or extended as a colonnade, with a roof structure over a walkway,
     supported by columns or enclosed by walls.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'portico'


class Signage(WallAppurtenance):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'signage'


class Spandrel(WallAppurtenance):
    '''
     spandrel is a roughly triangular space, usually found in pairs, between the top of an arch and a rectangular frame;
     between the tops of two adjacent arches or one of the four spaces between a circle within a square.
     They are frequently filled with decorative elements.
    '''

    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'spandrel'


class Fence(WallAppurtenance):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'fence'




###end exterior_vertical_closure.py




###start exterior_horizontal_enclosure.py



#from _typeshed import Self
from facade_component import FacadeComponent
from shapely.geometry import Polygon
from material_enum import *



class Roofing(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof'

class RoofAppurtenance(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof appurtenance'

class TrafficBearingHoriEnclosure(FacadeComponent):
    '''
    Horizontal enclosures that are also traffic bearing. Includes Horizontal Enclosure Supplementary Components as
appropriate.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'traffic bearing horizontal enclosure'

class HorizontalOpening(FacadeComponent):
     def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
         super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
         self.compType = 'horizontal opening'

class OverheadExteriorEnclosure(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'overhead exterior enclosure'

class SteepSlopeRoofing(Roofing):
    '''
    Steep Slope: 21:12 and higher
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'steep slope roofing'

class RoofPanel(Roofing):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof panel'

class RoofTile(Roofing):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof tile'

class SheetMetalRoofing(Roofing):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'sheet metal roofing'
        self.materials = [metal]

class RoofShingle(Roofing):
    '''
    Roof shingles are a roof covering consisting of individual overlapping elements.
    These elements are typically flat, rectangular shapes laid in courses from the bottom edge of the roof up,
    with each successive course overlapping the joints below.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof shingle'

class RoofShake(Roofing):
    '''
    A shake is typically described as a wooden shingle that is made from split logs.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof shake'
        self.materials = [wood]

class RoofSlate(Roofing):
    '''
    A slate roof is a premium roof system made primarily out of natural slate tiles and other slate roofing materials
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof slate'
        self.materials = [stone]

class RainWaterManagement(RoofAppurtenance):
    '''
    ainwater harvesting system, also called rainwater collection system or rainwater catchment system,
    technology that collects and stores rainwater for human use.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'rain water management'

class LowSlopeRoof(Roofing):
    '''
    Low Slope: 2:12-4:12
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'low slope roof'

class RoofingCover(Roofing):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roofing cover'

class RoofingBallast(RoofingCover):
    '''
    A ballasted roof means that the roof membrane is not anchored or adhered in any way to the decking material.
    It is, however, ballasted, generally with gravel.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roofing ballast'

class RoofGravel(RoofingBallast):
    '''
     A layer of gravel, or small stones, is applied on top of the final coating of asphalt to protect the roof from the elements,
     including ultraviolet (UV) rays and hail.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof gravel'

class RoofPaver(RoofingBallast):
    '''
    Pavers is a planking system installed to protect the roof's surface while providing access for utility maintenance.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof paver'

class Canopy(FacadeComponent):
    '''
    A canopy is an overhead roof structure that has open sides.
    Canopies are typically intended to provide shelter from the rain or sun,
    but may also be used for decorative purposes,
    or to give emphasis to a route or part of a building.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'canopy'
        self.materials = [glass, metal]

class CanopyFrame(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'canopy frame'

class ExteriorCeiling(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'exterior ceiling'
class ExteriorSoffit(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'exterior soffit'

class RoofingSupplementary(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roofing supplementary'

class Flashing(RoofingSupplementary):
    '''
    Roof flashing is a thin metal material that roofers install to direct water away from certain areas (walls, chimneys, roof valleys) of your roof.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'flashing'

class SubstrateBoard(RoofingSupplementary):
    '''
    Substrate boards on wood decks (plywood, OSB, planking) are used to increase fire resistance,
    prevent adhesive from dripping into the interior, provide a clean and acceptable surface onto which an air or vapor retarder can be adhered,
    or as a surface onto which the insulation can be adhered.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'substrate board'

class Trim(RoofingSupplementary):
    '''
    Trim is what seals joints and drip edges, and keeps moisture from penetrating your home.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'trim'


class CounterFlashing(RoofingSupplementary):
    '''
    a strip of sheet metal in the form of an inverted L built into
    a vertical wall of masonry and bent down over the flashing to make it watertight.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'counterflashing'

class GravelStopFascia(RoofingSupplementary):
    '''
    a metal flashing shape attached to roof structure to protect the roof edge against water penetration
    and to contain a built-up roof and prevent its gravel surface from falling over the roof edge.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'gravel stop'
        self.materials = [metal]

class Coping(RoofingSupplementary):
    '''
    Wall coping is a protective cap or cover on a wall that prevents water infiltration from above.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'coping'

class RoofAccessory(RoofAppurtenance):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof accessory'

class RoofLadder(RoofAccessory):
    '''
    A roofing ladder is simply an extension ladder that has been securely attached to the ridge of a sloped roof
    to allow a roofer to work from an angle (though, no more than 75 degrees) on the roof.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof ladder'
        self.materials = [metal]

class RoofCurb(RoofAccessory):
    '''
    Rooftop curbs are raised metal frames designed for mounting structures safely to your roof.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof curb'

class RoofWalkway(RoofAccessory):
    '''
    Basically, a rooftop walkway system is a pathway that allows people to traverse the roof in a safe manner.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof walkway'

class RidgeVent(RoofAccessory):
    '''
     ridge vent is an air exhaust vent installed on the peak of a roof.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'ridge vent'

class ReliefVent(RoofAccessory):
    '''
    Relief vent means an auxiliary vent which permits additional circulation of air in or between drainage and vent systems.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'relief vent'

class SnowGuard(RoofAccessory):
    '''
    Snow guards are rooftop devices that allow snow and ice to drop off in small amounts
    or allow snow and ice to melt completely before falling to the ground.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'snow guard'

class RoofSpecialty(RoofAppurtenance):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof specialty'

class Cupola(RoofSpecialty):
    '''
    In architecture, a cupola is a relatively small, most often dome-like, tall structure on top of a building.
    Often used to provide a lookout or to admit light and air, it usually crowns a larger roof or dome.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'cupola'

class Spire(RoofSpecialty):
    '''
     decorative caps to the point or end of a roof
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'Spire'

class Steeple(RoofSpecialty):
    '''
    a steeple is a tall tower on a building,
    topped by a spire and often incorporating a belfry and other components.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'steeple'

class WeatherVane(RoofSpecialty):
    '''
    A wind vane, weather vane, or weathercock is an instrument used for showing the direction of the wind.
    It is typically used as an architectural ornament to the highest point of a building.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'weather vane'

class Tower(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.comType = 'tower'

class Setback(FacadeComponent):
    '''
    A setback, in the specific sense of a step-back,
    is a step-like form of a wall or other building frontage, also termed a recession or recessed storey.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'setback'

class Terrace(FacadeComponent):
    '''
    A terrace is an external, raised, open, flat area in either a landscape (such as a park or garden) near a building,
    or as a roof terrace on a flat roof.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'terrace'

class Flagpole(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'flagpole'

class ConductorHead(RainWaterManagement):
    '''
    Collector Heads, also know as Conductor Heads, are a decorative feature for roof drainage.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'conductor head'

class Gutter(RainWaterManagement):
    '''
     a component of a water discharge system for a building
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'gutter'

class Scupper(RainWaterManagement):
    '''
    A roof scupper is a drainage system for flat roofs that can't rely on sloping to naturally move water through a gutter system.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'scupper'

class DownSpout(RainWaterManagement):
    '''
    the gutter downspout is the vertical pipe attachment that moves water out of your gutters and away from your building to empty safely into a separate drainage system.
    '''
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'downspout'

class RoofWindow(HorizontalOpening):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof window'

class UnitSkylight(HorizontalOpening):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'unit skylight'

class FrameSkylight(HorizontalOpening):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'frame skylight'

class SkylightScreen(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'skylight screen'

class SkylightProtection(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'skylight protection'

class RoofHatch(HorizontalOpening):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof hatch'

class SmokeVent(HorizontalOpening):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'smoke vent'

class Chimney(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'chimney'

class HoriOpeningSupplementary(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'horizontal opening supplementary component'

class Glazing(HoriOpeningSupplementary):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'glazing'

class JointSealant(HoriOpeningSupplementary):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'joint sealant'

class ExteriorCeiling(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'exterior ceiling'

class Bulkhead(OverheadExteriorEnclosure):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'bulkhead'




###end exterior_horizontal_closure.py


"""