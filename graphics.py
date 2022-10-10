from tkinter import *
import math
import astar
import thetastar
from astar import node as nodeA
from thetastar import node as nodeTheta
#WORK IN PROGRESS

file = None 
#cell class
class Cell():
    def __init__(self, closed, x, y):
        self.closed = closed
        self.x = x-1
        self.y = y-1

#create cell
def createCell(cell, my_canvas, dimFactor):
    if(cell.closed == 0):
        my_canvas.create_rectangle(cell.x*dimFactor, cell.y*dimFactor, (cell.x+1)*dimFactor, (cell.y+1)*dimFactor, outline='grey')
    else:
        my_canvas.create_rectangle(cell.x*dimFactor, cell.y*dimFactor, (cell.x+1)*dimFactor, (cell.y+1)*dimFactor, outline='grey', fill='grey')

#create start and end points on screen
def createPoints(startCoor, endCoor, canvas, dimFactor):
    x1 = startCoor[0]-1
    y1 = startCoor[1]-1
    x2 = endCoor[0]-1
    y2 = endCoor[1]-1
    #creates text
    message1 = "start: (" + str(x1+1) + "," + str(y1+1) + ")"
    canvas.create_text(x1*dimFactor+50, y1*dimFactor+20, text=message1)
    message2 = "end: (" + str(x2+1) + "," + str(y2+1) + ")"
    canvas.create_text(x2*dimFactor+50, y2*dimFactor+20, text=message2)

    #creates dots
    canvas.create_oval(x1*dimFactor-5, y1*dimFactor-5, x1*dimFactor+5, y1*dimFactor+5,fill='green')
    canvas.create_oval(x2*dimFactor-5, y2*dimFactor-5, x2*dimFactor+5, y2*dimFactor+5,fill='red')

def createLines(startCoor, endCoor, canvas, dimFactor):
    x1 = startCoor[0]-1
    y1 = startCoor[1]-1
    x2 = endCoor[0]-1
    y2 = endCoor[1]-1

    canvas.create_line(x1*dimFactor, y1*dimFactor, x2*dimFactor, y2*dimFactor, fill='red')

def createGraph(root, dimensions, startCoor, endCoor, closed, path, nodes):
    #create canvas widget
    my_canvas = Canvas(root, height=1500, width=1500, bg="white")
    my_canvas.delete("all")
    
    #create cell input
    node = Entry(root, width=50)    
    btn = Button(root, width=20, text="Get Values at Cell", command = lambda: getValues(my_canvas, node, nodes))
    node.pack()
    btn.pack()

    my_canvas.pack(pady=20)

    #ensure equally spaced cells
    print(dimensions)
    large = max(dimensions)
    dimFactor = math.floor(1000/large)

    #call to create cells
    for cell in closed:   
            createCell(cell, my_canvas, dimFactor)

    #call to create labels for start and end points
    createPoints(startCoor, endCoor, my_canvas, dimFactor)

    #call to create path
    i = 1
    while i < len(path):
        createLines(path[i-1], path[i], my_canvas, dimFactor)
        i+=1

    root.mainloop()

#get requested values from coordinate
def getValues(canvas, cell, nodes):
    print(nodes)
    cell = cell.get()
    cell = cell.split(" ")
    cell = (int(cell[0]), int(cell[1]))
    for node in nodes:
        if node.position[0] == cell[0] and node.position[1] == cell[1]:
            message = str(cell[0]) + "," + str(cell[1]) + " g: " + str(node.gvalue) + " h: " + str(node.hvalue) + " f: " + str((node.hvalue+node.gvalue))
            print(message)
            #canvas.create_text(500, 1200, text=message)

#read user input and text file
def getText(root, file, alg):
    path = file

    #store coordinates in lists
    with open(path) as f:
        #get nodes from a star
        nodes = None
        path = None
        if alg == 0:
            path, nodes = astar.main(f)
        if alg == 1:
            path = thetastar.main(f)
        #print(path)
        #print(nodes)

        #read start coor
        dimensions = []
        startCoor = []
        endCoor = []
        closed = []
        f.seek(0)
        start = f.readline()
        for num in start.split():
            startCoor.append(int(num))
        #read end coor
        end = f.readline()
        for num in end.split():
            endCoor.append(int(num))
        #read dimensions
        dim = f.readline()
        print(dim)
        for num in dim.split():
            dimensions.append(int(num))
        #read cells
        for line in f:
            line = line.split(' ')
            newCell = Cell(int(line[2]), int(line[0]), int(line[1]))
            closed.append(newCell)
        
        createGraph(root, dimensions, startCoor, endCoor, closed, path, nodes)

    #print(startCoor, endCoor, dimensions)
    f.close()

#create graph btn function 
def getFile(root, graph, alg):
    print("clicked")
    file = graph.get()
    getText(root, file, alg)

#store coordinates in lists
def main():
    root = Tk()
    root.title('A*')
    root.geometry("500x500")
    #create entry and button for graph selection
    label = Label(root, width=50, text="file path:")
    graph = Entry(root, width=50)
    aButton = Button(root, width=20, text="Run A*", command= lambda: getFile(root, graph, 0))
    thetaButton = Button(root, width=20, text="Run theta*", command = lambda: getFile(root, graph, 1))
    label.pack()
    graph.pack()
    aButton.pack()
    thetaButton.pack()
    #create cell input
    #cell = Entry(root, width=50)
    #btn = Button(root, width=20, text="Get Values at Cell", command= lambda: getValues(root, graph))
    #cell.pack()
    #btn.pack()

    root.mainloop()

main()
