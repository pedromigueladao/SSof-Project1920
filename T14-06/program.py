a = "joao"
b = "vasco"
c = s();

src = ("%s %s %s" % a, b, s());

c = sanitize(c);

sink(src)
