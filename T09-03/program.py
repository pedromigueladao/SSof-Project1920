a = (1,2,3,5)
raw(a[0])
a[0] = get("user")
a[0] = clean(a[0])
a[1] = get("password")
a[1] = mogrify(a[1])
raw(a[0],a[1])