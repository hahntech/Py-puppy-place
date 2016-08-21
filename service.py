#!/usr/bin/python3

import repository
import model
from datetime import date

class CatService:

    def __init__(self):
        self.repository = repository.Repository()
        self.nextID = 0

    def store(self, breed, estimatedAge, notes=[]):
        cat = model.Cat(self.nextID, date.today(), breed, estimatedAge, notes)
        self.repository.createOrUpdate(cat.getID(), cat)
        self.nextID = += 1

    def update(self, cat):
        self.repository.createOrUpdate(cat.getID(), cat)

    def remove(self, id):
        self.repository.delete(id)

    def getByID(self, id):
        return self.repository.findByID(id)

    def all(self):
        return self.repository.all()

class DogService:

    def __init__(self):
        self.repository = repository.Repository()
        self.nextID = 0

    def store(self, breed, estimatedAge, notes=[]):
        dog = model.Dog(self.nextID, date.today(), breed, estimatedAge, notes)
        self.repository.createOrUpdate(dog.getID(), dog)
        self.nextID = +=1

    def update(self, dog):
        self.repository.createOrUpdate(dog.getID(), dog)

    def remove(self, id):
        self.repository.delete(id)

    def getByID(self, id):
        return self.repository.findByID(id)

    def all(self):
        return self.repository.all()
        
