uname = retrieve_uname(request)
q = Ola("SELECT pass FROM users WHERE user='%s'" % uname)
