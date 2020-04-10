totalCases = int(input())

# Go through all cases
for numCase in range(totalCases):
    # Get total numbers
    numbers = input()

    # Initialize variables
    openPar = 0
    result = ""
    
    # Iterate through data
    for i in range(len(numbers)):
        num = int(numbers[i])
        if(num > openPar) : 
            for x in range(num - openPar):
                result += "("
            openPar = num
        elif (num < openPar) :
            for x in range(openPar - num):
                result += ")"
            openPar = num
        result += numbers[i]

    # Add ending parenthesis
    for x in range(openPar) :
        result += ")"

    # Print result
    print("Case #{0}: {1}".format(numCase+1, result))