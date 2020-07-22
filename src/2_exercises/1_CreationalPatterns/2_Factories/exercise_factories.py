class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    def create_person(self, name):
        # todo