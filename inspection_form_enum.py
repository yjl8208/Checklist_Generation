from enum import Enum

"""
Facade inspection form: vertical or horizontal
--> facade decomposition by floor ('H') or by section ('V')

"""
class InspectionFormEnum(Enum):
    V = 'V'
    H = 'H'
    
    def __init__(self, inspectionForm):
        self.inspectionForm = inspectionForm

    def getInspectionForm(self):
        return self.inspectionForm
