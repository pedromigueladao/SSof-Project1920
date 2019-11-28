a, b = get_value(c)
src = get_name()

# sanitizing b, and executing it on a sink -> no vulnerability expected
b = shower(b)
example.util.response.Response(b)

# tainting b again, and then executing it on a sink -> vulnerability expected
b = src
jinja2.Markup(b.get())

# executing a on a sink, but sanitizing it before executing -> no vulnerability expected
jinja2.Markup(shower(a))
