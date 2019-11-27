i = source()
if i != '':
    i = sanitizer(i)
sink(i)
