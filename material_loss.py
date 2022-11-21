from .defect import Defect

#Subclass for defect
class MaterialLoss(Defect):
    
    #material loss defect has propertySet
    def __init__(self, id, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(id, defectType, defectPlane, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.propertySet = propertySet

        #affected area in sqft/square inch
        'TODO: measurement unit enumeration'
        'TODO: add unit, area should be a class'
        self.affectedArea = None
      

    def setAffectedArea(self, area):
        self.affectedArea = area
    def getAffectedArea(self):
        return self.affectedArea

    
class Crazing(MaterialLoss):
    
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'crazing'
        self.appMaterials = ['brick masonry']
        self.appComps = ['wall']
    
class Crack(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'crack'
        self.appMaterials = ['brick masonry', 'concrete', 'stone', 'terra cotta', 'metal', 'cast iron', 'brownstone', 'glass', 'stucco', 'brick veneer', 'slate']
        

class Spall(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'spall'
        self.appMaterials = ['brick masonry', 'stone', 'concrete', 'terra cotta', 'metal', 'cast iron']

        self.condition = None

    def setCondition(self, conditionEnum):
        'TODO: set condition enumeration class for defect property set'
        self.condition = conditionEnum
    def getCondition(self):
        return self.condition
        
class Errosion(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        #erosion = pitting, abrasion
        'TODO: map several different defect names to the same defect type'
        self.defectType = 'errosion'
        self.appMaterials = ['brick masonry', 'mortar joint', 'stone', 'wood', 'metal', 'cast iron']
        self.appComps = ['sheet metal']
        #defect properties
        self.severity = None

    def setSeverity(self, severityEnum):
        'TODO: set severity enumeration class for defect property set'
        self.severity = severityEnum
    def getSeverity(self):
        return self.severity


class CoatingFailed(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        #coating failed = peeling, delamination, scaling, exfoliation, topping, blistering, wrinkling, checking, alligatoring, chalking 
        self.defectType = 'coating failed'
        self.appMaterials = ['brick masonry', 'stone', 'concrete', 'brownstone', 'stucco', 'terra cotta', 'metal', 'cast iron']
        self.appComps = ['sheet metal']

class Coving(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        #coving = gap, open hole
        self.defectType = 'coving'
        self.appMaterials = ['brick masonry']

class Missing(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'missing'
        self.appMaterials = ['brick masonry','stone', 'concrete', 'terra cotta', 'metal', 'cast iron', 'glass']
        self.appComps = ['mortar joint', 'brick unit']

class RepairFailure(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'repair '
        self.appMaterials = ['brick masonry', 'stone', 'concrete', 'terra cotta', 'metal', 'cast iron', 'brownstone', 'glass']
        self.appComps = ['joint sealant', 'dutchman', 'mortar joint', 'sheet metal']
        #length： in linear ft
        self.length = None

    def setLength(self, length):
        self.length = length
    def getLength(self):
        return self.length
        

class Hollow(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'hollow'
        self.appMaterials = ['brick masonry', 'stone', 'concrete', 'terra cotta']

class Loose(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'loose'
        self.appMaterials = ['brick masonry', 'stone', 'concrete', 'terra cotta', 'metal', 'cast iron', 'glass']

class FasternerFailed(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'fastener failed'
        self.appMaterials = ['brick masonry', 'slate', 'wood', 'sheet metal', 'architectural metal']
        self.length = None

    def setLength(self, length):
        self.length = length
    def getLength(self):
        return self.length

class LathFailed(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'lath failed'
        self.appMaterials = ['brick masonry', 'plaster']

class Checking(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'checking'
        self.appMaterials = ['brick masonry', 'wood']

class GypsumCrust(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'gypsum crust'
        self.appMaterials = ['stone', 'gypsum'] 
        
class Opening(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        #opening = gap, hole, sagging
        self.defectType = 'opening'
        self.appMaterials = ['stone', 'brick masonry', 'terra cotta', 'brownstone']
        self.appComps = ['mortar joint', 'joint']

class SurfaceDecay(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        '''
        Shallow loss of material, typically at the edges of a masonry unit. Separation of layers along natural bedding planes, 
        resulting in loss of material at the outer surface of the unit or voids within the unit.
        '''
        #decay = flaking, delamination, exfoliated, sugaring, surface chip, crumbling
        self.defectType = 'surface decay'
        self.appMaterials = ['stone', 'terra cotta', 'brownstone']

class Broken(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'broken'
        self.appMaterials = ['concrete']
        self.appComps = ['concrete masonry unit', 'terra cotta unit']

class ExpansionJoint(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'expansion joint'
        self.appMaterials = ['concrete', 'terra cotta', 'metal', 'cast iron']
        self.appComps = ['veneer']

class HoneyComb(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'honey comb'
        self.appMaterials = ['concrete']

class LossOfGlaze(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'loss of glaze'
        self.appMaterials = ['terra cotta']
        #depth in 1/8" increments
        self.depth = None

    def setDepth(self, depth):
        self.depth = depth
    def getDepth(self):
        return self.depth

class MetalDemage(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        #damage = bent, dented, torn, punctured
        self.defectType = 'metal damage'
        self.appMaterials = ['metal', 'sheet metal', 'architectural metal']
        #length in linear ft
        self.length = None
        #diameter in inches
        self.diametrer

    def setLength(self, length):
        self.length = length
    def getLength(self):
        return self.length
    def setDiameter(self, diameter):
        self.diameter = diameter
    def getDiameter(self):
        return self.diameter

class PuttyFailed(MaterialLoss):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.defectType = 'putty failed'
        self.appMaterials = ['glass']
        'TODO: setup components so that based on one appComps, run a routine to add all related components to this list'
        self.appComps = ['glass panel']


        