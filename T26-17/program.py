a = source()
if True:
    b = sanitizer2(a)
else:
    b = sanitizer(a)

sink(b)
