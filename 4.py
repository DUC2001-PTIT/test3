def adjacentElementsProduct(inputArray):
    max = inputArray[0] * inputArray[1]
    for i in range(1,len(inputArray)-1,1):
        j = i+1
        if max < (inputArray[i] *inputArray[j]):
           max = inputArray[i] *inputArray[j]
    return max