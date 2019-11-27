a = source()
if True:
    b = a + 3
else:
    b = sanitizer(a)

sink(b)