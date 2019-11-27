a = "Lili"
while get():
    a = "ola"

#should not sanitize
a = mogrify(a)
execute(a)
