import numpy as np

totalCases = int(input())

# Go through all cases
for numCase in range(totalCases):
    # Get number of activities
    numActivities = int(input())

    # Initialize variables
    result =  ""
    resultArray = []
    activities = np.empty((numActivities, 3), dtype=int)

    # Read all activities
    for i in range(numActivities):
        inputVals = input().split()
        activities[i] = [i, inputVals[0], inputVals[1]]

    # Order by start time
    orderActivities = activities[activities[:,1].argsort()]
    endTimeC = 0
    endTimeJ = 0

    for act in orderActivities:
        if(endTimeC <= act[1]):
            resultArray.append([act[0], "C"])
            endTimeC = act[2]
        elif(endTimeJ <= act[1]):
            resultArray.append([act[0], "J"])
            endTimeJ = act[2]
        else:
            result = "IMPOSSIBLE"
            break

    # If schedule is possible
    if(result == "") :
        # Order resultArray and get printable string
        resultArray = sorted(resultArray, key = lambda x : x[0])
        result = result.join([row[1] for row in resultArray])
        
    # Print result
    print("Case #{0}: {1}".format(numCase+1, result))