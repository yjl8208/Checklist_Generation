from enum import Enum

class RefConCodeEnum(Enum):
    Code1968 = "1968 Building Code" #Apply to building < 07/01/2008
    Code2008 = "2008 Building Code" #Apply to building (07/01/2008 - 12/31/2014)
    Code2014 = "2014 Construction Code" #Apply to building >12/31/2014

    def __init__(self, refConCode):
        self.refConCode = refConCode
    