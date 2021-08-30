def shapeArea(n):
    hanggiua = n + (n-1)
    giuahinh = (hanggiua // 2) + 1
    dt = hanggiua
    for i in range(giuahinh-1,0,-1):
        dt += (2*(hanggiua - 2 ))
        hanggiua = hanggiua -2
    return dt
