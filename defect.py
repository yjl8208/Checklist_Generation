#Defect Class

class Defect:

    
    def __init__(self, id, defectType, defectPlane, possCause='', suggestRepair='', hasPropertySet=False):
        """TODO: initiate unique ID for instances. """
        self.id = id
        "TODO: DefectType Class"
        self.defectType=defectType
        self.defectPlane = defectPlane
        "TODO: possibleCause class?"
        self.possCause=possCause
        "#TODO: suggestedRepair class"
        self.suggestRepair=suggestRepair
        'TODO: propertySet class?'
        self.hasPropertySet = hasPropertySet
        'TODO: add relatedDefect attribute'
        # defectID = None
        self.associatedComponents = {}
        self.appComps = []
        self.appMaterials = []
        'TODO: need measurement? measurment unit?'
        self.reference = None
        
    def getDefectID(self):
        return self.id
        
    def assignToComponent(self, facadeComponent):
        "TODO: update with object ID representation if possible"
        facadeComponent.associatedDefects[self.defectType].append(self)
        self.associatedcomponents[facadeComponent.compType].append(facadeComponent)
    
    """
    the get/set functions
    """
    def getDefectType(self):
        return self.defectType
    
    def getDefectPlane(self):
        return self.defectPlane
    def setDefectPlane(self, defectPlane):
        self.defectPlane = defectPlane

    def getPossibleCause(self):
        return self.possCause
    def setPossCause(self, possCause):
        self.possCause = possCause

    def getSuggestRepair(self):
        return self.suggestRepair
    def setSuggestRepair(self, suggestion):
        self.suggestRepair = suggestion

    def getAppMaterials(self):
        return self.appMaterials
    def addAppMaterials(self, newMaterials):
        #newmaterials: list of materials (in String)
        self.appMaterials.append(newMaterials)

    def getAppComps(self):
        return self.appComps
    def addAppComps(self, newComps):
        #newComps: list of new components
        self.appComps.append(newComps)

    def getRefImg(self):
        return self.reference
    def updateRefImg(self, img):
        self.reference = img
    
        
"""
JSON object can be used to add reference images
ref link: https://docs.python.org/3/library/json.html
"""        
    


        
    
"""
JSON object can be used to add reference images
ref link: https://docs.python.org/3/library/json.html
"""  

