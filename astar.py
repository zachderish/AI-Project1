import heap
import math
import timeit

class node:
    def __init__(self, position, hvalue, gvalue, parent):
        self.position = position
        self.hvalue = hvalue
        self.gvalue = gvalue
        self.parent = parent

    def getf(self):
        return self.gvalue + self.hvalue

    def updateg(self, g):
        self.gvalue = g
    
    def __eq__(self, other):
        #print("item to compare: ", other.position)
        return self.position == other.position
    
    def __lt__(self, node):
        if self.getf() < node.getf():
            return True
        return False

    def __gt__(self, node):
        if self.getf() > node.getf():
            return True
        return False

def min(x, y):
    if x > y:
        return y
    else:
        return x

def max(x, y):
    if x > y:
        return x
    else:
        return y

def findH(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return 1.414*min(abs(x1-x2),abs(y1-y2))+max(abs(x1-x2),abs(y1-y2))-min(abs(x1-x2),abs(y1-y2))

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt(pow(abs(x1-x2),2)+pow(abs(y1-y2),2))

def isBlocked(position, blocked):
    if position in blocked:
        return True
    return False

#finds if node is available to travel to, also make sure not off grid
def isOpen(position, child, dimensions, blocked):

    # check off grid or not
    cx, cy = child
    dx, dy = dimensions

    if cx > dx or cx < 0:
        return False

    if cy > dy or cy < 0:
        return False

    # check blocked path or not
    px, py = position

    if cx-px == 1 and cy-py == 1:
        return not isBlocked(position, blocked)
    
    if cx-px == 0 and cy-py == 1:
        return not isBlocked(position, blocked) or not isBlocked((px-1,py), blocked)

    if cx-px == -1 and cy-py == 1:
        return not isBlocked((px-1,py), blocked)

    if cx-px == -1 and cy-py == 0:
        return not isBlocked((px-1,py), blocked) or not isBlocked((px-1,py-1), blocked)

    if cx-px == -1 and cy-py == -1:
        return not isBlocked((px-1,py-1), blocked)

    if cx-px == 0 and cy-py == -1:
        return not isBlocked((px,py-1), blocked) or not isBlocked((px-1,py-1), blocked)

    if cx-px == 1 and cy-py == -1:
        return not isBlocked((px,py-1), blocked)

    if cx-px == 1 and cy-py == 0:
        return not isBlocked((px,py-1), blocked) or not isBlocked(position, blocked)

def findChildren(Node, dim, blocked):
    listofchildren = []
    position = Node.position
    x, y = position

    places = []
    places.append((x-1,y))
    places.append((x,y-1))
    places.append((x-1,y-1))
    places.append((x+1,y))
    places.append((x,y+1))
    places.append((x+1,y+1))
    places.append((x-1,y+1))
    places.append((x+1,y-1))

    for i in places:
        if isOpen(position, i, dim, blocked):
            listofchildren.append(i)
    
    return listofchildren


def updateVertex(parent, child, openList):
    cost = distance(parent.position, child.position)
    
    if parent.gvalue + cost < child.gvalue:
        child.updateg(parent.gvalue + cost)
        child.parent = parent
        if openList.contains(child):
            openList.remove(child)
        
        openList.insert(child)

def main(file):

    # Used to calculate program run time
    startTime = timeit.default_timer()

    #list for nodes and their values
    nodes = []

    #file = open(file)
    # Get input from graphics
    start = tuple(map(int, file.readline().split()))
    goal = tuple(map(int, file.readline().split()))
    dim = tuple(map(int, file.readline().split()))


    blocked = []
    while True:
        line = file.readline()
        if not line:
            break
        x = line.split()
        
        if int(x[2]) == 1:
            pos = int(x[0]), int(x[1])
            blocked.append(pos)

    openList = heap.heap()
    
    startNode = node(start, findH(start, goal), 0, None)
    nodes.append(startNode)
    startNode.parent = startNode

    openList.insert(startNode)

    closedList = []
    final_node = None
    nodes_traversed = 0

    
    while not openList.isEmpty():
        #print("open list size: ", openList.get_size())
        exploringNode = openList.pop()
        nodes_traversed += 1
        
        if exploringNode.position == goal:
            final_node = exploringNode
            break

        closedList.append(exploringNode)

        children = findChildren(exploringNode, dim, blocked)
        for i in children:
            if node(i,0,0,None) not in closedList:
                child = node(i, findH(i, goal), float('inf'), None)
                if not openList.contains(node(i,0,0,None)):
                    #child = node(i, findH(i, goal), float('inf'), None)
                    nodes.append(child)
                    openList.insert(child)
                updateVertex(exploringNode, child, openList)


    # if path found, final node is goal node
    path = []
    if final_node is None:
        print("no path found")
    else:
        print("Path found,", "goal at ", final_node.position, ", Tracing from goal to start:")

        i = final_node
        while i.parent is not i:
            print(i.position)
            path.append(i.position)
            i = i.parent


    # Results Output
    print('Total Nodes Traversed: ', nodes_traversed)
    print("Path Length: ", len(path))

    stopTime = timeit.default_timer()
    print('Program finished in ', stopTime - startTime, "seconds")
    #start node was not being printed
    path.append(start)
    return path, nodes


#main("C:\\Python Stuff\\CS 440\\Assignment 1\\graph0.txt")
