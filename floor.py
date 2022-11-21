from shapely.geometry import Point
from geometry_representation import TwoDPlane
import itertools
from shapely.geometry import Polygon


class Floor:
    
    # #TODO: ID implementation in other classes
    # newid = itertools.count()

    def __init__(self, height, length, startPoint, floorNum):
        
        #TODO: initialize floor ID--> ID does not work as expected. refers
        #ref link: https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class
        # self.flrID = next(Floor.newid)
        self.id = id
        #height:float
        self.height = height
        #length:float
        self.length = length
        #startPoint--> the left lower corner of the floor plane: [float, float]
        self.startPoint = Point(startPoint)
        #flrNum: int
        self.flrNum = floorNum
        #Plane: polyCoordinates [(x0, y0), (x0, y1), (x1, y1), (x1, y0)] with the starting point being the left lower corner and runs clockwise

        print("hello")
        print(self.startPoint, floorNum)

        startX = self.startPoint.x
        startY = self.startPoint.y
        x1 = startX + self.length
        y1 = startY + self.height
        self.flrPlane = TwoDPlane([startPoint, (startX, y1), (x1, y1), (x1, startY)])
        #components:a dictionary that stores the components included in this floor. key: component type(4th level), value: list of component instances
        self.components = {}

        self.comPlane = [ (startX, startY), (startX, startY+height), (startX+length, startY+height), (startX+length, startY) ]




    """
    'Getter' and 'Setter' functions
    """    
    def getNumOfBalcony(self):
        """ TODO: get number of balconies for each floor [Define the way components is stored in the dictionary]"""
        if 'balcony' in self.components.keys():
            numOfBalcony = len(self.components['balcony'])
            return numOfBalcony
        else:
            # print("This floor does not contain any balcony.")
            return 0
    
    def getFlrID(self):
        return self.flrID
    def getComponents(self):
        return self.components

    def getHeight(self):
        return self.height
    #TODO:set new height?
    def setHeight(self, height):
        self.height = height

    def getLength(self):
        return self.length
    def setLength(self, length):
        self.length = length

    def getStartPoint(self):
        return self.startPoint
    def setStartPoint(self, point):
        self.startPoint = point

    def getFlrNum(self):
        return self.flrNum
    def setFlrNum(self, num):
        self.flrNum = num

    def getFlrPlane(self):
        return self.flrPlane
        
    # def getDefects(self):
    'NO NEED for RQ2 NOW'
      