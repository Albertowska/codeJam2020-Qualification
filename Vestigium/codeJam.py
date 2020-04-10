import numpy as np

totalCases = int(input())

# Go through all cases
for numCase in range(totalCases):
    # Get matrix size
    arraySize = int(input())

    # Initialize variables
    mat = np.zeros((arraySize,arraySize))
    colDuplicated = 0
    rowDuplicated = 0
    
    # Read all data
    for i in range(arraySize):
        mat[i]=input().split(" ")

    # Sum diagonal
    totalDiagonal = int(mat.diagonal().sum())

    # Calculate duplicated rows and colums
    for i in range(arraySize):
        # Check if all column elements are unique
        col = mat[:, i]
        if(np.unique(col).size != arraySize):
            colDuplicated +=1

        # Check if all row elements are unique
        row = mat[i, :]
        if(np.unique(row).size != arraySize):
            rowDuplicated +=1

    # Print result
    print("Case #{0}: {1} {2} {3}".format(numCase+1, totalDiagonal, rowDuplicated, colDuplicated))