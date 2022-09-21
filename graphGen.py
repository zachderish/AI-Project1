import random

#create Square class
class Square:
    def __init__(self, closed, x, y):
        self.closed = closed
        self.x = x
        self.y = y

#generate if square is closed or open
def genSquares(xSize, ySize):
    squares = []
    numCells = int(xSize*ySize)
    #generate 10% random closed cells 
    randoms = random.sample(range(0,numCells),int(numCells*.1))
    print(len(randoms))
    counter = 0
    for row in range(xSize):
        for col in range(ySize):
            closed = 0
            #check if cell is closed
            if counter in randoms:
                closed = 1
            #add Square object to squares array
            square = Square(closed, row, col)
            squares.append(square)
            counter+=1
    return squares


#generating start and end points
def randomPoints(xSize, ySize):
    coor = []
    x1, y1 = random.randint(1,xSize), random.randint(1, ySize)
    coor.append(x1)
    coor.append(y1)
    x2, y2 = random.randint(1,xSize), random.randint(1,ySize)
    coor.append(x2)
    coor.append(y2)
    return coor

#writing text files
def writeFile(number, squares, rows, cols, coor):
    name = "graph" + str(number) + ".txt"
    with open(name,'w') as f:
        #writing start and end points, plus size of graph
        start = str(coor[0]) +" " + str(coor[1])
        end = str(coor[2]) +" " + str(coor[3])
        f.write(start)
        f.write('\n')
        f.write(end)
        f.write('\n')
        size = str(rows) + " " + str(cols)
        f.write(size)
        f.write('\n')
        #iterate to write squares' location and their closed status
        for square in range(len(squares)):
            f.write(str(squares[square].x))
            f.write(" ")
            f.write(str(squares[square].y))
            f.write(" ")
            f.write(str(squares[square].closed))
            f.write('\n')


def main(): 
    #user input
    rows = input("Enter number of rows: ")
    cols = input("Enter number of columns: ")
    squareNum = input("Enter number of graphs: ")

    for x in range(int(squareNum)):
        #call to generate squares
        rows = int(rows)
        cols = int(cols)
        squares = genSquares(rows, cols)

        #calls randomPoints for start and end points
        coor = randomPoints(rows, cols)

        #writes the .txt files for each graph
        writeFile(x, squares, rows, cols, coor)
main()