class Node:
    def __init__(self, startAddress, endAddress, hole, processID):
        self.next = None
        self.startAddress = startAddress
        self.endAddress = endAddress
        self.hole = hole
        self.processID = processID

    

class LinkedList:
    def __init__(self):
        self.numnodes = 0
        self.head = None

    def insertFirst(self,startAddress, endAddress,hole, processID):
        newnode = Node(startAddress, endAddress,hole,processID)
        newnode.next = self.head
        self.head = newnode
        self.numnodes += 1

    def insertLast(self,startAddress, endAddress,hole, processID):
        newnode = Node(startAddress, endAddress,hole, processID)
        newnode.next = None
        if self.head == None:
            self.head = newnode
            return
        lnode = self.head
        while lnode.next != None:
            lnode = lnode.next
        lnode.next = newnode
        self.numnodes += 1

    def remFirst(self):
        cnode = self.head
        self.head = cnode.next
        cnode.next = None
        del cnode
        self.numnodes -= 1

    def remLast(self):
        lnode = self.head
        while lnode.next != None:
            pnode = lnode
            lnode = lnode.next
            pnode.next = None
        del lnode
        self.numnodes -= 1

    def getFirst(self):
        return self.head

    def getLast(self):
        cNode = self.head
        while cNode.next != None:
            cNode = cNode.next
        return cNode

    def print_list(self):
        lnode = self.head
        while lnode:
            lnode.strnode()
            lnode = lnode.next

    def getSize(self):
        return self.numnodes

class Processes:

    def __init__(self):
        self.processList = LinkedList()
        self.processList.insertFirst(0, 2559, True, -1)
        self.allocateMemory("operating system", 400)

    

    def allocateMemory(self, processID, memory):
        if self.checkID(processID):
            print(processID + " already exists.Check again")
            return
        currNode = self.processList.head
        while currNode != None:
            
            freeMemory = currNode.endAddress-currNode.startAddress+1
            if currNode.hole == True and freeMemory >= memory:
                currNode.hole = False
                currNode.processID = processID
                currNode.endAddress = currNode.startAddress + memory - 1
                remainingMemory = freeMemory - memory
                if remainingMemory > 0:
                    
                    newNode = Node(currNode.endAddress+1, currNode.endAddress+remainingMemory, True, -1)
                    newNode.next = currNode.next
                    currNode.next = newNode
                print(processID + " has been allocated")
                return
            currNode = currNode.next
        print("Not enough memory to allocate slot")


    def checkID(self, processID):
        currNode = self.processList.head
        while currNode != None:
            if currNode.processID == processID:
                return True
            currNode = currNode.next
        return False


    def terminate(self, processID):
        currNode = self.processList.head
        while currNode != None:
            if currNode.processID == processID:
                currNode.hole = True
                currNode.processID = -1
                self.continuousBlock()
                print(processID + " has been terminated")
                return
            currNode = currNode.next
        print(processID + " does not exist")


    def continuousBlock(self):
        currNode = self.processList.head
        while currNode != None and currNode.next != None:
            
            node = currNode.next
            if currNode.hole == True and node.hole == True:
                currNode.endAddress = node.endAddress
                currNode.next = node.next
                self.continuousBlock()
                return
            else:
                currNode = currNode.next

    def snapshot(self):
        currNode = self.processList.head
        while currNode != None:
            processID = currNode.processID
            if processID == -1:
                processID = "free slot"
            startAddress = currNode.startAddress
            endAddress = currNode.endAddress
            print(processID , "=> " , (startAddress) , "k - " , (endAddress) , "k")
            currNode = currNode.next
            
p = Processes()
p.allocateMemory("p1",600)
p.allocateMemory("p2", 1000)
p.allocateMemory("p3", 300)
p.terminate("p2")
p.allocateMemory("p4", 700)
p.terminate("p1")
p.allocateMemory("p5", 400)
print("")
p.snapshot()
                
    
    
    

    
