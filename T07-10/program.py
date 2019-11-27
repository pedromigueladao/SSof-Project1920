a = source()
b = 1
if a:
    a = 2
    if b:
        a = source3()
else:
    a = source2()
sink(a)