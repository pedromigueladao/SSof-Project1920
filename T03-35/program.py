uname = retrieve_uname(request)
uname = uname + uname
q = cursor.execute("SELECT pass FROM users WHERE user='%s'" % uname)
mark_safe()
mark_safe(uname, uname)
