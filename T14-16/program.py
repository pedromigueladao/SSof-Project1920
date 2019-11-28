a, b = get_value(c)
src = get_name()

# sanitizing b and returning it to d - b is still tainted, but d is not.

d = shower(b)
example.util.response.Response(d) # no vulnerability expected

example.util.response.Response(b) # vulneratibility expected

bath(b)

# sanitizing b and then executing it on a sink -> no vulnerability expected
jinja2.Markup(b.get())

# executing a on a sink, but sanitizing it before executing -> no vulnerability expected
jinja2.Markup(bath(a))
