class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.numNodes = 0

    def insertFirst(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.numNodes+=1

    def insertlast(self,data):
        node = Node(data)
        if self.numNodes == 0 :
            self.head = node
            self.numNodes+=1

        else:
            currNode = head
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = node
            self.numNodes+=1

    def remFirst(self):
        self.head = self.head.nexr
        self.numNodes -=1

    def remLast(self):
        currNode = self.head
        while currNode.next is not None:
            
