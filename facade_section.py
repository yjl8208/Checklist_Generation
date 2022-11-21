#from facade import Facade
from shapely.geometry import Polygon

# class Thing:
#     def __init__(self, parent):
#         self.parent = parent

# phone  = Thing(bag1)
# bag = Bag([phone, lip_balm, paper])
# paper1, paper2, paper3 = cut(paper)
# def cut(item):
#     parent = item.parent
#     i1, i2, i3 = item[:1], item[1:2], item[2:3]
#     o1 = paper(i1, parent)
#     o2 = 
#     o3 = 
#     return o1, o2, o3

# paper_parent = paper.parent

# class Thing:
#     def __init__(self, parent):
#         self.parent = parent

# phone  = Thing(bag1)
# bag = Bag([phone, lip_balm, paper])
# paper1, paper2, paper3 = cut(paper)
# def cut(item):
#     parent = item.parent
#     i1, i2, i3 = item[:1], item[1:2], item[2:3]
#     o1 = paper(i1, parent)
#     o2 = 
#     o3 = 
#     return o1, o2, o3

# paper_parent = paper.parent

class FacadeSection:
    
    
    #store components as a dictionary:key-->component type, value-->component ID
    """ #TODO: Consider JSON format to store the hierarchical information"""
    
    @property
    def __init__(self, sectionPlane):
        
        self.id = id
        #sectionPlane: TwoDPlane instance 
        self.secPlane = sectionPlane
        self.facade = None
        #Dictionary of components in FacadeSection, key: compType, value: list of component instances.
        self.components = {}
        #Dictionary of defects in FacadeSection, key: defectType, value: list of defect instances.
        self.defects = {}
    

    '''
    'set/get' functions
    '''
#Do we need to update the plane?
    def setSecPlane(self, plane):
        self.secPlane = plane
    def getSecPlane(self):
        return self.secPlane
#Facade should be set when the section is generated
    def setFacade(self, facade):
        self.facade = facade
    def getFacade(self):
        return self.facade
        
    #polygons.bounds for getting a (minx, miny, maxx, maxy) tuple as bounding box
    #contains/within function in Shapely can be used to check the spatial relationship
    def containComponent(self, component):
        relation = self.secPlane.containsPlane(component.comPlane)
        return relation

    def getComponents(self):
        components = self.facade.getFacadeComponents()
        for compType in components.keys():
            for item in components[compType]:
                if self.containComponent(item) == True:
                    self.components[compType] += item
        return self.components


    def getDefectType(self):
        #Return a list of defect type
        defectType = []
        for key in self.component.keys():
            for component in self.component[key]:
                defectType = set(defectType)
                componentDefect = set(component.associatedDefects.keys())
                newOnes = componentDefect - defectType
                defectType = defectType + list(newOnes)
        return defectType

    'TODO: Implement getDefect function'
    # def getDefect(self):  
    #     for comp in self.components:
    #         defects.extend(comp.getDefect)
    
    # def containDefect(self, defect):
    #     "Check if a defect instance is in this Section"
    #     if defect.defectType in self.getDefectType() == False:
    #         return False
    #     for compType in self.components.keys()
    #     return self.polyCoordinates.contains(defect.polyCoordinates)

    
    """TODO: Get defect list through Component Class."""
    """
    HOW TO DIFFERENTIATE THE DEFECT OBJECTS THAT HAVE SAME ATTRIBUTES BUT ARE ASSIGNED TO DIFF COMPONENTS??--> using ID
    """
   
    
    #Extract facade component instances from facade section?
    # def hasComponent(self, facadeComponent):
    #     return self.components
    
    
# test        
    