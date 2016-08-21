#!/usr/bin/python3

class Reopsitory:

    """ In-memory storage for PuppyPlace entities"""

    def __init__(self):
        self.storage = {}

    def createOrUpdate(self, id, entry):
        self.storage[id] = entry

    def delete(self, id):
        del self.storage[id]

    def findByID(self, id):
        return self.storage.get(id)

    def all(self):
        return list(self.storage.values())

        
