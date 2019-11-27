a = source()
if True:
    b = 3
else:
    b = sanitizer(a)

sink(b)