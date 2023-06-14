#                     Conway's Game of Life
#                  --------------------------
#
# Original version by Guillaume Brunerie, adapted by Anders Mörtberg.

import random
from graphics import *


class Cell:
    """A class representing cells"""

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def coordinates(self):
        """Return the coordinates of the cell as a tuple"""
        return self._x, self._y

    def neighbors(self):
        """Compute the neighbors of a cell"""
        dx = [-1, 0, 1]  # A list for differences in x values to run through
        neighbors_list = []
        for i in dx:  # Runs through the dx list and applies -1,0 and +1 on each y
            neighbors_list.append(Cell(self._x + i, self._y - 1))
            if i != 0:  # By not adding a value where x and y both == 0, you dont add the current cell to its list with neighbours.
                neighbors_list.append(Cell(self._x + i, self._y))
            neighbors_list.append(Cell(self._x + i, self._y + 1))
        return neighbors_list

        # Equality test for cells

    def __eq__(self, other):
        return self.coordinates() == other.coordinates()

    # Hash function for cells (necessary to use cells as keys in a dictionary)
    def __hash__(self):
        return self.coordinates().__hash__()


def randomWorld(width, height, proportion=3):
    """Return a random world"""
    world = set()
    for x in range(0, width - 1):
        for y in range(0, height - 1):
            if random.randint(1,
                              10) <= proportion:  # Random cell between 1 and 10 being lower or equal to proportion, default 3, gives the proportion of cells being alive
                world.add(Cell(x, y))

    return world


def update(world):
    """Update the world by applying the rules of the game:

    1. Any live cell with two or three neighbors survives.
    2. Any dead cell with three live neighbors becomes a live cell.
    3. All other live cells die in the next generation. Similarly,
       all other dead cells stay dead.
    """
    counter = {}
    result = set()
    alive = set()

    for c in world:  # cycle through all cells given in through world
        alive.add(c.coordinates())  # A set list of cells being alive at the start
        for x in c.neighbors():  # Checks all neighbours to alive cells and adds 1 to the counter for that cell.
            if x.coordinates() in counter:  # If the the cell have already been added to counter, add one more, otherwise add a first counter to it.
                counter[x.coordinates()] += 1
            else:
                counter[x.coordinates()] = 1

    for c in alive:  # If cell started alive and has 2 or 3 alive neighbours it stays alive.
        if c in counter.keys():
            if counter[c] == 2 or counter[c] == 3:
                result.add(Cell(c[0], c[
                    1]))  # cycle thruogh the tuple and adds first number as x and secound as y to init the Cell.

    for key, value in counter.items():  # If a dead cell has 3 alive neighbours it gets resurrected and is alive. The set list prevents duplicates
        if value == 3:
            result.add(Cell(key[0], key[
                1]))  # cycle thruogh the tuple and adds first number as x and secound as y to init the Cell.

    return result


## Extra functions for shifting and combining worlds

def shiftWorld(w, dx=0, dy=0):
    """Shift a world dx steps in x direction and dy steps in y direction"""
    out = {}
    for c in w:
        (x, y) = c.coordinates()
        out[Cell(x + dx, y + dy)] = True
    return out


def unionWorlds(ws):
    """Compute the union of a list of worlds"""
    out = {}
    for w in ws:
        for c in w:
            out[c] = True
    return out


## Some fun starting worlds:

# One glider
# https://www.conwaylife.com/wiki/Glider
glider = {Cell(x, y): True for (x, y) in [(2, 1), (3, 2), (1, 3), (2, 3), (3, 3)]}

# Two gliders
glider2 = unionWorlds([glider, shiftWorld(glider, 10)])

# Many gliders and an obstacle
manygliders = unionWorlds([shiftWorld(glider, dx, dy)
                           for dx in [0, 10, 20]
                           for dy in [0, 10, 20]] +
                          [{Cell(x + 32, 30): True for x in range(20)}])


## Code for displaying the world and running the animation

def display(width, height, world, win, rectangles):
    for x in range(width):
        for y in range(height):
            rectangles[y][x].setFill("black" if Cell(x, y) in world else "white")
    win.update()


## The main method
def main():
    # Number of iterations to run animation
    iterations = 1000

    # Size of squares
    k = 10

    # Width of window (will be multiplied by k)
    width = 60

    # Height of window (will be multiplied by k)
    height = 60

    # Create a window
    win = GraphWin("Game of Life", width * k, height * k, autoflush=False)

    # Create rectangles grid
    rectangles = [[Rectangle(Point(j * k, i * k)
                             , Point((j + 1) * k, (i + 1) * k))
                   for j in range(width)]
                  for i in range(height)]

    # Draw rectangles in window
    for x in range(width):
        for y in range(height):
            rectangles[y][x].draw(win)

    # Initialize the world randomly
    world = randomWorld(width, height)

    # Uncomment to initialize with one glider
    # world = glider

    # Uncomment to initialize with two gliders
    # world = glider2

    # Uncomment to initialize with many gliders and an obstacle
    # world = manygliders

    # Run simulation "iterations" number of steps
    for i in range(iterations):
        # Draw the world
        display(width, height, world, win, rectangles)

        # Update the state of the world
        world = update(world)

    # Close the window and quit when we are done
    win.close()
    quit()


# Uncomment to run the animation
main()



c = Cell(2,3)
#print(c.coordinates())
#print(c.coordinates() == (2,3))
#print([ x.coordinates() for x in c.neighbors() ])
#print([ x.coordinates() for x in Cell(0,0).neighbors() ])
print([ c.coordinates() for c in randomWorld(10,10) ])

print(update(set()))

#set()

print(update({ Cell(0,0) }))

#set()

line = { Cell(1,1) , Cell(2,1), Cell(3,1) }

print([ x.coordinates() for x in line])

#[(3, 1), (1, 1), (2, 1)]

print([ x.coordinates() for x in update(line)])

#[(2, 0), (2, 1), (2, 2)]

print([ x.coordinates() for x in update(update(line))])

#[(3, 1), (1, 1), (2, 1)]

print([ x.coordinates() for x in update(update(update(line)))])

#[(2, 0), (2, 1), (2, 2)]

print([ x.coordinates() for x in update(update(update(update(line))))])

#[(3, 1), (1, 1), (2, 1)]