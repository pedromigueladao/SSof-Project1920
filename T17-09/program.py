a = source()
b = a and sanitizer(a) or True
sink(b)
