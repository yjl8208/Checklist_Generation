from shapely.geometry import Polygon

"""
Geometric representation for building, facade, facade section, facade component, and defect 

ref link: https://standards.buildingsmart.org/IFC/RELEASE/IFC4/FINAL/HTML/link/ifcgeometricrepresentationitem.htm
"""

class GeometryRepresentation():
    def __init__(self, polyCoord):
        self.polyCoord = polyCoord
        self.plane = Polygon(polyCoord)

    """
    'getter' and 'setter' functions
    """
    def getPolyCoord(self):
        return self.polyCoord
    def getPlane(self):
        return self.plane
    def setPolyCoord(self, polyCoord):
        self.polyCoord = polyCoord
        self.plane = Polygon(polyCoord)
    
    
"""
representation for 2D plane
Create a polygon based on the polycoordinates of points
-Check for contain relationship between plane instances
-seperate a plane to a number of vertical planes
"""

class TwoDPlane:

    #TODO: use shapely Point class to define Plane
    def __init__(self, polyCoord):
    #     Plane: polyCoordinates [(x0, y0), (x0, y1), (x1, y1), (x1, y0)] with the starting point being the left lower corner and runs clockwise
         self.polyCoord = polyCoord
         self.plane = Polygon(polyCoord)






    """

to do: sepaarte plane based on columns, and floors

use shapely to dfefine plane
-> done, define as polygon

rmake "containPlane" based on shapely
-> done, define as polygon

make actually woroking " getbounds and getarea"


    """




    """ # Define functions to evaluate the contain relationship """
    def containPlane(self, secPlane):
        #Return TRUE if self contains the second plane, FALSE if not
        firstPlane = self.plane
        secondPlane = secPlane
        #return firstPlane.contains(secondPlane)
        return firstPlane.contains(secondPlane)



    """ # Define functions to seperate the plane into several sections (can be used for facade--> facade sections)"""
    "--> seems to divide into columns --> modify to use with shapely"
    def seperatePlane(self, num):
        #seperate the plane to the number of subplanes
        self.y0 = self.getPolyCoord()[0][1]
        self.y1 = self.getPolyCoord()[1][1]
        planes = []
        y0 = self.y0
        y1 = self.y1
        inspectionRange = (self.getPolyCoord()[2][0]-self.getPolyCoord()[0][0])/num
        for i in range (0, num):
            x0 = i*inspectionRange
            x1 = (i+1)*inspectionRange
            point1 = (x0, y0)
            point2 = (x0, y1)
            point3 = (x1, y1)
            point4 = (x1, y0)
            plane = TwoDPlane([point1, point2, point3, point4])
            planes.append(plane)
        return planes

    def getArea(self):
        #return area of the 2D plane
        return  self.plane.area

    def getBounds(self):
        #return tuple (xmin, ymin, xmax, ymax)
        return self.plane.bounds

    def getPolyCoord(self):
        #return tuple (xmin, ymin, xmax, ymax)
        return self.polyCoord












