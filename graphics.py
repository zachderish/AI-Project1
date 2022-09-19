from cgitb import text
from mimetypes import init
from tkinter import *
import math
from tracemalloc import start
#WORK IN PROGRESS

#cell class
class Cell():
    def __init__(self, closed, x, y):
        self.closed = closed
        self.x = x
        self.y = y

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
    canvas.create_oval(x1*dimFactor-1, y1*dimFactor-1, x1*dimFactor+5, y1*dimFactor+5,fill='green')
    canvas.create_oval(x2*dimFactor-1, y2*dimFactor-1, x2*dimFactor+5, y2*dimFactor+5,fill='red')

def createGraph(root, dimensions, startCoor, endCoor, closed):
    #create canvas widget
    my_canvas = Canvas(root, height=1500, width=1500, bg="white")
    my_canvas.pack(pady=20)

    #ensure equally spaced cells
    large = max(dimensions)
    dimFactor = math.floor(1000/large)

    #call to create cells
    for cell in closed:   
            createCell(cell, my_canvas, dimFactor)

    #call to create labels for start and end points
    createPoints(startCoor, endCoor, my_canvas, dimFactor)

    root.mainloop()

#read user input and text file
def getText(root, file):
    path = file

    #store coordinates in lists
    startCoor = []
    endCoor = []
    dimensions = []
    closed = []
    with open(path) as f:
            #read start coor
            start = f.readline()
            for num in start.split():
                startCoor.append(int(num))
            #read end coor
            end = f.readline()
            for num in end.split():
                endCoor.append(int(num))
            #read dimensions
            dim = f.readline()
            for num in dim.split():
                dimensions.append(int(num))
            #read cells
            for line in f:
                line = line.split(' ')
                newCell = Cell(int(line[2]), int(line[0]), int(line[1]))
                closed.append(newCell)

    #print(startCoor, endCoor, dimensions)
    createGraph(root, dimensions, startCoor, endCoor, closed)
    f.close()

#create graph btn function 
def getFile(root, graph):
    print("clicked")
    file = graph.get()
    getText(root, file)

    

#store coordinates in lists
def main():
    root = Tk()
    root.title('A*')
    root.geometry("500x500")
    #creat entry and button for graph selection
    label = Label(root, width=50, text="file path:")
    graph = Entry(root, width=50)
    button = Button(root, width=20, text="Create Graph", command= lambda: getFile(root, graph))
    label.pack()
    graph.pack()
    button.pack()
    root.mainloop()

main()