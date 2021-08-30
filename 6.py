def makeArrayConsecutive2(statues):
    statues.sort()
    canthem = 0 
    for i in range(0,len(statues)-1,1):
        j = i +1
        if statues[j] > statues[i]:
            canthem += (statues[j] - statues[i] -1)
    return canthem
    