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