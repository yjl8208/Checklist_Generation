from defect import Defect

class SurfaceClrOrTxtrChange(Defect):
    #Surface color or texture change property set
    def __init__(self, id, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(id, defectType, defectPlane, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        self.propertySet = propertySet

class Leakage(SurfaceClrOrTxtrChange):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        '''
        Water stains on walls, organic growth, difference in coloring.
        '''
        #leakage = moisture
        self.defectType = 'leakage'
        self.appMaterials = ['brick masonry', 'stone', 'concrete', 'terra cotta', 'metal', 'cast iron']
        #boolean value of whether organic growth was observed with the leakage
        self.organiceGrowth = None

    def setOrganicGrowth(self, organicGrowth):
        self.organiceGrowth = organicGrowth
    def getOrganicGrowth(self):
        return self.organiceGrowth
    
class Soiling(SurfaceClrOrTxtrChange):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        '''
        Alteration, change in color due to deposits of materials. Film, very thin layer of deposit.
        '''
        #soiling = stain
        self.defectType = 'soiling'
        self.appMaterials = ['brick masonry', 'stone', 'concrete', 'terra cotta', 'metal', 'cast iron', 'glass']
        self.appComps = ['brick veneer', 'flashing', 'brick masonry unit', 'fixture', 'sheet metal', 'glass panel', 'window']
        #area affected in sqft
        self.areaAffected = None
        #SoilingMaterial is a subclass of material enumeration class
        #materials is a list of soiling materials instances
        self.materials = []
        #Boolean of whether the soiling exists near the flashing
        self.presenceOfFlashing = None
        #Boolean of whether rusted steel or iron fixture was observed
        self.presenceOfRustFixture = None

    def setAreaAffected(self, areaAffected):
        self.areaAffected = areaAffected
    def getAreaAffected(self):
        return self.areaAffected
    
    def setSoilingMaterial(self, material):
        material.assign(material, self)
    def getSoilingMaterial(self):
        return self.materials
    
    def setPresenceOfFlashing(self, flashing):
        self.presenceOfFlashing = flashing
    def getPresenceOfFlashing(self):
        return self.presenceOfFlashing

    def setPresenceOfRustFixture(self, fixture):
        self.presenceOfRustFixture = fixture
    def getPresenceOfFlashing(self):
        return self.presenceOfRustFixture

class LimeRun(SurfaceClrOrTxtrChange):
    def __init__(self, defectType, defectPlane, propertySet, possCause='', suggestRepair='', hasPropertySet=True):
        super().__init__(defectType, defectPlane, propertySet, possCause=possCause, suggestRepair=suggestRepair, hasPropertySet=hasPropertySet)
        '''
        Crust building up at mortar joints.
        '''
        self.defectType = 'lime run'
        self.appMaterials = ['brick masonry']
        self.appComps = ['mortar joint']


    
    