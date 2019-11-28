uname = retrieve_uname(request)
escape_string(request)
q = cursor.execute("SELECT pass FROM users WHERE user='%s'" % uname)