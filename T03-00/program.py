a = "Hello World"
while True:
    execute(a)
    a = escape_string(a)
    raw(a)
    a = mogrify(a)
    a = a + get() + get_object_or_404() + ContactMailForm()
