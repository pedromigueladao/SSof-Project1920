a = True
while a:
    if(not a):
        a = get()
    else:
        execute(b)
    a = execute(mogrify(a))