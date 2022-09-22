from cmath import sqrt
import heap

#Opens the graph file that is being explored
file = open('graph0.txt', 'r')

#The NODE Class
class node:
    def __init__(self, position, hvalue, gvalue, fvalue, childList):
        self.position = position
        self.hvalue = hvalue
        self.gvalue = gvalue
        self.fvalue = fvalue
        self.childList = childList

def findH(startx, starty, goalx, goaly):
    return sqrt(pow(abs(startx - goalx), 2) + pow(abs(starty - goaly), 2))

#Function for finding a list of children (DOES NOT ACCOUNT FOR EDGE CASES) (DOES NOT INITIALIZE CHILDREN OR ADD THEM TO THE OPEN LIST)
#Input the position of a node and returns a list of it's children which aren't blocked
def findChildren(position):
    listOfChildren = []
    x = position[0] - 1
    
    while x < (position[0] + 1):
        y = position[1] - 1
        
        while y < (position[1] + 1):  
            #The formula for determining which line to read from the file is ((x*50)+y)+3
            tempTuple = tuple(map(int, file.readlines()[((x * 50) + y) + 3].split()))
            
            if (tempTuple[0] == position[0]) and (tempTuple[1] == position[1]):
                #This is the position of the node that is being explored
                continue

            #If the node is blocked
            if tempTuple[2] == 0:
                listOfChildren.append(tempTuple)
    
    return listOfChildren

def updateVertex(nodeA, nodeB):
    nodeA.gvalue

def main():
    
    #Depends on how the program will access the graph files, opens file and gets start and goal positions
    startPosition = tuple(map(int, file.readlines()[0].split()))
    goalPosition = tuple(map(int, file.readlines()[1].split()))

    #Create Fringe and set it to null, or empty
    openList = heap()
    
    #Find Values of First Node and insert first node into the heap
    tempHValue = findH(startPosition[0], startPosition[1], goalPosition[0], goalPosition[1])
    tempChildList = findChildren(startPosition)
    startNode = node(startNode, tempHValue, 0, tempHValue+0, tempChildList)
    heap.insert(openList, startNode)

    #Create a Closed List
    closedList = []

    #Algorithm starts searching for the goal
    while heap.isEmpty(openList):
        exploringNode = openList.pop()
        
        if exploringNode.position == goalPosition:
            return "Path Found!!!"

        closedList.append(exploringNode)

        #For each child:
            #If child is NOT in the closed list
                #If child is NOT in the fringe
                    #G-Value of the child is Infinity?
                    #Set Parent of child to NULL/
            #updateVertex()


    return "No Path Found."


main()

"""""
#Function for adding all the children of whatever node is passed as a parameter into the open list
def initChildren(exploringNode):
    for x in exploringNode.childList:
        tempHValue = sqrt(pow(abs(x[0] - endPosition[0]), 2) + pow(abs(x[1] - endPosition[1]), 2))
        tempGValue = 0
        
        #Check to see if the traveral value is 1 or 1.41
        if (exploringNode.position[0] != x[0]) and (exploringNode.position[1] != x[1]):
            tempGValue = exploringNode.gvalue + 1.41
        else:
            tempGValue = exploringNode.gvalue + 1

        tempFValue = tempHValue + tempGValue
        tempList = x.findChildren()
        openList.append(node((x[0], x[1]), tempHValue, tempGValue, tempFValue, tempList))

#Generate the first node and add the children to the open list
startPosition = tuple(map(int, file.readlines()[0].split()))
staPosHVal = sqrt(pow(abs(startPosition[0] - endPosition[0]), 2) + pow(abs(startPosition[1] - endPosition[1]), 2))
tempList = findChildren(startPosition)

#Add start node to the closed list
closedList.append(node(startPosition, staPosHVal, 0, staPosHVal + 0, tempList))

#Initialize children of the first node so the program can start searching in directions
initChildren(closedList[0])

#The A* Algorithm
while len(openList) > 0: #While there exist potential paths to explore in the open list
   
#STEP 1: FIND THE NODE IN THE LIST WITH THE LEAST F-VALUE   
    #Child with lowest f-value is the first in the open list
    lowestf = 0
    lowestfPosition = openList[0]
    
    #Loop through open list to find node with the lowest f-value
    for x in openList:
        if x.fvalue < lowestf:
            lowestf = x.fvalue
            lowestfPosition = x
            
    #LowestfPosition is now the position in the list with the lowest F-Value
    removedNode = openList.pop(lowestfPosition)
    
    #Add children from the 
    initChildren(removedNode)
    """""