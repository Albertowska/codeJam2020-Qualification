import sys
import numpy as np

# Apply action
def applyAction(action, solArray):
    if(action[1]):
        #Reverse array
        solArray = list(reversed(solArray))
    elif(action[2]):
        #Complement array
        solArray = np.array([complement(i) for i in solArray])
    elif(action[3]):
        #Complement and Reverse
        solArray = np.array([complement(i) for i in solArray])
        solArray = list(reversed(solArray))
    return solArray

# Complement matrix
def complement(num):
    if(num == 0):
        return 1
    elif(num == 1):
        return 0
    else:
        return num

# Ask next number
def askNext(index):
    print(index)
    sys.stdout.flush()
    return int(input())

def askAndAssign(solArray, index, times):
    num = askNext(index)
    solArray[index-1] = num
    return times+1

# Read total cases and size
line = input().split(" ")
totalCases = int(line[0])
arraySize = int(line[1])

# Iterate through all cases
for numCase in range(totalCases):
    times = 1
    solArray = np.full(arraySize, 2)
    solucion = False

    nextToAsk = 1

    # Iterate until we get solution 
    while (not solucion):
        # Guess what change happened
        if(times != 1 and times % 10 == 1):
            nextToAskTemp = 1
            
            # Nothing, Reverse, Complement, Both
            action = [True, True, True, True]
            existsNext = True

            actionApplied = False
            while (not actionApplied and existsNext):
                s = askNext(nextToAskTemp)
                times+=1

                # Discard actions applied
                if(solArray[nextToAskTemp-1] != s):
                    action[0] = False
                if (solArray[arraySize - nextToAskTemp] != s):
                    action[1] = False
                if (solArray[nextToAskTemp-1] == s):
                    action[2] = False
                if (solArray[arraySize - nextToAskTemp] == s):
                    action[3] = False
                
                # Find pair of numbers equal and different to find action applied
                areEqual = (solArray[nextToAskTemp-1] == solArray[arraySize - nextToAskTemp])
                existsNext = False
                
                 # Find next val to check which is different or equal
                for a in range(nextToAskTemp, arraySize):
                    if (areEqual and solArray[a] != solArray[arraySize - a - 1] and solArray[a] != 2):
                        nextToAskTemp = a + 1
                        existsNext = True
                        break
                    elif (not areEqual and solArray[a] == solArray[arraySize - a - 1] and solArray[a] != 2):
                        nextToAskTemp = a + 1
                        existsNext = True
                        break
                    
                # Check if only 1 true
                actionApplied = (sum(action) == 1)

            solArray = applyAction(action, solArray)

        # Ask next number
        times = askAndAssign(solArray, nextToAsk, times)

        # Avoid asking after a change
        if(times % 10 != 1):
            # Ask last minus next
            last = (arraySize - nextToAsk + 1)
            times = askAndAssign(solArray, last, times)

            nextToAsk+=1
        
        solucion = not 2 in solArray

    # Print solution
    print(''.join(map(str,solArray)))

    # Read solution
    if (input() == "N"):
        break