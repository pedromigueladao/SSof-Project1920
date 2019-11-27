a = source()
b = source2()
c = source3()
d = source4()
e = a
f = b + c
g = 2*c + d
c = 1
print(sink(sink(e), c, sink(f), sink(g, 4*a)))