

class Building:

    
    def __init__(self, floors, materials, height, binNum, refConCode, hasInspectionHistory=False):
        
        #id: string for building ID
        self.id = id
        #TODO: floor: dictionary of floor instances included in the building key: floor.flrID, value: floor instance name [string]--> can be used to access the instance with locals()
        #For now: floors is a list of floor objects
        self.floors = floors
        
        """ NUM OF FLRS MAY CHANGE FOR DIFF FACADE--> 3d REPRESENTATION FOR BUILDING, USE BOUNDING BOX AND FUNCTIONS TO DERIVE THIS NUM"""
    #calculation or derivation from the polygon, both are fine    
        self.numOfFlrs = len(floors)
        
        #facades: list of facade instances in the building
        # self.facades = facades
        
        #TODO: buildingPropertySet: list of building information needed for report submission
        #address, blockNum, lotNum, landmarkStatus, yearBuilt, isRenovated,yearRenovated, usage[Enum], certificateOfOcupancy
        #type[Enum],hasECBViolation(bool), 
        #self.buildingPropertySet = buildingPropertySet
        
        #materials: list of materials consisting the facade 
        self.materials = materials
        #height: float
        self.height = height
        #bin: int works as ID for building
        self.bin = binNum
        #refConCode: enumeration instance of  the building's reference construction code 
        self.refConCode = refConCode
        
        #hasInspectionHistory: boolean; link to InspectionHistory instances
        self.hasInspectionHistory = hasInspectionHistory
        #inspectionHistory: a list to store the previous inspection project instances
        self.inspectionHistory = None
        
        # facades = []--> will need a dictionary keep track of the building--facade [and building--floor] relationship
        self.owner = None
        self.floorHeights = []
    #numOfBalconies --> obtained from flrs or facades
    #BuildingPropertySet

    """
    'getter' and 'setter' functions
    """    
    def getOwner(self):
        return self.owner
    def setOwer(self, owner):
        self.owner = owner

    #floorHeights: a list of heights for all floors included in this building
    def getFloorHeights(self):
        # floorHeights = []
        for floor in self.floors:
            self.floorHeights.append(floor.getHeight())
        return self.floorHeights

    #arrayList
    def getListOfFlr(self):
        listOfFlr = []
        for floor in self.floors:
            listOfFlr.append(floor.getFlrID())
        return listOfFlr

    'TODO: not sure if we need to update the floors (not necessary for RQ 2 and 3)'

    def setFlrs(self, flrs):
        #flrs: a dictionary of floors 
        self.floors = flrs
    def addFlr(self, floor):
        #TODO: sort the list based on the floorNum?
        self.floors.append(floor)
    def deleteFlr(self, floorNum):
        for floor in self.floors:
            if floor.flrNum == floorNum:
                self.floors.remove(floor)

    
    #list of floor numbers
    def getNumOfFlrs(self):
        numOfFlrs = len(self.floors)
        return numOfFlrs
    
    def getMaterials(self):
        #return a list of materials
        return self.materials

    def setMaterials(self, materials):
        #materials: list of Materials
        self.materials = materials
    def addMaterial(self, material):
        #material: one instance of FacadeMAterialEnum Class
        self.materials.append(material)
    
    def getHeight(self):
        return self.height
    def setHeight(self, height):
        #height: float
        self.height = height
    
    def getBIN(self):
        return self.bin
    def setBIN(self, binNum):
        #binNum: int
        self.bin = binNum

    def getRefConCode(self):
        return self.refConCode
    def setRefConCode(self, code):
        #code: refConCode object
        self.refConCode = code

    def getHasInspectionHistory(self):
        return self.hasInspectionHistory
    def setHasInspectionHistory(self, new):
        #new: TRUE or False for whether the target building has inspection history
        self.hasInspectionHistory = new


    """
    numOfBalcony: can be obtained from facades or floors
        
    """   
    def getNumOfBalcony(self):
        numOfBalcony = 0
        for floor in self.floors:
            numOfBalcony += floor.getNumOfBalcony()
        return numOfBalcony
    

    """
    TODO: Get defects function implementation
    """

if __name__ == 'main':
    print('hello')
        
        