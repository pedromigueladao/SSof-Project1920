a = source(source3(source4()))
e = source5()
if True:
    b = source2()
    c = a + b
    if True and False:
        b = source3()
        c = a + e

sink(c)