class Person:
    def __init__ (self, id, name):
        self.name = name
        self.id = id

    def __str__(self):
        return str(self.id) + "\t" + self.name




class Drink:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def __str__(self):
        return str(self.id) + "\t" + self.name


class Preference:
    def __init__(self, person: str, drink):
        self.person = person
        self.drink = drink
    def __str__(self):
        return self.person.__str__() + "\t" + self.drink.__str__()


class Round:
    def __init__(self):
        self.active = False
        self.order = []
    def add_order(self, person, drink):
        if self.active == True:
            self.order.append(Preference(person, drink))

    

    def set_active(self, status):
        self.active = status