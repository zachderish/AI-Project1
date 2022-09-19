from tkinter import *
#WORK IN PROGRESS

#create border
def createBorder(dimensions):
    root = Tk()
    root.title('A*')
    root.geometry("500x500")

    #create canvas widget
    my_canvas = Canvas(root, width=100, height=100, bg="white")
    my_canvas.pack(pady=20)

    #create rectangle
    my_canvas.create_rectangle(0, 0, dimensions[0], dimensions[1], outline='grey')

    root.mainloop()
#store coordinates in lists
def main():
    #user input
    txtFile = input("file name: ")

    #open file (must be in graphs folder)
    path = 'graphs/' + txtFile

    #store coordinates in lists
    startCoor = []
    endCoor = []
    dimensions = []
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
    #print(startCoor, endCoor, dimensions)
    createBorder(dimensions)
    f.close()

main()