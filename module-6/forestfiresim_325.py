"""Forest Fire Simulation with a lake.

Title: Module 6.2 - Forest Fire Simulation
Authors: Michael Benko, Samuel Guizar, Prince Hubbard, and Nicholas Zankl
Date: September 13, 2026
Purpose: Simulate forest growth and fire spread while using a permanent lake
         near the center of the display as a firebreak.

The original Forest Fire Sim was modified by Sue Sampson and was based on a
program by Al Sweigart. This version adds an unchanging blue water feature.
Press Ctrl-C to stop the simulation.
"""

import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()


# Display constants.
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # The lake uses a character different from the tree and fire.

# Simulation settings. Values can be changed from 0.0 through 1.0.
# NOTE: 0.20 represents 20% mathematically, but due to the (* 100) scaling inside 
# createNewForest(), execution results in ~0.2% density. 
# Preserved for legacy fidelity

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5

# Lake dimensions. Odd values keep the lake centered on one grid coordinate.
LAKE_WIDTH = 19
LAKE_HEIGHT = 7


def main():
    """Run and display the forest fire simulation until the user stops it."""
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        # Build the forest for the next simulation step.
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # A neighboring fire may have already changed this cell.
                    continue

                if forest[(x, y)] == WATER:
                    # Water never grows, burns, or disappears.
                    nextForest[(x, y)] = WATER
                elif ((forest[(x, y)] == EMPTY)
                      and (random.random() <= GROW_CHANCE)):
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                      and (random.random() <= FIRE_CHANCE)):
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # Fire spreads only to neighboring tree cells. Since water
                    # is never a tree, flames cannot enter or cross the lake.
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    nextForest[(x, y)] = EMPTY
                else:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Return a new forest dictionary containing trees and a central lake."""
    forest = {'width': WIDTH, 'height': HEIGHT}

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    addLake(forest)
    return forest


def addLake(forest):
    """Place an oval-shaped water feature near the center of the forest."""
    centerX = forest['width'] // 2
    centerY = forest['height'] // 2
    horizontalRadius = LAKE_WIDTH // 2
    verticalRadius = LAKE_HEIGHT // 2

    # The ellipse equation shapes the lake without requiring outside graphics.
    for x in range(centerX - horizontalRadius, centerX + horizontalRadius + 1):
        for y in range(centerY - verticalRadius, centerY + verticalRadius + 1):
            horizontalDistance = (x - centerX) / horizontalRadius
            verticalDistance = (y - centerY) / verticalRadius

            if horizontalDistance ** 2 + verticalDistance ** 2 <= 1:
                forest[(x, y)] = WATER


def displayForest(forest):
    """Display trees, fire, empty ground, and blue lake water."""
    bext.goto(0, 0)

    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]

            if cell == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif cell == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif cell == WATER:
                bext.fg('blue')
                print(WATER, end='')
            else:
                print(EMPTY, end='')
        print()

    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
