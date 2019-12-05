a = ContactMailForm("user")
b = "user"
c = b + a
RawSQL(c)
d = "ola" + b
mark_safe(d)
c = flatatt(c)
e = Response(c)