def sortByHeight(a):
    b = []
    nho = 0
    for i in range(0,len(a),1):
        if a[i] == -1:
            break
        if a[i] != -1 and i == (len(a)-1):
            a.sort()
            return a
    for i in range(0,len(a)-1,1):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
               nho = a[i]
    for i in range(0,len(a),1):
        if a[i] == nho :
            b.append(i)
    print(len(b))
    for i in range(0,len(b)):
        a.remove(nho)
    a.sort()
    for j in range(0,len(b),1):
        a.insert(b[j],nho)
    return a
    