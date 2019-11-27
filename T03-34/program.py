uname = retrieve_uname(request)
uname2 = uname + mogrify(uname)
q = cursor.execute("SELECT pass FROM users WHERE user='%s'" % uname2)
