a = "joao"
b = "vasco"
c = s();

src = ("%s %s %s" % a, b, s());

src = sanitize(src);

sink(src)
