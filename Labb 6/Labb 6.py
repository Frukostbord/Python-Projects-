"""
All living cells with two or three neighbors survive.
All dead cells with three living neighbors are revived.
All other living cells die and already dead cells stay dead.
"""


import random
from graphics import *

class Cell:
    """A class representing cells"""

    def __init__(self,x,y):
        self._x = x
        self._y = y

    def coordinates(self):
        return (self._x, self._y)

    def neighbors(self):
        # Nested for-loop in a list comprehension
        result = [Cell(x_coord, y_coord) for x_coord in [self._x+1, self._x,self._x-1]
                  for y_coord in [self._y+1, self._y,self._y-1]]

        # Removes the coordinates same as the input
        result.pop(4)
        return result

    # Equality test for cells
    def __eq__(self,other):
        return self.coordinates() == other.coordinates()

    # Hash function for cells (necessary to use cells as keys in a dictionary)
    def __hash__(self):
        return self.coordinates().__hash__()

def randomWorld(width, height, proportion=3):
    # Nested for loop in a set comprehension for getting cells
    world = {Cell(w, h) for w in range(0, width) for h in range(0, height) if random.randint(1, 10) <= proportion}
    return world


def update(world):
    """Update the world by applying the rules of the game:
    1. Any live cell with two or three live neighbors survives.
    2. Any dead cell with three live neighbors becomes a live cell.
    3. All other live cells die in the next generation. Similarly,
       all other dead cells stay dead.
    """
    dead_cells = dict()
    counter = dict()
    result = set()

    # Getting coordinates
    world = [c.coordinates() for c in world]

    # Getting all the neighbors for each living cell
    for living_cells in world:
        counter[living_cells] = 0
        neighbors = (cell.coordinates() for cell in Cell(living_cells[0], living_cells[1]).neighbors())

        # Counting the alive neighbors for each cell and counting dead cells
        for cells in neighbors:
            if cells in world:
                counter[living_cells] += 1
            if cells not in counter.keys():
                dead_cells[cells] = 0

        # Adding the cells that survive (2 or 3 neighbors)
        if counter[living_cells] == 2 or counter[living_cells] == 3:
            result.add(Cell(living_cells[0],living_cells[1]))

    # Counting living cells next to dead cells
    for dead_cell in dead_cells.keys():
        neighbors = (cell.coordinates() for cell in Cell(dead_cell[0], dead_cell[1]).neighbors())

        for cells in neighbors:
            if cells in counter.keys():
                dead_cells[dead_cell] += 1

        # Reviving dead cells if they have 3 neighbors
        if dead_cells[dead_cell] == 3:
            result.add(Cell(dead_cell[0], dead_cell[1]))

    return result


## Extra functions for shifting and combining worlds

def shiftWorld(w,dx=0,dy=0):
    """Shift a world dx steps in x direction and dy steps in y direction"""
    out = set()

    for c in w:
        (x,y) = c.coordinates()
        out.add(Cell(x+dx,y+dy))

    return out

def unionWorlds(ws):
    """Compute the union of a list of worlds"""
    out = set()

    for w in ws:
         for c in w:
            out.add(c)

    return out


## Some fun starting worlds:

# One glider
# https://www.conwaylife.com/wiki/Glider
glider = { Cell(x,y) for (x,y) in [(2,1),(3,2),(1,3),(2,3),(3,3)] }

# Two gliders
# glider2 = unionWorlds([glider,shiftWorld(glider,10)])

# Many gliders and an obstacle
# manygliders = unionWorlds([ shiftWorld(glider,dx,dy)
#                             for dx in [0,10,20]
#                                 for dy in [0,10,20] ] +
#                           [ { Cell(x+32,30) for x in range(20) }])


## Code for displaying the world and running the animation

def display(width,height,world, win, rectangles):
    for x in range(width):
        for y in range(height):
            rectangles[y][x].setFill("black" if Cell(x,y) in world else "white")
    win.update()

## The main method
def main():
    # Number of iterations to run animation
    iterations = 1000

    # Size of squares
    k = 10

    # Width of window (will be multiplied by k)
    width  = 60

    # Height of window (will be multiplied by k)
    height = 60

    # Create a window
    win = GraphWin("Game of Life", width * k, height * k, autoflush=False)

    # Create rectangles grid
    rectangles = [ [ Rectangle(Point(j * k, i * k)
                              ,Point((j + 1) * k, (i + 1) * k))
                   for j in range(width)]
                 for i in range(height)]

    # Draw rectangles in window
    for x in range(width):
        for y in range(height):
            rectangles[y][x].draw(win)

    # Initialize the world randomly
    world = randomWorld(width,height)

    # Uncomment to initialize with one glider
    # world = glider

    # Uncomment to initialize with two gliders
    # world = glider2

    # Uncomment to initialize with many gliders and an obstacle
    # world = manygliders

    # Run simulation "iterations" number of steps
    for i in range(iterations):
        # Draw the world
        display(width,height,world,win,rectangles)

        # Update the state of the world
        world = update(world)

    # Close the window and quit when we are done
    win.close()
    quit()

# Uncomment to run the animation
main()



"""
c = Cell(2,3)
print(c.coordinates())
print(c.coordinates() == (2,3))

print([x.coordinates() for x in c.neighbors()])
print([x.coordinates() for x in Cell(0,0).neighbors()])

print([c.coordinates() for c in randomWorld(10,10)])


print(update([c.coordinates() for c in randomWorld(10,10)]))



print(update(set()))
#set()
print(update({Cell(0,0)}))
#set()
line = {Cell(1,1), Cell(2,1), Cell(3,1)}
print([x.coordinates() for x in line])
#[(3, 1), (1, 1), (2, 1)]
print([x.coordinates() for x in update(line)])
#[(2, 0), (2, 1), (2, 2)]
print([x.coordinates() for x in update(update(line))])
#[(3, 1), (1, 1), (2, 1)]
print([x.coordinates() for x in update(update(update(line)))])
#[(2, 0), (2, 1), (2, 2)]
print([x.coordinates() for x in update(update(update(update(line))))])
#[(3, 1), (1, 1), (2, 1)]

"""