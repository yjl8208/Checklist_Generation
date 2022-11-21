from enum import Enum
from datetime import date

"""
Enumeration for condition
"""

class ConditionEnum(Enum):
    
    SAFE = 'SAFE'
    SWARMP = 'SWARMP'
    UNSAFE = 'UNSAFE'
    
    def __init__(self, condition, assessmentDate=date.today(), assessmentDescription=''):
        self.condition = condition
        self.assessmentDate = assessmentDate
        self.assessmentDescription = assessmentDescription

    """
    'setter' and 'getter' function
    """
    def getCondition(self):
        return self.value
    def getAssessmentDate(self):
        return self.assessmentDate
    def getAssessmentDescription(self):
        return self.assessmentDescription