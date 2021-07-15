# James Williams

class Building:
    def __init__(self, siding):
        self.__siding = siding

    def get_siding(self):
        return self.__siding
    def set_siding(self, siding):
        self.__siding = siding

class House(Building):
    def __init__(self, siding, rooms=[]):
        super().__init__(siding)
        self.__rooms = rooms

    def get_rooms(self):
        return self.__rooms
    def set_rooms(self, rooms):
        self.__rooms = rooms
    def totalSquareFeet(self):
        total = 0
        for room in self.__rooms:
            total += room.get_squarefeet()
        return total

class Commercial(Building):
    def __init__(self, siding, rooms=[]):
        super().__init__(siding)
        self.__rooms = rooms

    def get_rooms(self):
        return self.__rooms
    def set_rooms(self, rooms):
        self.__rooms = rooms
    def totalSquareFeet(self):
        total = 0
        for room in self.__rooms:
            total += room.get_squarefeet()
        return total

class Room:
    def __init__(self, squarefeet, water=False, gas=False):
        self.__squarefeet = squarefeet
        self.__water = water
        self.__gas = gas

    def get_squarefeet(self):
        return self.__squarefeet
    def set_squarefeet(self, sqarefeet):
        self.__squarefeet = squarefeet
    def get_water(self):
        return self.__water
    def set_water(self, water):
        self.__water = water
    def get_gas(self):
        return self.__gas
    def set_gas(self, gas):
        self.__gas = gas
