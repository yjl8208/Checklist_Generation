from facade_component import FacadeComponent
from shapely.geometry import Polygon
from material_enum import *
#Store the hierarchy of facade components
#group the instances based on the structure

class VerticalEnclosure(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'vertical enclosure'

class Wall(FacadeComponent):
    def __init__(self, id, compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(id, compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'exterior wall'

class Window(FacadeComponent):
    #TODO: modify the id
    def __init__(self,  compType, materials, comPlane, subcomponents=..., safeCon=None):
        super().__init__(compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
        self.compType = 'exterior window'

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

class  EIFS(FacadeComponent):
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
        super().__init__( compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)
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
        self. compType = 'balcony wall'

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




