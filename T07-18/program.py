a = X_source()
b = Y_source()
c = 2
X_sink(X_sanitizer(a))
Y_sink(b, X_sanitizer(c))