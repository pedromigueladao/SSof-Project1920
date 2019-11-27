a = source()
b = 1
while a:
    a = 2
    while b:
        a = source3()
else:
    a = source2()
c = sink(a)
sink(c)