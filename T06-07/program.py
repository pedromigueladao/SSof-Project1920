a = get()

if a:
    execute(a)
else:
    if a:
        execute(a)
    else:
        a = mogrify(a)
    a = mogrify(a)
execute(a)