#!/usr/bin/python3

from service import DogService, CatService

class Menu:
    def __init__(self, options={}):
        self.options = options.copy()
        self.options[0] = "Exit"

    def printOptions(self):
        keys = sorted(self.options.keys())
        for k in keys:
            print("{}. {}".format(k, self.options.get(k)))
        try:
            selected = int(input("What do you want to do?"))
        except ValueError:
            print("Please provide a valid option.")
            selected = None
        return selected

class AnimalSelectionMenu(Menu):
    def __init__(self, dogCallback, catCallback):
        Menu.__init__(self, {1: "Dog", 2:"Cat"})
        self.dogCallback = dogCallback
        self.catCallback = catCallback

    def start(self):
        selected = self.printOptions()
        if selected == 1:
            self.dogCallback()
        elif selected == 2:
            self.catCallback()

class GuestCheckInMenu:
    def __init__(self, dogService, catService):
        self.dogService = dogService
        self.catService = catService

    def createDog(self):
        self.dogService.store(input("breed: "), input("estimated age: "))

    def createCat(self):
        self.catService.store(input("breed: "), input("estimated age: "))

    def start(self):
        AnimalSelectionMenu(self.createDog, self.createCat).start()

class GuestCheckoutMenu:
    def __init__(self, dogService, catService):
        self.dogService = dogService
        self.catService = catService

    def checkOutDog(self):
        ListMenu(self.dogService, self.catService).listDogs()
        id = int(input("dog id: "))
        self.dogService.remove(id)

    def checkOutCat(self):
        ListMenu(self.dogService, self.catService).listCats()
        id = int(input("cate id: "))
        self.catService.remove(id)

    def start(self):
        AnimalSelectionMenu(self.checkOutDog, self.checkOutCat).start()

class ListMenu:
    def __init__(self, dogService, catService):
        self.dogService = dogService
        self.catService = catService

    def listDogs(self):
        sortedDogs = sorted(self.dogService.all(), key=lambda d: d.getID())
        dogs = map(lambda dog: "{}) {} - {} - {} - {}".format(dog.getID(),
        dog.getAdmissionDate(), dog.getBreed(), dog.getEstimatedAge(),
        ",".join(dog.getNotes())), sortedDogs)
        for dog in dogs:
            print(dog)

    def listCats(self):
        sortedCats = sorted(self.catService.all(), key=lambda c: c.getID())
        cats = map(lambda cat: "{}) {} - {} - {} - {}".format(cat.getID(),
        cat.getAdmissionDate(), cat.getBreed(), cat.getEstimatedAge(),
        ",".join(cat.getNotes())), sortedCats)
        for cat in cats:
            print(cat)

    def start(self):
        AnimalSelectionMenu(self.listDogs, self.listCats).start()

class AddNotesMenu:
    def __init__(self, dogService, catService):
        self.dogService = dogService
        self.catService = catService

    def addNotesDog(self):
        ListMenu(self.dogService, self.catService).listDogs()
        id = int(input("dog id: "))
        note = input("note: ")
        self.dogService.getByID(id).addNote(note)

    def addNotesCat(self):
        ListMenu(self.dogService, self.catService).listCats()
        id = int(input("cat id: "))
        note = input("note: ")
        self.catService.getByID(id).addNote(note)

    def start(self):
        AnimalSelectionMenu(self.addNotesDog, self.addNotesCat).start()

class MainMenu(Menu):
    def __init__(self, dogService=DogService(), catService=CatService()):
        Menu.__init__(self, {
            1: "Guest Check-in",
            2: "Guest Check-out",
            3: "Guests Lists",
            4: "Add Notes"
            })
            self.dogService= dogService
            self.catService = catService

        def checkIn(self):
            GuestCheckInMenu(self.dogService, self.catService).start()

        def checkOut(self):
            GuestCheckoutMenu(self.dogService, self.catService).start()

        def list(self):
            ListMenu(self.dogService, self.catService).start()

        def addNotes(self):
            AddNotesMenu(self.dogService, self.catService).start()

        def start(self):
            print("Welcome to Puppy Place's system!")

            selected = None
            while selected != 0:
                selected = self.printOptions()
                if selcted == 1:
                    self.checkIn()
                elif selected == 2:
                    self.checkOut()
                elif selected == 3:
                    self.list()
                elif selected == 4:
                    self.addNotes()
                    









#
