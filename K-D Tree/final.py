import math
class Node:
    def __init__(self, x, y, z, flag):
        self.left = None
        self.right = None
        self.split = None  # use 0 for x
        self.flag = flag # flag will be 2

        if flag is 2: #2 dimensions
            self.data = [x, y]
        else: #3 dimensions
            self.data = [x, y, z]

    def insert(self, node):

        if self.split is 0: #node is plit from x axis
            if node.data[0] < self.data[0]:  # checking whether the current nodes x is less than the previous one
                if self.left is None:  # self has no left sub tree
                    self.left = node
                    node.split = 1 #change split by x to split by y
                else:  # self has a left subtree
                    self.left.insert(node) # recursive call

            else:  # checking whether the current nodes x is greater than the previous one
                if self.right is None: #self has no right sub tree
                    self.right = node
                    node.split = 1 # change split by x to split by y
                else:
                    self.right.insert(node) # recursive call

        elif self.split is 1: #node is split by y axis
            if node.data[1] < self.data[1]: # checking whether current node's y value is less than self
                if self.left is None: # self has no left child
                    self.left = node
                    if self.flag is 2: #for a 2D plane
                        node.split = 0 #split must be made 0 again
                    else:
                        node.split = 2 # for a 3D space split must be made 2
                else:
                    self.left.insert(node)# recursive call

            else:#node's y value is greater than self's y value
                if self.right is None: #self has no right sub tree
                    self.right = node
                    if self.flag is 2:
                        node.split = 0
                    else:
                        node.split = 2
                else:
                    self.right.insert(node)

        else:
            if node.data[2] < self.data[2]:
                if self.left is None:
                    self.left = node
                    node.split = 0
                else:
                    self.left.insert(node)
            else:
                if self.right is None:
                    self.right = node
                    node.split = 0
                else:
                    self.right.insert(node)

    def printAll(self):
        print(self.data)
        if self.left is not None:
            self.left.printAll()
        if self.right is not None:
            self.right.printAll()

    def findClosest(self, node, distances, nodes):

        if self.split is 0: # if self is split by x
            if node.data[0] < self.data[0]: # checking whether the x value of node is less than self
                if self.left is not None: #recursive call
                    arr = self.left.findClosest(node, distances, nodes)

                if self.flag is 2:# calculating current distance for a 2D plane
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2)
                else:# calculating current distance for a 3D space
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2) + (
                    (self.data[2] - node.data[2]) ** 2)

                max_index = distances.index(max(distances));#finding the index of the maximum distance stored
                #in the list distances

                if curr_d < distances[max_index]:#if current distance is less than the maximum in the list
                    distances[max_index] = curr_d# replace that maximum value with the newly found value
                    nodes[max_index] = self #do the same with the list 'nodes'

                temp_d = ((self.data[0] - node.data[0]) ** 2)#find a temporary distance taking the square of the
                max_index = distances.index(max(distances));#differences of x coordinates

                if temp_d < distances[max_index] and self.right is not None: #if that distance is less than the
                    arr = self.right.findClosest(node, distances, nodes)#maximum and self has a right sub tree
                #traverse the right sub tree
            else:
                if self.right is not None:
                    arr = self.right.findClosest(node, distances, nodes)

                if self.flag is 2:
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2)
                else:
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2) + (
                    (self.data[2] - node.data[2]) ** 2)

                max_index = distances.index(max(distances));

                if curr_d < distances[max_index]:
                    distances[max_index] = curr_d
                    nodes[max_index] = self

                temp_d = ((self.data[0] - node.data[0]) ** 2)
                max_index = distances.index(max(distances))

                if temp_d < distances[max_index] and self.left is not None:
                    arr = self.left.findClosest(node, distances, nodes)

        elif self.split is 1:
            if node.data[1] < self.data[1]:
                if self.left is not None:
                    arr = self.left.findClosest(node, distances, nodes)

                if self.flag is 2:
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2)
                else:
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2) + (
                    (self.data[2] - node.data[2]) ** 2)

                max_index = distances.index(max(distances));

                if curr_d < distances[max_index]:
                    distances[max_index] = curr_d
                    nodes[max_index] = self

                temp_d = ((self.data[1] - node.data[1]) ** 2)
                max_index = distances.index(max(distances))

                if temp_d < distances[max_index] and self.right is not None:
                    arr = self.right.findClosest(node, distances, nodes)

            else:
                if self.right is not None:
                    arr = self.right.findClosest(node, distances, nodes)

                if self.flag is 2:
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2)
                else:
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2) + (
                    (self.data[2] - node.data[2]) ** 2)

                max_index = distances.index(max(distances))

                if curr_d < distances[max_index]:
                    distances[max_index] = curr_d
                    nodes[max_index] = self

                temp_d = ((self.data[1] - node.data[1]) ** 2)
                max_index = distances.index(max(distances))

                if temp_d < distances[max_index] and self.left is not None:
                    arr = self.left.findClosest(node, distances, nodes)

        else:
            if node.data[2] < self.data[2]:
                if self.left is not None:
                    arr = self.left.findClosest(node, distances, nodes)

                if self.flag is 2:
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2)
                else:
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2) + (
                    (self.data[2] - node.data[2]) ** 2)

                max_index = distances.index(max(distances));

                if curr_d < distances[max_index]:
                    distances[max_index] = curr_d
                    nodes[max_index] = self

                temp_d = ((self.data[2] - node.data[2]) ** 2)
                max_index = distances.index(max(distances))

                if temp_d < distances[max_index] and self.right is not None:
                    arr = self.right.findClosest(node, distances, nodes)

            else:
                if self.right is not None:
                    arr = self.right.findClosest(node, distances, nodes)

                if self.flag is 2:
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2)
                else:
                    curr_d = ((self.data[0] - node.data[0]) ** 2) + ((self.data[1] - node.data[1]) ** 2) + (
                    (self.data[2] - node.data[2]) ** 2)

                max_index = distances.index(max(distances))

                if curr_d < distances[max_index]:
                    distances[max_index] = curr_d
                    nodes[max_index] = self

                temp_d = ((self.data[2] - node.data[2]) ** 2)
                max_index = distances.index(max(distances))

                if temp_d < distances[max_index] and self.left is not None:
                    arr = self.left.findClosest(node, distances, nodes)

c = 3
distances = []
nodes = []

for i in range(c):
    distances.append(float('inf'))
    nodes.append(None)

def getInput():
    print('Please enter the required plane')
    print('Enter "a" to select 2D plane "b" to select 3D plane')
    data = input()
    if data is 'a':
        n, t = input().strip().split(' ')
        n, t = [int(n), int(t)]

        x, y = input().strip().split(',')
        x = x[1:]
        y = y[:-1]
        x, y = [float(x), float(y)]

        a = Node(x, y, 0, 2)
        a.split = 0

        for i in range(n - 1):
            x, y = input().strip().split(',')
            x = x[1:]
            y = y[:-1]
            x, y = [float(x), float(y)]

            if i > c - 2:
                d_new = list(distances)
                n_new = list(nodes)
                a.findClosest(Node(x, y, 0, 2), d_new, n_new)

                for n in n_new:
                    print(n.data);

            a.insert(Node(x, y, 0, 2))
    elif data is 'b':
        n, t = input().strip().split(' ')
        n, t = [int(n), int(t)]

        x, y, z = input().strip().split(',')
        x = x[1:]
        z = z[:-1]
        x, y, z = [float(x), float(y), float(z)]

        a = Node(x, y, z, 3)
        a.split = 0

        for i in range(n - 1):
            x, y, z = input().strip().split(',')
            x = x[1:]
            z = z[:-1]
            x, y, z = [float(x), float(y), float(z)]

            if i > c - 2:
                d_new = list(distances)
                n_new = list(nodes)
                a.findClosest(Node(x, y, z, 3), d_new, n_new)
                for n in n_new:
                    print(n.data);
            a.insert(Node(x, y, z, 3))
    else:
        print('Please enter valid data. Enter "a" or "b"')
        getInput()


getInput()

