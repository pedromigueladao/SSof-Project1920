if True:
    a = get()
    execute(a)
    if False:
        execute(a)
    else:
        execute(b)
else:
    execute(a)
