class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toString(self):
        return self.name+" "+str(self.age)

