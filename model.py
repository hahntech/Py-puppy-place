#!/usr/bin/python3

class Animal:
    """An animal representation in PuppyPlace system"""

    def __init__(self, id, date, breed, estimatedAge, notes=[]):
        self.id = id
        self.admissionDate = date
        self.breed = breed
        self.estimatedAge = estimatedAge
        for note in notes:
            self.validateNoteType(note)
        self.notes = notes.copy()

    def getID(self):
        return self.id

    def getAdmissionDate(self):
        return self.admissionDate

    def getBreed(self):
        return self.breed

    def getEstimatedAge(self):
        return self.estimatedAge

    def getNotes(self):
        return self.notes

    def validateNoteType(self, note):
        if type(note) == str:
            return True
        else:
            raise TypeError("Notes are required to be string data types.")

    def addNote(self, note):
        if self.validateNoteType(note):
            self.notes = self.notes + [note]

    class Cat(Animal):
        """A cat representation in PuppyPlace system"""

        def __init__(self, id, date, breed, estimatedAge, notes=[]):
            Animal.__init__(self, id, date, breed, estimatedAge, notes)

    class Dog(Animal):
        """A dog representation in PuppyPlace system"""

        def __init__(self, id, date, breed, estimatedAge, notes=[]):
            Animal__init__(self, id, date, breed, estimatedAge, notes)

            
