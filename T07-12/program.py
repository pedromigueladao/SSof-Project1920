a = source()
b = 1
x = 2
if x:
    a = 2
    if b:
        a = source3()
    elif c:
        a = source4()
    else:
        a = source5()
else:
    a = source2()
c = sink(a)
sink(c)