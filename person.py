
class Person:
    def __init__(self, id, firstName, lastName) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName

class Owner(Person):
    def __init__(self, id, firstName, lastName) -> None:
        super().__init__(id, firstName, lastName)

class Inspector(Person):
    def __init__(self, id, firstName, lastName, company) -> None:
        super().__init__(id, firstName, lastName)
        self.company = company
