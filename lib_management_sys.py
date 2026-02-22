'''
Creating an Libarary management system using python oops
'''

class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}(ID={self.person_id}, Name={self.name})"


