import heap
import math

class node:
    def __init__(self, position, hvalue, gvalue, parent):
        self.position = position
        self.hvalue = hvalue
        self.gvalue = gvalue
        self.parent = parent # Node

    def getf(self):
        return self.gvalue + self.hvalue

    def updateg(self, g):
        self.gvalue = g
    
    def __eq__(self, other):
        #print("item to compare: ", other.get_position())
        return self.position == other.position
    

    def __lt__(self, node):
        if self.getf() < node.getf():
            return True
        return False

    def __gt__(self, node):
        if self.getf() > node.getf():
            return True
        return False

def findH(start, goal):
    startx, starty = start
    goalx, goaly = goal
    return math.sqrt((pow(startx - goalx,2) + pow(starty - goaly, 2)))

# Given 2d positions pos1 and pos2, tuples, check straight line connected or not
# returns true if line of sight connected
# blocked = list of blocked positions
def line_of_sight(pos1, pos2, blocked):
    x0, y0 = pos1
    x1, y1 = pos2
    f = 0
    dx = x1 - x0
    dy = y1 - y0
    sy = 1
    sx = 1
    if dy < 0:
        dy = -dy
        sy = -1
    if dx < 0:
        dx = -dx
        sx = -1
    if dx >= dy:
        while x0 != x1:
            f = f + dy
            if f >= dx:
                if (x0 + (sx-1)/2, y0 + (sy-1)/2) in blocked:
                    return False
                y0 = y0 + sy
                f = f - dx
            if f != 0 and (x0 + (sx-1)/2, y0 + (sy-1)/2) in blocked:
                return False
            if dy == 0 and (x0 + (sx-1)/2, y0) in blocked and (x0 + (sx-1)/2, y0 - 1) in blocked:
                return False
            x0 = x0 + sx
    else:
        while y0 != y1:
            f = f + dx
            if f > dy:
                if (x0 + (sx-1)/2, y0 + (sy-1)/2) in blocked:
                    return False
                x0 = x0+sx
                f = f-dy
            if f != 0 and (x0 + (sx-1)/2, y0 + (sy-1)/2) in blocked:
                return False
            if dx == 0 and (x0, y0 + (sy-1)/2) in blocked and (x0 - 1, y0 + (sy-1)/2) in blocked:
                return False
            y0 = y0 + sy
    return True

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


#return a list of valid children positions
def findChildren(Node, goal, dimensions, blocked):
    listOfChildren = []
    position = Node.position
    x, y = position

    #iterate through 8 children, plus node itself
    for row in range(x-1,x+2):
        for col in range(y-1,y+2):
            #make sure node is not its own child
            if (row != x or col != y):
                child = row,col
                
                #print(isOpen(position,child, dimensions))
                if isOpen(position, child, dimensions, blocked):
                    listOfChildren.append(child)

    return listOfChildren
    

def updateVertex(nodeA, nodeB, openList, blocked):
    posA = nodeA.position
    posB = nodeB.position
    
    if nodeA.parent is not None and line_of_sight(nodeA.parent.position,posB, blocked):
        parent = nodeA.parent
        if parent.gvalue + findH(parent.position, nodeB.position) < nodeB.gvalue:
            nodeB.updateg(parent.gvalue + findH(parent.position, nodeB.position))
            nodeB.parent = parent
            

            if openList.contains(nodeB):
                openList.remove(nodeB)
            
            openList.insert(nodeB)

    else:
        
        cost = findH(nodeA.position, nodeB.position)

        if nodeA.gvalue + cost < nodeB.gvalue:
            nodeB.updateg(nodeA.gvalue+cost)
            nodeB.parent = nodeA
            if openList.contains(nodeB):
                openList.remove(nodeB)
        
            openList.insert(nodeB)

def main(file):
    #get basic graph info
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
    
    startH = findH(start, goal)

    startNode = node(start, startH, 0, None)
    openList.insert(startNode)

    closedList = []
    final_node = None
    nodes_traversed = 0

    
    while not openList.isEmpty():
        #print("open list size: ", openList.get_size())
        exploringNode = openList.pop()
        if exploringNode in closedList:
            continue
        nodes_traversed += 1
        
        if exploringNode.position == goal:
            final_node = exploringNode
            break

        closedList.append(exploringNode)

        children = findChildren(exploringNode, goal, dim, blocked)
        for i in children:
            # Check if i is in closedList
            skip_i = False
            for j in closedList:
                if i == j.position:
                    skip_i = True
                    break
            # if i in closedList, skip i
            if skip_i:
                continue

            if not openList.contains(node(i,0,0,None)):
                child = node(i, findH(i, goal), float('inf'), None)
                openList.insert(child)
            updateVertex(exploringNode, child, openList, blocked)

    path = []
    # if path found, final node is goal node
    if final_node is None:
        print("no path found")
    else:
        print("path found", "goal at ", final_node.position)

        i = final_node
        while i is not None:
            print(i.position)
            path.append(i.position)
            i = i.parent


    
    print('Nodes Traversed: ', nodes_traversed)
    return path


#main()

#file.close()