uname = retrieve_uname(request)
uname2 = mogrify(uname)
q = cursor.execute("SELECT pass FROM users WHERE user='%s'" % uname, uname2, ola)
