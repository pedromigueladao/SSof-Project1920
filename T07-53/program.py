a = source()
b = 0
c = 0
d = 0
while b:
    d = c
    c = b
    b = a

q = sink(d)