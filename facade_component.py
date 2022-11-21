from facade import Facade
from facade_section import FacadeSection
from shapely.geometry import Polygon



#FacadeComponent
#FacadeComponent
class FacadeComponent:

    #TODO: modify the ID representation
    # compID = None
    
    def __init__(self, compType, materials, comPlane, subcomponents = [], safeCon=None):
        
        """TODO: update the ID functions"""
        self.id = id
        """TODO: compoType Class?"""
        self.compType = compType
        #material: list of materials
        self.materials = materials
#         self.flrNum = flrNum
#         self.sectNum = sectNum
        #comPlane: TwoDPlane object
        self.comPlane = comPlane
        self.stability = None
        #store subcomponent as a list, if there's no subComp, return None
        self.subComp = subcomponents
        self.safeCon = safeCon
        #dictionary that stores defect instances with defect type as key and list of id/defect instances as value
        self.associatedDefects = {}

    
    '''
    'getter/setter' functions
    '''
    def hasDefect(self):
        if len(self.associatedDefects) != 0:
            return True
        else:
            return False
    def getAssociatedDefects(self):
        if self.hasDefect() == True:
            return self.associatedDefects
        #Is it better to return the dictionary or a list of defect instances/types
        else:
            print("This component does not have defect identified on it.")
    def getDefectType(self):
        #return defect type
        defectType = self.associatedDefects.keys()
        return defectType

    def getCompType(self):
        return self.compType
        #Not really need to set component type
    def setCompType(self, compType):
        #compType is a String
        self.compType = compType
    
    def getMaterials(self):
        return self.materials
    def setMaterials(self, materials):
        self.materials = materials
    
    def getPlane(self):
        return self.comPlane
    def setPlane(self, plane):
        self.comPlane = plane
    
    #Stability: boolean value for whether the component is stable
    def setStability(self, stability):
        self.stability = stability

    def getStability(self):
        if self.stability != None:
            return self.stability
        else:
            print("The stability of this component has not been eveluated yet.")
    
    def getSubComp(self):
        if len(self.subComp) == 0:
            #print('This component does not have any sub-components.')
            return None
        return self.subComp
    def getSubCompType(self):
        if len(self.subComp) == 0:
            return None
        subType = []
        # subPlanes = []
        for item in self.subComp:
            subType.append(item.compType)
            # subPlanes.append(item.comPlane)
        return subType
    def setSubComp(self, subComp):
        self.subComp = subComp
    def addSubComp(self, item):
        self.subComp.append(item)

    def hasSafeCon(self):
        if self.safeCon != None:
            return True
        else:
            return False
    def getSafeCon(self):
        if self.hasSafeCon() == True:
            return self.safeCon
        else:
            print("The safe condition of this component is not evaluated individually.")
    def setSafeCon(self, safeCon):
        self.safeCon = safeCon


    
    def assignDefect(self, defect):
        #? assign instance or name defect type?
        self.associatedDefects[defect.getdefectType()].append(defect.getDefectID())
        #print("The %s has been assigned to the designated %s" %（self.compType, defect.defctType))

    def removeDefect(self, defect):
        #remove a defect instance
        self.associatedDefects[defect.getdefectType()].remove(defect.getDefectID())


    # def getDefectInstances(self):
    #     defectInstances = [] #? 
    #     for defect in self.associatedDefects.keys():
    #         defectInstances = defectInstances.extend(self.associatedDefects.get(defect))
    
    
    #Need sectionNum?
#     def sectionNum (self, facade):       


class Window(FacadeComponent):
    def __init__(self, compType, materials, comPlane, subcomponents=[], safeCon=None):
        super().__init__(compType, materials, comPlane, subcomponents=subcomponents, safeCon=safeCon)  