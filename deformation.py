from defect import Defect

#subclass for defect 
class Deformation(Defect):
    #Deformation defect has propertySet
    def __init__(self, id, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(id, defectType, defectPlane, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.propertySet = propertySet


class Bowing(Deformation):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        '''
        Inward or outward displacement of middle section of wall over large span.
        '''
        self.defectType = 'bowing'
        self.appMaterials = ['brick masonry', 'stone', 'concrete', 'terra cotta', 'metal', 'cast iron']
        self.appComps = ['brick veneer', 'wall', 'marbel panel', 'concrete panel']
        #Bowing direction: inward or outward
        self.direction = None

    def setDirection(self, direction):
        self.direction = direction
    def getDirection(self):
        return self.direction  

class Bulging(Deformation):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        '''
        Lack of verticality of wall.
        '''
        self.defecType = 'bulging'
        self.appMaterials = ['brick masonry', 'concrete', 'terra cotta', 'metal', 'cast iron', 'glass']
        self.appComps = ['bearing masonry', 'trasnitional facade', 'brick veneer', 'parapet', 'roof', 'concrete panel', 'glass panel', 'window']

        #direction of crack: horizontal, vertical, or diagnal
        self.directionOfCrack = None
        #boolean value for whether the bulding is on parapet
        self.onParapet = None
        #boolean value for wheather parapet leaning exists 
        self.parapetLeaning = None
        #shifting direction: horizontal(left/right or forward/backward) or vertical (up/down)
        self.shiftingDirection = None 

    def setDirectionOfCrack(self, directionEnum):
        self.directionOfCrack = directionEnum
    def getDirectionOfCrack(self):
        return self.directionOfCrack

    def setOnparapet(self, onParapet):     
        self.onParapet = onParapet
    def getOnParapet(self):
        return self.onParapet
    
    def setParapetLeaning(self, parapetLeaning):
        self.parapetLeaning = parapetLeaning
    def getParapetLeaning(self):
        return self.parapetLeaning

class RollingBlock(Deformation):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        '''
        Face of brick veneer ubdulations along a vertical plane
        '''
        self.defectType = 'rolling block'
        self.appMaterials = ['brick masonry', ]
        self.appComponents = ['brick veneer', ]

class Displacement(Deformation):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        '''
        Units shifted out of their as-built position in a certain direction
        '''
        self.defectType = 'displacement'
        self.appMaterials = ['brick masonry', 'stone', 'concrete', 'terra cotta', 'metal', 'cast iron']
        self.appComps = ['brick veneer', 'stone panel', 'concrete panel']
        self.presenceOfWeepHole = None
        self.seperationAlongJoint = None
        #shifting direction: horizontal(left/right or forward/backward) or vertical (up/down)
        self.shiftingDirection = None 

    def setPresenceOfWeepHole(self, presenceOfWeepHole):
        self.presenceOfWeepHole = presenceOfWeepHole
    def getPresenceOfWeepHole(self):
        return self.presenceOfWeepHole
    def setSeperationAlongJoint(self, seperationALongJoint):
        self.seperationAlongJoint = seperationALongJoint
    def getSeperationAlongJoint(self):
        return self.seperationAlongJoint

    def setShiftingDirection(self, shiftingDirection):
        self.shiftingDirection = shiftingDirection
    def getShiftingDirection(self):
        return self.shiftingDirection
    
class Leaning(Deformation):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        '''
        Out of plumb positions
        '''
        self.defectType = 'leaning'
        self.appMaterials = ['stone', 'concrete', 'terra cotta', 'metal', 'cast iron']

class Slippage(Deformation):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        '''
        Individual stone replacement
        '''
        self.defectType = 'slippage'
        self.appMaterials = ['concrete']
        self.appComps = ['concrete panel']

