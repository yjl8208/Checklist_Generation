from enum import Enum

"""
Enumeration for Facade direction
"""

class DirectionEnum(Enum):
    N = "North"
    S = "South"
    E = "East"
    W = "West"
    
    def __init__(self, direction):
        self.direction = direction
