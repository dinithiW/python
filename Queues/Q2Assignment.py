class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
         return (len(self.items))

inputLine = input("Please enter the vehicle details")

vehiclesList = inputLine.split(',')

for a in vehiclesList:
    
    c = carPark()
    status,plateNumber = a.split()
    if status=='a':
            
        c.addToCarPark(plateNumber)
        
    elif status=='d':
        c.departures(plateNumber)
    else:
        continue
    

        
class car(object):

    def __init__(self,lplateNumber):
        self.lplateNumber = lplateNumber
        self.moves = 0

class waitingList:

    def __init__(self):
        self.wait = []
        self.moves = 0

    
        
class carPark:

    def __init__(self):
        self.vehiclesParked = []
        self.allVehicles = []
        self.waitingList = Queue()

    def addToCarPark(self,plateNumber):
        if(len(self.vehiclesParked)<10 ):
            #print(self.vehiclesParked.size())
            print("Space is available")
            self.vehiclesParked.append(plateNumber)
            print(plateNumber + " has arrived")
            print("There are ",(10-len(self.vehiclesParked))," slots remaining")

        else:
            self.waitingList.enqueue(plateNumber)
            print("Vehicle added to waiting list") 

    def departures(self,lplateNumber):
        print('depart')#for a in self.allVehicles

