filename = raw_input()
filename = ourSanitizer(filename)

eval(open(filename))
