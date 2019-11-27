uname = retrieve_uname(request)
q = get("SELECT pass FROM users WHERE user='%s'" % uname)
