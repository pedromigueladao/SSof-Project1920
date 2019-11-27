username = get('username')
out = ''
while username != '':
    c = substr(username, 0, 1)

    if c == '<':
        out = out + '<'
    elif c == 's':
        out = out + 's'
    elif c == 'c':
        out = out + 'c'
    elif c == 'r':
        out = out + 'r'
    elif c == 'i':
        out = out + 'i'
    elif c == 'p':
        out = out + 'p'
    elif c == 't':
        out = out + 't'
    elif c == '>':
        out = out + '>'
    elif c == '/':
        out = out + '/'

    username = substr(username, 1)
response = make_response(out)
