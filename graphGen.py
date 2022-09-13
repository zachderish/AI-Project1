import random

class Square:
    def __init__(self, closed):
        self.closed = closed
squares = []
for x in range(8):
    closed = False
    odds = random.random()
    print(odds)
    if(odds <= .1):
        closed = True
    square = Square(closed)
    squares.append(square)
for square in squares:
    print(square.open)

odds = random.randint(1,4)
print(odds)