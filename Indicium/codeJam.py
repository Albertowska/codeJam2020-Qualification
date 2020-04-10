import itertools
import operator
import sys
import numpy as np

# Check if matrix valid
def valid(cols_so_far):
    for i, col1 in enumerate(cols_so_far):
        for col2 in cols_so_far[i + 1:]:
            if any(map(operator.eq, col1, col2)):
                return False
    return True

# Get matrix generator
def enum(values, k, cols_so_far=None):
    if cols_so_far is None:
        cols_so_far = (tuple(values),)
    if not valid(cols_so_far):
        pass
    elif len(cols_so_far) == k:
        yield tuple(zip(*cols_so_far))  # transpose
    else:
        for perm in itertools.permutations(values):
            yield from enum(values, k, cols_so_far + (perm,))

# Print possible solution
def printPossible(myArray, numCase):
    print("Case #{0}: POSSIBLE".format(numCase+1))
    for row in myArray:
        print(' '.join(map(str,row)))


# Get total number of cases
totalCases = int(input())

for numCase in range(totalCases):
    line = input().split(" ")
    matrixSize = int(line[0])
    reqSum = int(line[1])

    possible = False

    # Get tuple with number and matrix generator
    myTuple = tuple((ele) for ele in range(1, matrixSize+1))
    generator = enum({*myTuple}, matrixSize)

    # Try for all possible solutions
    for item in generator:
        myArray = np.asarray(item)
        flipHorArray = np.fliplr(myArray)
        # Sum diagonal to check if possible
        if(myArray.diagonal().sum() == reqSum):
            printPossible(myArray, numCase)
            possible = True
            break;
        # Try reverse diagonal
        elif(flipHorArray.diagonal().sum() == reqSum):
            printPossible(flipHorArray, numCase)
            possible = True
            break;

    if(possible==False):
        print("Case #{0}: IMPOSSIBLE".format(numCase+1))