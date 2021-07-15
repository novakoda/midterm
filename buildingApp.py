# James Williams
print('\n----- James Williams -----\n')

from building import *

def createHouse():
    print('\n-----\nCreating a new house...\n')
    siding = input('What is the siding of the home? ')
    house = House(siding)
    rooms = []

    living = Room(int(input('Enter living room sqft: ')))
    rooms.append(living)
    kitchen = Room(int(input('Enter kitchen room sqft: ')),True,True)
    rooms.append(kitchen)
    dining = Room(int(input('Enter dining room sqft: ')))
    rooms.append(dining)

    beds = int(input('How many bedrooms? '))
    for i in range(beds):
        bed = Room(int(input('Enter bedroom %s sqft: '%(i+1))))
        rooms.append(bed)

    baths = int(input('How many bathrooms? '))
    for j in range(baths):
        bath = Room(int(input('Enter bathroom %s sqft: '%(j+1))),True)
        rooms.append(bath)

    house.set_rooms(rooms)
    return house

def createCommercialBuilding():
    print('\n-----\nCreating a new commercial building...\n')
    siding = input('What is the siding of the building? ')
    commercialBuilding = Commercial(siding)
    rooms = []

    kitchens = int(input('How many kitchens? '))
    for i in range(kitchens):
        kitchen = Room(int(input('Enter kitchen %s sqft: '%(i+1))),True,True)
        rooms.append(kitchen)

    roomsQuant = int(input('How many rooms? '))
    for j in range(roomsQuant):
        room = Room(int(input('Enter room %s sqft: '%(j+1))))
        rooms.append(room)

    baths = int(input('How many bathrooms? '))
    for k in range(baths):
        bath = Room(int(input('Enter bathroom %s sqft: '%(k+1))),True)
        rooms.append(bath)

    commercialBuilding.set_rooms(rooms)
    return commercialBuilding

def showSize(building):
    print('Total size of the %s building is %i sqft.' %
          (building.get_siding(), building.totalSquareFeet()))


houses = int(input('\nHow many homes do you want to create? '))
for hb in range(houses):
    home = createHouse()
    showSize(home)
    
stores = int(input('\nHow many commercial buildings do you want to create? '))
for cb in range(stores):
    store = createCommercialBuilding()
    showSize(store)
