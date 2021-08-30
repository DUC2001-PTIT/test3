def allLongestStrings(inputArray):
    max = len(inputArray[0])
    b = []
    c = -1
    for i in range(1,len(inputArray),1):
        if max < len(inputArray[i]):
            max = len(inputArray[i])
    for j in range(0,len(inputArray)):
        if len(inputArray[j]) == max :
            b.append(inputArray[j])
    return b 