from facade_component import FacadeComponent
from shapely.geometry import Polygon
#Store the hierarchy of facade components
#group the instances based on the structure






def comp_init(self, id, compType, materials, comPlane, subcomponents=[], safeCon=None):
    super().__init__(compType, materials, comPlane, subcomponents=[], safeCon=None)
    self.compType = 'floor'

exec("Floor = type(\"Floor\", (FacadeComponent, ), {\"__init__\": comp_init})")





#source: https://python-course.eu/oop/dynamically-creating-classes-with-type.php
#source: https://www.geeksforgeeks.org/create-classes-dynamically-in-python




"""
class Floor(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=[], safeCon=None):
        super().__init__(compType, materials, comPlane, subcomponents=[], safeCon=None)
        self.compType = 'floor'
"""

class Superstructure(FacadeComponent):
    "TODO: implement superstructure class"
    def __init__(self, id, compType, materials, comPlane, subcomponents=[], safeCon=None):
        super().__init__(compType, materials, comPlane, subcomponents=[], safeCon=None)
        self.compType = 'superstructure'



class Roof(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'roof'

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
        
