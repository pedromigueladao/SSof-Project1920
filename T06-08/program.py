a = get()

if a:
    execute(a)
else:
    a = mogrify(a)

execute(a)