def checkPalindrome(inputString):
    mid = (len(inputString)-1//2)
    start = 0
    last = len(inputString)-1
    flag = 0
    while (start < mid):
        if (inputString[start] == inputString[last]):
            start += 1
            last -= 1
        else:
            flag = 1
            break
    if flag == 0:
       return True
    else :
       return False