from inspection_form_enum import InspectionFormEnum
from shapely.geometry import Polygon
import math
from facade_section import FacadeSection

#Facade 

#Facade 
class Facade:

    def __init__(self, building, materials, direction, horiLength, plane, facadeComponents, hasSections=False):
        #Automatically assign an ID for the instance object
        self.id = id
        # building: building that include the facade
        self.building = building
        # self.facadeID = id(self)
        #material: ENUM compMATERIAL CLASS NEEDED
        self.materials = materials
        #Direction:ENUM DIRECTION CLASS NEEDED
        self.direction = direction
        #elevation: vertical positive measure of the facade (in ft)<-- height of building (getHeightOfBuilding method in Class Building)
        """#TODO: SIMILAR TO NUMOFFLRS, THIS NUMBER MAY CHANGE FOR DIFF FACADE INSTEAD OF A SAME NUM FOR THE WHOLE BUILDING--> ???"""
        self.numOfFlr = self.building.getNumOfFlrs()
        self.elevation = self.building.getHeight()
        #floorHeight: height of each floor (list? for different heights on each floor) <-- heightOfFloors from Floor through Building
        self.floorHeights = self.building.getFloorHeights()
        #horiLength: horizontal lenth of the facade in positive length measure (in ft)
        self.horiLength = horiLength
        #Plane: TwoDPlane instance
        self.plane = plane
        self.hasSections = hasSections
        
        #boundingbox: corner, x, y [positive length measure]

        self.hasFloor = True
        #floors: a list of all floors contained in this side of facade --> A map to store the building-floor 
        self.floors = []
        self.numberOfSections = 0
        #inspectionRange and numberOfSections --> vertical inspection form
        self.inspectionRange = None
        self.inspectionForm = None 
        #     floorHeight = None
        #TODO: Setup the facade ID attribute
        # facadeID = None
        #sections: a list to keep track of the facade sections that is included within this facade--> A map to store the building-section
        self.sections = []
        #Keep tracks of the components (key: componentType, value: componentObject) included here --> from here calculate the floor number and section that the component belongs to
        self.facadeComponents = facadeComponents
    
        #TODO: building <--> facade 
        #-->Add a map to keep the building-facade bidirectional relationship
        
        """ TODO: If having coordinates, should I derive elevation and length from calculation instead of input?"""
        
    '''
    'set/get' functions
    '''
    def getBuilding(self):
        return self.building
    
    def setMaterials(self, materials):
        #materials: a list of FacadeMaterialEnum instances
        self.materials = materials
    def addMaterials(self, materials):
        #materials: a list of FacadeMatyerialEnum instances
        self.materials.append(materials)
    def getMaterials(self):
        if len(self.materials) != 0:
            return self.materials
        else:
            #Is it possible that the facade
            print("Please add material information to this facade.")
    
    def setDirection(self, direction):
        #direction: instance of DirectionEnum class
        if self.direction == None:
            self.direction = direction
        else:
            print("The facade direction was set as "+self.direction.value)
            decision = input("Do you still want to set the direction? (y/n)")
            if decision == 'y':
                self.direction = direction
            else:
                return

    def getDirection(self):
        return self.direction
    
    def getElevation(self):
        return self.elevation
    
    def getNumOfFlr(self):
        #numOfFloor: int of how many floors are covered with the facade 
        return self.numOfFlr
    
    def getFlrHeights(self):
        return self.floorHeights
    
    def getHoriLength(self):
        return self.horiLength
        
    #TODO: Do we need to set horizontal length?
    def setHoriLength(self, length):
        self.horiLength = length
    
    def getSections(self):
        if len(self.sections) == 0:
            return None
        return self.sections
    def updateSections(self, num):
        print("The facade will be divided into {} sections.".format(str(num)))
        self.numberOfSections = num
        self.sections = self.setFacadeSection(num)
        return self.sections

    def setInspectionForm(self):
        '''
        input: inspectionForm
        output: numberOfSections for "V", numOfFlrs for "H".
        '''

        inspectionForm = input ("Please select the decomposition method (V/H): ")
        while inspectionForm != 'V' and inspectionForm != 'H':
            inspectionForm = input ("Please select the decomposition method (V/H): ")
        self.inspectionForm = InspectionFormEnum(inspectionForm)

        if self.inspectionForm.value == 'V':
            print("The facade will be decomposed vertically into sections.")
            self.hasSections = True
            self.numberOfSections = int(input ("How many drops will you do? "))
            #Check the number of drops based on the updated 1RCNY 103-04
            while self.numberOfSections > 0 and self.numberOfSections <  math.ceil(self.horiLength/60):
                print ("You need to do more drop-down inspection for this facade.")
                self.numberOfSections = int(input ("How many drops will you do? "))
            
            self.inspectionRange = self.horiLength/self.numberOfSections

            return self.numberOfSections
        
        if self.inspectionForm.value == "H":
            print("The facade will be decomposed horizontally by floor.")
            return self.numOfFloor
               
    def setFacadeSection(self):
        '''
        input: facade object
        output: a list of facadeSection objects
        '''
    #divide facade into a certain number of sections based on the inspector's input
        if self.inspectionForm == None:
            self.numberOfSections = self.setInspectionForm()
            print('when None happen:',self.numberOfSections)
        if self.inspectionForm.value == 'V':
            planes = self.plane.seperatePlane(self.numberOfSections)
            print('planes are: ',planes)
            for plane in planes:
                section = FacadeSection(plane, self)
                self.sections.append(section)
            return self.sections           
    
    #polygons.bounds for getting a (minx, miny, maxx, maxy) tuple as bounding box
    #contains/within function in Shapely can be used to check the spatial relationship
    
    
    def containComponent(self, facadeComponent):

        '''
        INPUT: facadeComponent object
        OUTPUT: Boolean for whether the component is contained within the facade
        '''
        relation = self.plane.containsPlane(facadeComponent.comPlane)
        
        return relation
    
    def getFacadeComponents(self):
        return self.facadeComponents
    #facade contains defect list --> can be obtained from component class
    """def containDefect(self, defect):
        '''
        INPUT: defect object
        OUTPUT: Boolean for whether the defect is contained within the facade
        '''
        relation = self.plane.contains(defect.defectPlane)
        if relation == True:
            self.defect
        return self.polyCoordinates.contains(defect.polyCoordinates)
    """

# if __name__ == "__main__":
#     test = Facade ("mars_rover2", "till Mars", "ISRO")
#     print(test.launch())
#     print(test.get_maker())        